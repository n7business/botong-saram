---
id: marketing-0936
domain: marketing
claim: 홈페이지 페이지의 meta 태그에 noindex가 있으면 그 페이지는 네이버 검색에서 빠지고, nofollow가 있으면 페이지 안의 링크를
  수집하지 않으므로, 검색에 내보낼 페이지에서는 두 설정을 풀어야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: '2027-01-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- noindex
- nofollow
- 검색누락
- frame
verified_by: 공식 출처
mentions: 1
---
메인 페이지나 글이 네이버에 안 나오면 페이지 소스에 <meta name="robots" content="noindex">가 있는지 확인하세요. 제작 중에 넣어 두고 잊는 경우가 많습니다. noindex가 붙은 페이지는 검색 반영에서 빠집니다. 공공기관 같은 일부 예외만 내부 정책에 따라 반영될 수 있습니다. 검색에 잡힌 문서 수가 적다면 nofollow 설정도 확인하세요. nofollow가 붙은 페이지는 안의 링크를 따라가지 않습니다. 메인 페이지를 frame 태그로 감싸거나 콘텐츠를 모두 자바스크립트로 불러오는 구조도 반영을 막을 수 있습니다. 이럴 때는 일반 HTML 태그를 쓰세요.
