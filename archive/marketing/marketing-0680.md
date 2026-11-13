---
id: marketing-0680
domain: marketing
claim: 네이버 웹마스터도구에 제출한 사이트맵·RSS 안의 링크가 상대 경로이거나 등록한 사이트와 호스트가 다르면 네이버가 수집하지 않으므로,
  링크는 등록한 도메인 그대로의 전체 주소로 적어야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: 링크가 상대 경로로 지정되어 있는 경우, 링크의 호스트가 등록된 사이트와 일치하지 않는 경우 수집을 진행하지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2027-01-13'
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
---
사이트맵과 RSS는 제출만 하면 되는 게 아니라 안의 링크 형식이 맞아야 합니다. '/post/1'처럼 상대 경로로 적힌 링크는 수집하지 않습니다. 등록한 사이트가 www.mysite.com인데 링크가 mysite.com이면 호스트가 달라서 역시 수집하지 않습니다. 검색에 반영되는 문서 수가 적다면 제출한 사이트맵·RSS 파일을 열어 링크가 'https://등록한도메인/...' 형태의 전체 주소인지 확인하세요. 사이트맵 위치는 robots.txt에 'Sitemap: 주소' 줄로 함께 적어 둘 수 있습니다.
