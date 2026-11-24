---
id: marketing-0997
domain: marketing
claim: 없는 페이지에서 '페이지가 없습니다'라는 안내만 띄우고 HTTP 200 OK로 응답하거나 오류 페이지로 redirect하지 말고, 404
  Not Found 같은 실제 오류 코드로 응답해야 합니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp.
  seen: '2026-11-24'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: null
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
- 오류페이지
merged_into: marketing-0894
---
홈페이지에서 없는 주소나 옛 주소로 들어오면 서버가 404 Not Found로 응답하게 설정합니다. 권한이 없는 페이지는 403, 서버 과부하는 503처럼 상황에 맞는 코드를 돌려줍니다. 방문자에게는 사이트에 맞게 꾸민 오류 안내 페이지를 보여 주어도 되지만, 그 페이지도 200 OK로 응답하면 안 됩니다. 별도의 오류 페이지 주소로 redirect하는 방식도 쓰지 않습니다. 이 설정은 제작업체나 개발자에게 요청하면 됩니다.
