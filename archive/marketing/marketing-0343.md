---
id: marketing-0343
domain: marketing
claim: 검색 노출을 늘리려고 같은 내용의 사이트나 주소를 여러 개 만들면 노출 가능성은 높아지지 않고 불이익을 받을 수 있으므로, 대표 주소
  하나로 모아야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp.
  seen: '2026-11-07'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-07'
  quote: 이 경우 검색 노출에 불이익을 받을 수 있으니 유의하세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2027-01-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 중복콘텐츠
- canonical
- '301'
verified_by: 공식 출처
---
같은 내용이면 되도록 단일 호스트명과 단일 URL을 씁니다. 네이버는 똑같은 내용은 중복 판정을 받으며, 동일한 콘텐츠로 여러 사이트를 개설하면 검색 노출에 불이익을 받을 수 있다고 안내합니다. 여러 주소를 꼭 써야 한다면 대표 주소로 301 redirect하고, www가 있는 주소와 없는 주소도 한쪽으로 redirect합니다. 301 redirect가 어려우면 HTML에 rel="canonical"로 대표 주소를 적습니다.
