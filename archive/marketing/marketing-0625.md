---
id: marketing-0625
domain: marketing
claim: 같은 홈페이지에 www가 붙은 주소와 안 붙은 주소처럼 여러 주소가 있다면 하나를 대표 주소로 정해 나머지를 301로 이동시키고, 그게
  어려우면 rel="canonical"로 대표 주소를 적어야 중복 판정을 피할 수 있다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-13'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다. 똑같은 내용은 중복 판정을 받습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2027-01-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- canonical
- '301'
- 대표주소
- www
verified_by: 공식 출처
---
주소를 여러 개 쓴다고 네이버 검색에 노출될 가능성이 높아지지 않고, 똑같은 내용은 중복 판정을 받습니다. www가 있는 주소와 없는 주소 중 하나를 대표 주소로 정하고, 나머지 주소는 서버에서 HTTP 301로 대표 주소로 보내세요. 자바스크립트로 이동시키면 안 됩니다. 301 이동이 어렵다면 각 페이지 HTML의 <link> 태그에 rel="canonical"로 대표 주소를 적습니다. 대표 주소를 지정하면 검색 결과에 중복 없이 대표 URL로 나올 가능성이 커집니다.
