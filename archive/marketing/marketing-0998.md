---
id: marketing-0998
domain: marketing
claim: 홈페이지 주소를 영구히 바꿀 때는 301 redirect를, 장애나 공사로 잠시 다른 페이지로 보낼 때는 302 redirect를 써야
  네이버가 기존 페이지를 삭제된 것으로 잘못 판단하지 않고 기존 검색 정보를 유지합니다.
status: verified
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp.
  seen: '2026-11-24'
  quote: 사이트의 장애나 잠시 페이지를 변경할 경우 302 Temporarily Moved 형식의 redirect를 사용해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2027-01-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- redirect
- '301'
- '302'
- 홈페이지
verified_by: 공식 출처
mentions: 1
---
주소를 아예 옮겼다면 서버에서 301 redirect로 응답해야 기존 주소의 검색 평가와 이용자 선호 정보가 새 주소로 넘어갑니다. 서버 장애나 잠깐의 공사 때문에 공사중 페이지로 보낼 때는 302 redirect를 씁니다. 이렇게 하지 않고 응답이 끊기면 검색로봇이 페이지가 삭제됐거나 다른 정보로 바뀌었다고 판단해 기존 정보를 지울 수 있습니다. 두 경우 모두 자바스크립트가 아니라 서버의 HTTP redirect로 처리해야 합니다.
