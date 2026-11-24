---
id: marketing-0897
domain: marketing
claim: 홈페이지 도메인을 옮길 때는 이전이 끝날 때까지 구 사이트에 robots.txt 차단을 걸거나 서버를 먼저 끄지 말고, 구 주소를 새
  주소로 1:1로 301 redirect한 뒤 주요 페이지가 모두 바뀐 것을 확인하고 나서 구 사이트를 정리해야 합니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2027-01-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 사이트이전
- 도메인변경
- '301'
verified_by: 공식 출처
mentions: 1
---
구 사이트의 각 주소는 새 사이트의 대응하는 주소로 1:1 HTTP 301 redirect를 걸고, 새 사이트의 모든 페이지에는 canonical 주소를 지정합니다. 그다음 웹마스터도구에 새 사이트를 등록하고 사이트맵을 제출합니다. 이전이 끝나기 전에 구 사이트에 robots.txt 차단을 걸거나 서버·네트워크를 먼저 멈추면, 검색로봇이 페이지가 옮겨졌는지 확인하러 들어오지 못해 이전이 반영되지 않을 수 있습니다. 검색 결과에서 주요 페이지가 모두 새 주소로 바뀐 것을 확인하고, 구 사이트로 들어오는 방문자도 없어졌을 때 서버를 끄고 웹마스터도구에서 구 사이트를 삭제하세요. 중소규모 사이트는 모든 URL을 한 번에 옮기는 것이 권장됩니다.
