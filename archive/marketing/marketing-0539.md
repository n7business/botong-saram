---
id: marketing-0539
domain: marketing
claim: 부득이하게 네이버 검색로봇을 막아야 할 때도 IP 주소로 막지 말고 robots.txt를 써야 한다. 네이버 로봇의 IP 대역은 언제든
  바뀔 수 있기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-11'
  quote: 부득이하게 검색 로봇을 차단해야 하는 경우 IP 기반으로 차단하지 마세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2027-01-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 검색로봇
- 방화벽
- robots.txt
verified_by: 공식 출처
---
방화벽이나 보안 설정에서 특정 IP를 막아 두면 네이버 검색로봇(Yeti)이 의도와 다르게 막히거나 풀릴 수 있습니다. 네이버는 로봇의 IP 대역이 예고 없이 바뀔 수 있다고 밝히고 있으므로, 수집을 막거나 허용하는 일은 표준 방식인 robots.txt로 해야 합니다. 들어온 접속이 진짜 네이버 로봇인지 확인하려면 IP를 역 DNS로 조회해 .naver.com으로 끝나는지 보고, 그 도메인을 다시 조회했을 때 원래 IP가 나오는지 확인합니다. 보안 업체나 호스팅 업체에 방화벽 관리를 맡겼다면 이 점을 전달해 두는 것이 좋습니다.
