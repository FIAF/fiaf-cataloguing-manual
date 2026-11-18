"""Report Wayback candidates for URLs cited in the manual's Markdown."""

import argparse
import csv
import json
import re
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode, urldefrag, urlsplit
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
URL_PATTERN = re.compile(r"""https?://[^\s<>"\[\]]+""")
FIELDS = (
    'status', 'source_url', 'archive_url', 'capture_timestamp_utc',
    'references', 'detail',
)


def extract_sources(docs):
    sources = defaultdict(set)
    for path in sorted(docs.rglob('*.md')):
        display_path = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            for match in URL_PATTERN.finditer(line):
                url = match.group().rstrip('.,;')
                while url.endswith(')') and url.count(')') > url.count('('):
                    url = url[:-1].rstrip('.,;')
                # The Creative Commons badge is an image asset, separate from its link.
                if urlsplit(url).hostname != 'licensebuttons.net':
                    sources[url].add(f'{display_path}:{number}')
    return sources


def fetch_json(endpoint, params):
    with urlopen(f'{endpoint}?{urlencode(params)}', timeout=15) as response:
        return json.load(response)


def lookup(url):
    for attempt in range(3):
        try:
            data = fetch_json('https://archive.org/wayback/available', {'url': url})
            if data.get('error'):
                raise ValueError(data['error'])
            capture = data['archived_snapshots'].get('closest')
            if not capture:
                return 'no snapshot returned', '', '', ''
            if capture.get('available') and capture.get('status') == '200':
                replay = capture['url'].replace('http://web.archive.org/', 'https://web.archive.org/', 1)
                return 'found', replay, capture['timestamp'], ''
            return 'unsuitable snapshot', '', '', f'Capture status {capture.get("status")}'
        except (URLError, TimeoutError, ValueError, KeyError) as error:
            detail = str(error)
            if attempt < 2:
                time.sleep(2 ** attempt)
    return 'lookup error', '', '', detail


def cdx_fallback(url, result):
    params = [
        ('url', url), ('output', 'json'), ('fl', 'timestamp,original,mimetype'),
        ('filter', 'statuscode:200'), ('limit', '-1'),
    ]
    if urlsplit(url).path.lower().endswith('.pdf'):
        params.append(('filter', 'mimetype:application/pdf'))
    status, replay, timestamp, detail = result
    try:
        data = fetch_json('https://web.archive.org/cdx/search/cdx', params)
        if len(data) > 1:
            timestamp, original, mime = data[-1]
            replay = f'https://web.archive.org/web/{timestamp}/{original}'
            return 'found', replay, timestamp, f'CDX fallback ({mime})'
        note = 'CDX returned no matching capture'
    except (URLError, TimeoutError, ValueError) as error:
        note = f'CDX lookup error: {error}'
    return status, replay, timestamp, ' | '.join(filter(None, (detail, note)))


def harvest(docs, output, workers):
    sources = extract_sources(docs)
    lookup_urls = sorted({
        urldefrag(url).url for url in sources
        if urlsplit(url).hostname != 'web.archive.org'
    })
    print(f'Looking up {len(lookup_urls)} distinct URLs', flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = dict(zip(lookup_urls, pool.map(lookup, lookup_urls)))
        # Retry remaining service errors at a slower pace before consulting CDX.
        for url, result in results.items():
            if result[0] == 'lookup error':
                results[url] = lookup(url)
                time.sleep(1.2)
        unresolved = [url for url, result in results.items() if result[0] != 'found']
        fallbacks = list(pool.map(lambda url: cdx_fallback(url, results[url]), unresolved))
        results.update(zip(unresolved, fallbacks))

    with output.open('w', encoding='utf-8', newline='') as report:
        writer = csv.writer(report, lineterminator='\n')
        writer.writerow(FIELDS)
        for url, references in sorted(sources.items()):
            base, fragment = urldefrag(url)
            if urlsplit(url).hostname == 'web.archive.org':
                match = re.match(r'/web/(\d{14})/', urlsplit(url).path)
                status, replay, timestamp, detail = 'already linked', url, match[1] if match else '', ''
            else:
                status, replay, timestamp, detail = results[base]
                if replay and fragment:
                    replay = f'{replay}#{fragment}'
            writer.writerow((status, url, replay, timestamp, ' | '.join(sorted(references)), detail))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path, help='path for the generated CSV')
    parser.add_argument('--docs', type=Path, default=ROOT / 'markdown', help='Markdown source directory')
    parser.add_argument('--workers', type=int, default=3, help='maximum simultaneous lookups')
    args = parser.parse_args()
    if args.workers < 1:
        parser.error('--workers must be at least 1')
    docs = args.docs.resolve()
    if not docs.is_dir():
        parser.error(f'Markdown directory does not exist: {docs}')
    harvest(docs, args.output, args.workers)


if __name__ == '__main__':
    main()
