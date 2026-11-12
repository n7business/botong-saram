---
id: marketing-0537
domain: marketing
claim: 홈페이지를 네이버 서치어드바이저 웹마스터도구에 등록해 소유확인을 마친 뒤 '요청-사이트맵 제출'로 XML 사이트맵을, '요청-RSS 제출'로
  최신글 본문 전체가 담긴 RSS를 내야 하며, 그 안의 링크가 상대 경로이거나 등록한 사이트와 호스트가 다르면 수집되지 않는다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-11'
  quote: 사이트 내의 최신글은 본문 전체를 포함하여 RSS 피드에 담아주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2027-01-08'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 사이트맵
- RSS
- 웹마스터도구
verified_by: 공식 출처
mentions: 1
---
사이트맵은 홈페이지에서 검색에 올라가야 할 주소 목록을 담은 XML 파일입니다. 네이버 서치어드바이저 웹마스터도구의 '요청-사이트맵 제출' 메뉴로 사이트맵을 내고, 새 글은 본문 전체를 넣은 RSS로 만들어 '요청-RSS 제출'로 냅니다. 사이트맵과 RSS 안의 링크는 https://로 시작하는 전체 주소로 쓰고, 등록한 사이트와 같은 호스트여야 합니다. 상대 경로로 쓰거나 호스트가 다르면 네이버가 그 링크를 수집하지 않습니다. robots.txt에 'Sitemap: 주소' 한 줄을 넣어 사이트맵 위치를 알려 둘 수도 있습니다.
