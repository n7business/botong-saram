---
id: marketing-0676
domain: marketing
claim: 홈페이지 도메인을 옮길 때는 구 사이트의 각 주소를 새 사이트의 같은 페이지로 1:1로 301 이동시켜야 하며, 이전이 끝나기 전에 구
  사이트에 robots.txt 차단을 걸거나 서버를 먼저 끄면 안 됩니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2027-01-13'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 사이트 이전
- 도메인 변경
- '301'
verified_by: 공식 출처
---
네이버는 중소 규모 사이트라면 모든 주소를 한꺼번에 옮기라고 권장합니다. 구 사이트 주소는 새 사이트의 같은 페이지로 1:1 대응하는 301 HTTP redirect로 이동시키고, 새 사이트 모든 페이지에 대표 주소(canonical)를 지정한 뒤 웹마스터도구에 새 사이트를 등록하고 사이트맵을 제출합니다. 구 사이트에 robots.txt 차단을 먼저 걸거나 서버를 먼저 끄면 로봇이 페이지가 옮겨졌는지 확인하러 오는 것조차 막혀서 이전이 반영되지 않을 수 있습니다. 주요 페이지가 모두 새 주소로 바뀐 것을 확인한 다음 구 사이트를 닫으세요. 대표 주소를 자주 바꾸면 사이트 품질 평가에 영향을 주므로, 이전은 브랜드 변경처럼 꼭 필요할 때만 해야 합니다.
