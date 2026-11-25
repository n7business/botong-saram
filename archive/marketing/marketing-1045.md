---
id: marketing-1045
domain: marketing
claim: 검색 노출을 늘리려고 같은 내용의 사이트나 주소(호스트명)를 여러 개 만들면 중복 판정을 받아 오히려 불이익을 받을 수 있으므로, 대표
  주소 하나만 쓰고 나머지 주소는 대표 주소로 301 redirect 해야 합니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-25'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
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
- 홈페이지
merged_into: marketing-0934
---
네이버는 같은 내용이 여러 주소에 있으면 중복으로 판정하고, 주소를 여러 개 쓴다고 노출 가능성이 높아지지도 않습니다. 사람들에게 알리고 싶은 고유 주소 하나를 대표(canonical) 주소로 정하세요. 옛 주소나 www가 붙은 주소와 붙지 않은 주소처럼 여러 주소를 꼭 유지해야 한다면 모두 대표 주소로 301 redirect 합니다. 서버 설정상 301 redirect가 어렵다면 HTML의 <link rel="canonical">로 대표 주소를 적어 두세요. redirect는 자바스크립트가 아니라 HTTP 방식으로 해야 합니다.
