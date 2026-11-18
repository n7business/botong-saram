---
id: marketing-0821
domain: marketing
claim: 홈페이지가 네이버 검색에 나오지 않으면 메인 페이지와 각 페이지의 meta 태그에 noindex가 들어 있는지 먼저 확인해 지워야 하며,
  noindex가 붙은 페이지는 검색 반영에서 빠집니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2027-01-18'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- noindex
- 검색누락
verified_by: 공식 출처
---
홈페이지 제작업체가 개발 중에 넣어 둔 <meta name="robots" content="noindex">가 그대로 남아 있으면 그 페이지는 네이버 검색에 반영되지 않습니다. 검색에 안 나온다면 메인 페이지부터 이 태그가 있는지 확인하고 지워 달라고 요청하세요. 같은 위치에 nofollow가 있으면 네이버가 그 페이지 안의 링크를 따라가 수집하지 않으므로 함께 지워야 합니다. 메인 페이지나 중요한 내용을 frame 태그로 감싸 두었거나 내용 전부를 자바스크립트로 불러오는 구조여도 검색에 잘 반영되지 않으니, 일반 HTML 태그로 바꾸는 것이 좋습니다.
