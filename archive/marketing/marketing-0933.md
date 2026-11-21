---
id: marketing-0933
domain: marketing
claim: 홈페이지가 네이버 검색에 나오지 않거나 갱신되지 않으면 방화벽·서버가 네이버 검색로봇(Yeti)을 IP로 막고 있는지 확인해야 하며,
  로봇 IP 대역은 언제든 바뀌므로 꼭 막아야 할 때도 IP 대신 robots.txt로 제어해야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: 부득이하게 검색 로봇을 차단해야 하는 경우 IP 기반으로 차단하지 마세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-firewall
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 방화벽의 제한 설정 때문에 접근이 차단되지는 않았는지 점검해야합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: '2027-01-18'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 검색로봇
- Yeti
- 방화벽
- robots.txt
verified_by: 공식 출처
mentions: 2
---
네이버 검색로봇의 이름(User-Agent)은 Yeti입니다. 웹 서버나 방화벽에서 Yeti의 접근을 허용해야 홈페이지가 검색에 수집됩니다. 검색에 안 나오거나 정보가 갱신되지 않으면 보안 설정이 로봇을 막고 있지 않은지 먼저 확인하세요. 로봇을 막아야 할 때도 IP로 차단하지 말고 표준 방식인 robots.txt를 쓰세요. 네이버 로봇의 IP 대역은 예고 없이 바뀔 수 있습니다.
