---
id: marketing-0824
domain: marketing
claim: 홈페이지가 네이버 검색에 나오지 않거나 내용이 갱신되지 않으면 방화벽이 네이버 검색로봇(Yeti)을 막고 있는지 확인해야 하며, 로봇을
  꼭 막아야 할 때도 IP로 차단하지 말고 robots.txt를 써야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 부득이하게 검색 로봇을 차단해야 하는 경우 IP 기반으로 차단하지 마세요. 검색 로봇의 IP 대역은 언제든지 변경될 수 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-firewall
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 방화벽의 제한 설정 때문에 접근이 차단되지는 않았는지 점검해야합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2027-01-18'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 방화벽
- Yeti
- 검색로봇
verified_by: 공식 출처
merged_into: marketing-0933
---
보안을 위해 켜 둔 방화벽이 네이버 검색로봇까지 막아서 검색에 나오지 않는 경우가 있습니다. 네이버 검색로봇의 이름(User-Agent)은 'Yeti'이니, 호스팅 업체나 제작업체에 Yeti의 접근을 허용해 달라고 요청하세요. 검색로봇을 꼭 막아야 한다면 IP로 차단하지 마세요. 네이버 검색로봇의 IP 대역은 언제든 바뀔 수 있으므로, 표준 방식인 robots.txt로 막는 것이 권장됩니다. Yeti를 사칭한 접근인지 의심되면 접속 IP를 역 DNS로 조회해 .naver.com으로 끝나는지 확인하세요.
