---
id: marketing-0489
domain: marketing
claim: 홈페이지에서 없는 페이지를 열었을 때 '페이지가 없습니다' 문구만 띄우고 정상 응답(200 OK)을 보내면 안 되고, 실제 404 응답
  코드를 보내야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2027-01-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 홈페이지
- '404'
- HTTP응답코드
verified_by: 공식 출처
---
주소가 틀렸거나 지워진 페이지에는 서버가 '404 Not Found' 응답 코드를 보내야 합니다. 화면에만 '페이지가 없습니다'라고 쓰고 응답 코드는 200 OK로 보내면, 검색로봇이 빈 페이지를 정상 문서로 오해할 수 있습니다. 모든 오류를 하나의 오류 페이지로 이동(redirect)시키는 방식도 쓰지 말라고 안내합니다. 권한이 없는 페이지는 403, 서버 과부하는 503처럼 상황에 맞는 코드를 그대로 보내고, 방문자에게는 사이트에 맞춘 안내 화면을 보여 주면 됩니다. 제작업체에 '없는 주소를 열면 404 코드가 나가는지' 확인을 요청하세요.
