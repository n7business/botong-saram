---
id: marketing-0045
domain: marketing
claim: 서버 부담 등으로 네이버 검색로봇을 잠시 막아야 할 때는 robots.txt로 차단하지 말고 웹마스터도구의 수집 설정에서 트래픽 제한량을
  최소로 낮춰야 하며, robots.txt로 막으면 그 기간에 수집된 문서가 검색에서 빠질 수 있다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 것을 권장합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2027-01-02'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 웹마스터도구
- 검색로봇
- robots.txt
verified_by: 공식 출처
---
사이트 성능 문제나 내부 사정으로 네이버 검색로봇 접근을 일시 차단해야 하는 경우가 있다. 이때 robots.txt에 Disallow를 넣으면 차단 기간 동안 수집된 사이트 내 문서가 네이버 검색에서 제외될 수 있다. 대신 네이버 웹마스터도구 '수집 설정'에서 트래픽 제한량을 최소로 지정하면 기존 검색 반영을 유지하면서 로봇 방문 부하만 줄일 수 있다. 서버가 과부하일 때 오류 페이지는 200이 아닌 503 응답으로 돌려주어야 로봇이 일시 장애로 이해한다. 문제가 해결되면 트래픽 제한을 다시 풀어 수집이 정상화되는지 웹마스터도구 수집 현황에서 확인한다.
