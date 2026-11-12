---
id: marketing-0458
domain: marketing
claim: 검색 노출을 늘리려고 같은 내용의 사이트나 도메인 주소를 여러 개 만들면 노출이 늘지 않고 중복 판정으로 불이익을 받을 수 있으니, 대표
  주소 하나로 운영해야 한다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: 네이버 서치어드바이저 (NAVER Corp.)
  seen: '2026-11-09'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저 (NAVER Corp.)
  seen: '2026-11-09'
  quote: 이 경우 검색 노출에 불이익을 받을 수 있으니 유의하세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2027-01-08'
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
- 도메인
verified_by: 공식 출처
merged_into: marketing-0566
---
네이버는 같은 내용을 담은 여러 사이트를 중복으로 판정합니다. 호스트명을 여러 개 써도 노출 가능성은 높아지지 않습니다. 옛 주소 유지 등으로 여러 주소를 꼭 써야 한다면 대표(canonical) 주소로 301 redirect 하세요. www가 붙은 주소와 안 붙은 주소도 한쪽으로 모아야 합니다. 301 redirect가 어려우면 HTML에 rel="canonical"로 대표 주소를 적어 둡니다.
