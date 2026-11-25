---
id: marketing-1049
domain: marketing
claim: 네이버 검색로봇을 막아야 할 때는 IP 주소로 차단하지 말아야 합니다. 검색로봇의 IP 대역은 언제든 바뀔 수 있으니 표준 방식인 robots.txt로
  제어하고, 방화벽이 검색로봇(Yeti)을 막고 있지 않은지도 점검해야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-25'
  quote: 부득이하게 검색 로봇을 차단해야 하는 경우 IP 기반으로 차단하지 마세요.
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
- 검색로봇
- 방화벽
- Yeti
merged_into: marketing-0933
---
네이버 검색로봇의 이름(User-Agent)은 Yeti이고, IP 대역은 예고 없이 바뀔 수 있습니다. 그래서 IP 기반으로 차단하면 의도와 다르게 동작할 수 있으며, 네이버는 robots.txt로 접근을 제어하라고 권장합니다. 사이트가 검색되지 않거나 정보가 갱신되지 않는다면 방화벽이 User-Agent나 IP로 Yeti를 막고 있지 않은지 확인하세요. 접속한 IP가 진짜 네이버 로봇인지는 역 DNS 조회 결과가 .naver.com으로 끝나는지로 확인할 수 있습니다.
