---
id: marketing-0675
domain: marketing
claim: 홈페이지 메인이나 글이 네이버 검색에 나오지 않으면 페이지의 meta 태그에 noindex가 들어 있는지 확인하고 있으면 지워야 하며,
  noindex가 붙은 페이지는 검색 반영에서 빠집니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
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
- noindex
- frame
- 검색 미노출
verified_by: 공식 출처
---
<meta name="robots" content="noindex">가 들어 있는 페이지는 네이버 검색 반영에서 제외됩니다. 홈페이지 제작 도구나 개발 중에 쓰던 설정이 그대로 남아 메인 페이지에 noindex가 붙어 있는 경우가 있습니다. 메인이 검색에 안 나오면 robots.txt와 방화벽 설정, noindex 태그 순서로 점검하세요. 내용 전체를 자바스크립트로 불러오거나 HTML frame 태그로 감싼 페이지도 검색에 반영되지 않을 수 있으므로, 중요한 내용은 일반 HTML로 넣어야 합니다.
