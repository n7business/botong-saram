---
id: marketing-0935
domain: marketing
claim: 네이버 웹마스터도구에 사이트맵(XML)과 최신글 본문 전체가 담긴 RSS를 제출하되, 그 안의 링크를 상대 경로로 쓰거나 등록한 사이트와
  다른 호스트로 적으면 수집되지 않습니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: 링크의 호스트가 등록된 사이트와 일치하지 않는 경우 수집을 진행하지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 사이트맵
- RSS
- 웹마스터도구
merged_into: marketing-0823
---
사이트맵은 웹마스터도구 '요청-사이트맵 제출' 메뉴에, RSS는 '요청-RSS 제출' 메뉴에 냅니다. 사이트맵은 수집할 URL 목록을 담은 XML 파일입니다. 이미 수집되는 사이트라도 사이트맵을 내면 더 잘 수집됩니다. RSS에는 최신글을 본문 전체까지 담으세요. 사이트맵·RSS 안의 링크는 등록한 사이트와 같은 호스트의 전체 주소(https://www.내도메인/...)로 적어야 합니다. 상대 경로나 다른 호스트로 적으면 수집하지 않습니다. robots.txt에 'Sitemap: 주소' 줄을 넣어 사이트맵 위치를 알려 줄 수도 있습니다.
