---
id: marketing-0934
domain: marketing
claim: 같은 내용으로 홈페이지나 주소를 여러 개 만들어도 네이버 노출은 늘지 않고 중복 판정을 받으므로, 대표 주소 하나를 정하고 나머지는 301
  redirect하거나 rel="canonical"로 대표 주소를 적어야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다. 똑같은 내용은 중복 판정을 받습니다.
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
- 중복콘텐츠
- canonical
- 301redirect
- 도메인
verified_by: 공식 출처
mentions: 1
---
노출을 늘리려고 똑같은 내용의 사이트나 주소를 여러 개 열면 검색 노출에서 불이익을 받을 수 있습니다. 같은 내용이라면 호스트 이름과 URL을 하나만 쓰세요. 예전 주소를 유지해야 하는 등 여러 주소가 꼭 필요하다면 대표 주소로 301 HTTP redirect를 거세요. www가 붙은 주소와 안 붙은 주소도 한쪽으로 모아야 합니다. 자바스크립트 이동(document.location 등)은 쓰지 마세요. 301 redirect가 어렵다면 <link rel="canonical">로 대표 주소를 적어 두세요. 그러면 검색 결과에 대표 URL로 중복 없이 노출될 가능성이 커집니다.
