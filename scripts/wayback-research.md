# Wayback Machine link conversion

The Internet Archive’s public Wayback Availability API can supply dated playback links for existing captures. A batch script can request one result per distinct external URL using `GET https://archive.org/wayback/available?url=...`. The documented endpoint accepts a single URL. Sending two `url` parameters in a live test returned one result. [FIAF issue #575](https://github.com/FIAF/fiaf-cataloguing-manual/issues/575) · [Internet Archive developer tutorial](https://archive.org/developers/tutorial-get-snapshot-wayback.html)

## Availability lookup

```sh
curl --get --data-urlencode 'url=https://www.fiafnet.org/' \
  --data-urlencode 'timestamp=20231001' \
  https://archive.org/wayback/available
```

Read `archived_snapshots.closest` and use its `url` when `available` is true and the capture `status` is `"200"`. URL-encode the input so query strings survive. The optional `timestamp` asks for the closest capture to a reference date. Omitting it asks for the latest available capture. An HTTP 200 from the lookup can also contain an empty `archived_snapshots` object. Keep a separate outcome for lookup errors, including an observed response with `error.code=timeout` and empty snapshots. [Internet Archive API reference](https://archive.org/help/wayback_api.php)

On 18 November 2026, the example returned capture `20231003220933` with `available: true` and status `"200"`. Its playback URL also returned HTTP 200. A synthetic missing path returned HTTP 200 with empty snapshots. [Availability request](https://archive.org/wayback/available?url=https%3A%2F%2Fwww.fiafnet.org%2F&timestamp=20231001) · [Playback URL](https://web.archive.org/web/20231003220933/https://www.fiafnet.org/) · [Missing-path request](https://archive.org/wayback/available?url=https%3A%2F%2Fexample.com%2Fwayback-test-nonexistent-575-61f16)

## Alternatives

- **CDX** lists captures and can filter by date range or captured status when editors need to choose among versions. A live query for the FIAF homepage returned HTTP and bare-host variants for the HTTPS `www` URL. Review the returned original URL and replay when the distinction matters. [Internet Archive’s CDX documentation](https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server#readme) · [CDX request](https://web.archive.org/cdx/search/cdx?url=https%3A%2F%2Fwww.fiafnet.org%2F&output=json&fl=timestamp%2Coriginal%2Cstatuscode&filter=statuscode%3A200&limit=2)
- **Save Page Now** can create a capture for a live page when lookup yields no suitable result. The Internet Archive documents single-page capture and describes an automation API. Some sites restrict crawling or have SSL settings that prevent saving. Capture submission was outside this lookup trial. [Save Pages in the Wayback Machine](https://help.archive.org/help/save-pages-in-the-wayback-machine/) · [Internet Archive’s Save Page Now announcement](https://blog.archive.org/2019/10/23/the-wayback-machines-save-page-now-is-new-and-improved/)

## Fit for the manual

A scan of inline HTTP(S) links found 102 distinct destinations outside Wayback and 14 existing Wayback link occurrences. The current audit script reports live HTTP status and uses a hard-coded checkout path. A conversion pass could generate a reviewable source-to-capture mapping for those distinct URLs, with capture dates, misses and lookup errors. Review the cited page and any target fragments before applying replacements, since a successful response establishes availability but does not verify the cited content. [Current link audit](audit_links.py)
