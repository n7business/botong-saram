---
id: marketing-0047
domain: marketing
claim: 없는 페이지는 '페이지가 없습니다' 내용만 보여주고 200 OK로 응답하거나 오류 페이지로 redirect하지 말고 404 응답 코드를
  그대로 돌려줘야 검색로봇이 삭제된 페이지를 정확히 인식한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
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
- '404'
- HTTP응답코드
- 홈페이지
verified_by: 공식 출처
---
상품을 내리거나 글을 삭제한 뒤 '페이지가 없습니다' 안내만 띄우면서 HTTP 200 OK를 돌려주면 검색로봇은 정상 페이지로 보고 계속 수집한다. 없는 페이지는 404 Not Found, 권한 없는 페이지는 403, 서버 과부하는 503처럼 의미에 맞는 응답 코드를 유지해야 한다. 안내 문구는 사이트 맞춤형 오류 페이지로 자연스럽게 보여주되, 응답 코드는 바꾸지 않는다. 존재하지 않는 URL을 메인 페이지나 별도 오류 페이지로 redirect하는 설정도 피한다. 홈페이지 빌더나 쇼핑몰 솔루션을 쓰면 브라우저 개발자 도구 네트워크 탭에서 삭제된 주소의 응답 코드가 404인지 확인한다.
