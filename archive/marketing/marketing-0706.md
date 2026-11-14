---
id: marketing-0706
domain: marketing
claim: 같은 내용의 홈페이지를 www 있는 주소와 없는 주소처럼 여러 주소로 열어 두지 말고 대표 주소 하나로 301 이동시켜야 하며, 주소가
  여러 개라고 네이버 검색에 더 잘 나오지 않고 오히려 중복으로 판정됩니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-15'
  quote: 여러 hostname 쓴다고 검색에 노출이 될 가능성이 높아지지 않습니다. 똑같은 내용은 중복 판정을 받습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 홈페이지
- 대표주소
- canonical
- '301'
merged_into: marketing-0625
---
주소를 여러 개 쓴다고 검색 노출 가능성이 높아지지 않고, 같은 내용은 중복으로 판정됩니다. www가 있는 주소와 없는 주소 중 하나를 대표 주소로 정하고, 나머지 주소는 대표 주소로 301 이동시키세요. 이동은 자바스크립트(document.location 등)가 아니라 서버의 HTTP redirect로 처리해야 합니다. 301 이동이 어렵다면 페이지 HTML에 rel="canonical"로 대표 주소를 적어 두면, 검색 결과에 중복 없이 대표 주소로 나올 가능성이 커집니다.
