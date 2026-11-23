---
id: marketing-0961
domain: marketing
claim: 페이지 이동을 자바스크립트로 처리해 이동할 주소를 숨기면 스팸 문서처럼 보여 좋은 페이지도 네이버에서 낮게 평가받을 수 있으므로, 주소
  이동은 HTTP redirect로 처리해야 합니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-23'
  quote: 자바스크립트를 이용한 redirect 처리는 자제해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2027-01-22'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- redirect
- 스팸
verified_by: 공식 출처
---
자바스크립트 redirect는 검색로봇이 어느 주소로 넘어가는지 파악하기 어렵습니다. 네이버는 이동 정보를 숨기는 페이지가 스팸성 문서에서 많이 발견된다고 밝혔습니다. 그래서 내용이 좋은 페이지도 스팸 처리 과정에서 중요도가 낮게 매겨질 수 있습니다. 방문자에게 이동을 알리고 싶다면 meta refresh도 인식되지만, 되도록 서버의 HTTP redirect(영구 이동은 301)를 쓰는 것이 좋습니다.
