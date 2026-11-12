---
id: marketing-0197
domain: marketing
claim: 홈페이지가 네이버 검색에 안 뜨거나 정보가 갱신되지 않으면 robots.txt, 방화벽·보안 플러그인의 검색로봇(User-Agent 'Yeti')
  차단 여부, 페이지 meta robots의 noindex를 먼저 확인해 풀어야 하며, 로봇 차단이 필요할 때는 IP가 아니라 robots.txt로
  해야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-firewall
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: 네이버 검색 서비스를 위해 웹 문서를 수집하는 검색로봇은 Yeti라고 불리우며
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2027-01-04'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
- noindex
- Yeti
verified_by: 공식 출처
mentions: 2
---
robots.txt와 웹 서버, 방화벽에서 네이버 검색로봇 Yeti의 접근을 허용했는지 확인합니다. meta 태그에 noindex가 있으면 해당 페이지는 검색 반영에서 제외되므로 해제합니다. 메인 페이지나 중요한 콘텐츠를 frame 태그로 감쌌다면 일반 HTML 태그로 바꿉니다. 로봇을 꼭 차단해야 할 때는 IP 대역이 언제든 바뀔 수 있으므로 IP 기반으로 막지 말고 robots.txt를 씁니다. 직접 수정하기 어려우면 제작업체나 기술담당자에게 요청합니다.
