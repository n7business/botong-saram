---
id: marketing-1000
domain: marketing
claim: 홈페이지를 새 도메인으로 옮길 때 이전이 끝나기 전에 옛 사이트에 robots.txt 차단을 걸거나 서버를 먼저 끄면, 네이버가 주소가
  바뀐 것을 확인하지 못해 이전이 검색에 제대로 반영되지 않을 수 있습니다.
status: merged
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp.
  seen: '2026-11-24'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 사이트이전
- 도메인변경
- '301'
merged_into: marketing-0897
---
사이트를 옮길 때는 옛 주소마다 새 주소로 1:1 대응하는 301 HTTP redirect를 걸고, 새 사이트의 모든 페이지에 canonical 주소를 지정합니다. 그다음 새 사이트를 웹마스터도구에 등록하고 사이트맵을 제출합니다. 검색로봇이 옛 사이트를 방문해야 페이지가 옮겨진 것을 확인할 수 있으므로, 주요 페이지가 모두 새 주소로 바뀐 것을 확인하기 전에는 옛 사이트를 robots.txt로 막거나 서버·네트워크를 끊지 않습니다. 옛 주소로 들어오는 사용자가 없어진 뒤에 서버를 종료하고 웹마스터도구에서 옛 사이트를 삭제합니다.
