---
id: marketing-0195
domain: marketing
claim: 검색 노출을 늘리려고 같은 내용의 사이트나 주소를 여러 개 만들면 노출 가능성은 높아지지 않고 중복 판정이나 불이익을 받을 수 있으므로,
  대표 주소 하나만 운영해야 한다.
status: merged
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다. 똑같은 내용은 중복 판정을 받습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 중복콘텐츠
- 대표주소
- canonical
merged_into: marketing-0025
---
같은 내용은 되도록 호스트명과 URL을 하나로 통일합니다. 여러 주소를 꼭 써야 하면 대표 주소로 301 redirect를 설정합니다. www가 있는 주소와 없는 주소도 한쪽으로 redirect합니다. 301 redirect가 어려우면 HTML에 rel="canonical"로 대표 주소를 적습니다. 모든 페이지의 제목을 똑같이 두지 말고, 페이지마다 주제를 정확히 설명하는 제목을 씁니다.
