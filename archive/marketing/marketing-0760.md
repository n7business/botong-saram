---
id: marketing-0760
domain: marketing
claim: 홈페이지에 없는 페이지는 '페이지가 없습니다' 문구만 띄우고 200 OK로 응답하거나 오류 페이지로 이동시키지 말고, 404 Not Found
  응답 코드를 그대로 돌려줘야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: '2027-01-12'
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
mentions: 1
---
주소를 잘못 입력했거나 지워진 옛 주소로 들어온 경우, 서버는 404 Not Found 응답 코드를 돌려줘야 합니다. 안내 문구만 보여 주고 200 OK로 응답하면 검색로봇은 그 화면을 정상 페이지로 받아들입니다. 오류 페이지로 이동(redirect)시키는 방식도 쓰지 말아야 합니다. 권한이 없는 페이지(403)나 서버 과부하(503)도 마찬가지로 응답 코드를 지켜야 합니다. 방문자에게는 사이트에 맞게 꾸민 안내 페이지를 보여 주되, 응답 코드는 바꾸지 않습니다. 홈페이지 제작업체에 '404 페이지가 실제 404 코드로 응답하는지' 확인해 달라고 요청하면 됩니다.
