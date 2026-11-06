---
id: marketing-0238
domain: marketing
claim: 404 오류 페이지에서 '페이지가 없습니다'라는 문구만 띄우고 HTTP 200을 돌려주지 말고, 없는 페이지는 404 응답 코드를 그대로
  내보내야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp.
  seen: '2026-11-06'
  quote: “페이지가 없습니다”라는 내용만 출력하고 HTTP 200 OK return 하지 말아 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2027-01-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 오류페이지
- HTTP응답코드
verified_by: 공식 출처
---
없는 페이지는 사람에게 안내 문구를 보여 주는 것과 별개로 서버 응답도 404 Not Found로 보내야 합니다. 오류 페이지로 redirect하거나 안내 문구만 출력하고 200 OK를 돌려주면 안 됩니다. 권한 없는 페이지(403)와 서버 과부하(503)도 내용만 출력하고 200을 돌려주지 않도록 합니다. 방문자에게는 사이트 맞춤형 오류 페이지로 자연스럽게 안내하면 됩니다. 직접 수정하기 어려우면 제작업체나 기술담당자에게 응답 코드 확인을 요청하세요.
