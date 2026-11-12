---
id: marketing-0046
domain: marketing
claim: 홈페이지가 네이버 검색에 안 뜨거나 정보가 갱신되지 않으면 방화벽·보안 플러그인이 네이버 검색로봇(User-Agent 'Yeti')을
  막고 있는지 확인해야 하며, 로봇 차단은 IP가 아니라 robots.txt로 해야 한다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: 부득이하게 검색 로봇을 차단해야 하는 경우 IP 기반으로 차단하지 마세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-firewall
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: 네이버 검색 서비스를 위해 웹 문서를 수집하는 검색로봇은 Yeti라고 불리우며
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
- 방화벽
- 검색로봇
- Yeti
verified_by: 공식 출처
merged_into: marketing-0197
---
홈페이지 보안 설정이나 호스팅 방화벽이 봇 접근을 일괄 차단하면 네이버 검색로봇도 함께 막혀 검색에 나오지 않거나 옛 정보가 그대로 남는다. 네이버 일반 검색로봇의 이름은 Yeti이며 User-Agent에 'compatible; Yeti/1.1; +https://naver.me/spd'가 들어간다. 서버 로그나 방화벽 기록의 IP를 역 DNS 조회(host 또는 nslookup)해 .naver.com으로 끝나면 네이버 로봇이다. 검색로봇의 IP 대역은 예고 없이 바뀌므로 IP 기반 차단은 하지 말고, 접근 제어가 필요하면 표준 방식인 robots.txt를 쓴다. 방화벽 설정을 직접 바꾸기 어렵다면 호스팅 업체나 제작업체에 'Yeti 로봇 허용'을 요청한다.
