---
id: marketing-0026
domain: marketing
claim: 홈페이지 주소나 페이지 URL을 바꿀 때는 자바스크립트가 아닌 서버의 301 redirect로 옛 주소를 새 주소에 연결해야 기존 검색
  평가가 이어지고, 일시 장애·공사중 페이지는 302를 써야 기존 정보가 지워지지 않는다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-03'
  quote: 사이트나 페이지를 변경할 경우 301 Permanently Moved 형식의 redirect를 사용해 주세요.
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
- 리다이렉트
- '301'
- 도메인변경
verified_by: 공식 출처
---
URL을 바꾸면서 옛 주소를 그냥 버리면 네이버 로봇은 새 사이트를 전혀 다른 신규 사이트로 보고 기존에 쌓인 검색 노출·이용자 선호 정보를 쓰지 못한다. 옛 주소에서 새 주소로 1:1 대응하는 301(영구 이동) redirect를 서버 설정으로 걸어둔다. location.href 같은 자바스크립트 redirect는 로봇이 이해하기 어렵고 스팸 문서에서 흔한 방식이라 저평가될 수 있다. 공사중 페이지나 잠깐 장애로 페이지를 바꿀 때는 302(임시 이동)를 써야 로봇이 원래 페이지를 삭제된 것으로 오판하지 않는다. 연속 redirect는 5회를 넘기지 말고, 변경 반영에 시간이 걸리므로 옛 주소 redirect는 한동안 유지한다.
