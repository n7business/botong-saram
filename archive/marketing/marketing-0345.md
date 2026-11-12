---
id: marketing-0345
domain: marketing
claim: 사이트나 콘텐츠가 네이버 검색에 나오지 않으면 글을 더 쓰기 전에 robots.txt·방화벽의 Yeti 차단과 noindex 설정, 그리고
  frame이나 자바스크립트에 의존한 구조인지부터 확인하고, 중요한 콘텐츠는 일반 HTML로 제공해야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-07'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2027-01-05'
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
mentions: 1
---
먼저 robots.txt와 웹 서버·방화벽이 네이버 검색로봇(User-Agent: Yeti)의 접근을 허용하는지 확인합니다. meta 태그에 noindex가 있으면 해제합니다. noindex가 표기된 페이지는 검색 반영에서 제외되기 때문입니다. 페이지의 모든 콘텐츠가 자바스크립트로 로딩되거나 HTML frame 태그로 감싸여 있는지도 살피고, 중요한 콘텐츠는 일반 HTML 태그로 제공하는 것이 권장됩니다. 직접 고치기 어려우면 사이트 제작업체나 기술담당자에게 요청합니다. 부득이하게 로봇을 차단할 때도 IP 대역은 언제든 바뀔 수 있으므로 IP 기반으로 막지 말고 robots.txt를 씁니다.
