---
id: marketing-0492
domain: marketing
claim: 서버 부하 등으로 네이버 검색로봇을 잠시 막아야 할 때는 robots.txt로 막지 말고 웹마스터도구 수집 설정의 트래픽 제한을 최소로
  지정해야 기존 문서가 검색에서 빠지지 않는다.
status: verified
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 것을 권장합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2027-01-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 웹마스터도구
- 트래픽제한
- robots.txt
verified_by: 공식 출처
---
이벤트 기간 등에 서버가 버거워 검색로봇 방문을 잠시 줄이고 싶을 수 있습니다. 이때 robots.txt로 막으면 그동안 수집된 사이트 문서가 네이버 검색에서 제외될 수 있습니다. 네이버는 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 방법을 권장합니다. 방화벽에서 IP로 막는 방법도 권하지 않습니다. 검색로봇의 IP 대역은 언제든 바뀔 수 있기 때문입니다.
