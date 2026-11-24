---
id: marketing-0894
domain: marketing
claim: 홈페이지의 없는 페이지는 '페이지가 없습니다' 안내만 띄우고 200 OK로 응답하거나 오류 페이지로 redirect하지 말고, 404
  Not Found 응답 코드를 그대로 돌려줘야 네이버 검색로봇이 정상 페이지와 구분합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2027-01-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 홈페이지
- 오류페이지
- HTTP응답코드
verified_by: 공식 출처
mentions: 1
---
주소를 잘못 쳤거나 지운 페이지에는 서버가 404 Not Found 응답 코드를 돌려줘야 합니다. 화면에 '페이지가 없습니다'라고 띄우면서 응답 코드는 200 OK로 보내면 검색로봇은 이 화면을 정상 문서로 받아들입니다. 모든 오류를 오류 안내 페이지 한 곳으로 redirect하는 것도 하지 말아야 합니다. 권한이 없는 페이지는 403, 서버에 부하가 걸렸을 때는 503처럼 상황에 맞는 코드를 쓰고, 방문자에게 보여 줄 안내 화면은 그 코드를 유지한 채 사이트 맞춤 오류 페이지로 꾸미면 됩니다. 제작업체에 맡긴 사이트라면 이 설정을 확인해 달라고 요청하세요.
