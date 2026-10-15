import datetime
import markdown
import pandas
import pathlib
import requests
import tqdm
from requests_html import HTML

# load markdown text.

markdown_path = pathlib.Path.home() / 'git' / 'fiaf-cataloguing-manual' / 'markdown'
if not markdown_path.exists():
    raise Exception(f'{markdown_path} not found.')

markdown_text = ''
markdown_files = [x for x in markdown_path.rglob('*') if x.suffix == '.md']
for m in markdown_files:
    markdown_text += m.read_text()

# extract links.

html = markdown.markdown(markdown_text)
links = HTML(html=html).links
links = [x for x in links if 'http' in x]

# build report.

report_path = pathlib.Path.cwd() / 'audit_links.csv'
if not report_path.exists():
    df = pandas.DataFrame(columns=['url', 'timestamp', 'status_code'])
    for l in tqdm.tqdm([x for x in links], desc='checking links'):
        l = l.split(']')[0].replace('[','')
        try:
            r = requests.get(l)
            df.loc[len(df)] = [(l), (datetime.datetime.now().isoformat()), (r.status_code)]
        except:
            df.loc[len(df)] = [(l), (datetime.datetime.now().isoformat()), ('fail')]

    df.to_csv(report_path, index=False)
