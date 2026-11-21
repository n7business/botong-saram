---
id: marketing-0939
domain: marketing
claim: 홈페이지 주소를 옮기거나 개편할 때 redirect가 여러 번 이어지게 두지 말고 최대 5회를 넘기지 않아야 하며, 거쳐 가는 모든 주소와
  최종 주소가 수집 가능한 정상 페이지여야 네이버가 수집합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: 연속해서 연결되는 리다이렉션 횟수는 최대 5회 이상을 넘기지 않는 것을 추천합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- redirect
- 사이트개편
- 도메인이전
merged_into: marketing-0826
---
주소가 연속해서 이동하는 횟수가 검색로봇의 허용 범위를 넘거나, 자기 자신으로 계속 돌아오는 무한 redirect가 생기면 그 페이지는 수집되지 않습니다. 개편 뒤에는 바뀌기 전 주소와 바뀐 뒤 주소가 제대로 이어지는지 확인하세요. 중간 주소 하나라도 robots.txt로 막혀 있거나 없는 페이지면, 처음과 끝 주소가 정상이어도 수집되지 않을 수 있습니다. 이런 문제는 브라우저 화면만 봐서는 알기 어려우니 개발자 도구로 확인하거나 제작업체에 점검을 맡기세요. redirect 변경이 검색에 반영되기까지는 시간이 걸립니다. 그러니 기존에 검색에 노출되던 주소의 redirect는 한동안 유지하세요.
