---
id: marketing-0820
domain: marketing
claim: 검색 노출을 늘리려고 같은 내용의 사이트나 주소를 여러 개 만들면 중복 판정을 받아 네이버 검색 노출에서 불이익을 받을 수 있으므로,
  대표 주소 하나를 정하고 나머지 주소는 그 대표 주소로 301 redirect해야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다. 똑같은 내용은 중복 판정을 받습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 이 경우 검색 노출에 불이익을 받을 수 있으니 유의하세요.
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
- 중복콘텐츠
- canonical
- redirect
verified_by: 공식 출처
---
같은 내용으로 도메인이나 사이트를 여러 개 만들어도 네이버 검색에 더 많이 나오지 않고, 오히려 중복 판정을 받아 노출에서 불이익을 받을 수 있습니다. 주소가 여러 개 있어야 한다면 사람들에게 알릴 대표 주소 하나를 정하고, 나머지 주소는 서버에서 대표 주소로 301 redirect하세요. www가 붙은 주소와 붙지 않은 주소도 한쪽으로 모아야 합니다. 301 redirect를 걸기 어렵다면 페이지에 <link rel="canonical">로 대표 주소를 적어 두세요. 모든 페이지의 제목을 똑같이 쓰지 말고, 페이지마다 그 페이지 내용을 설명하는 제목을 붙이세요.
