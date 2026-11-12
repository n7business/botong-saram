---
id: marketing-0538
domain: marketing
claim: 페이지에 nofollow 메타 태그가 붙어 있으면 네이버가 그 페이지 안의 링크를 따라가지 않으므로, 검색에 잡히는 문서 수가 적다면
  nofollow부터 풀어야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-11'
  quote: nofollow가 표기된 페이지의 경우 페이지 내 링크 수집을 진행하지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2027-01-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- nofollow
- 메타태그
verified_by: 공식 출처
---
네이버 검색에 올라간 내 홈페이지 문서 수가 유난히 적다면 페이지 소스에 <meta name="robots" content="nofollow">가 있는지 확인합니다. 이 태그가 붙은 페이지는 안에 있는 링크를 네이버가 수집하지 않아서, 그 페이지에서 이어지는 내부 페이지를 찾지 못합니다. 홈페이지 제작 업체가 템플릿에 기본으로 넣어 둔 경우도 있으니 제작 업체에 확인을 요청합니다. 수집 대상이 아닌 페이지만 따로 막고, 메인·목록 페이지에서는 이 태그를 빼야 합니다.
