---
id: marketing-0938
domain: marketing
claim: robots.txt는 사이트 루트에 일반 텍스트 파일(text/plain)로 두어야 합니다. 서버 오류(5xx)로 응답하면 네이버가 '모두
  수집 금지'로 해석하고, HTML 문서로 반환하면 규칙이 있어도 '파일 없음(모두 허용)'으로 해석할 수 있습니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: '''모두 허용하지 않음''으로 해석합니다.'
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: '2027-01-21'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- robots.txt
- 응답코드
- 웹마스터도구
verified_by: 공식 출처
---
robots.txt는 반드시 http://www.example.com/robots.txt처럼 루트에 두고, 일반 텍스트 파일로 열려야 합니다. 네이버 로봇은 응답 코드에 따라 다르게 움직입니다. 2xx면 규칙을 따르고, 4xx면 모두 허용으로 봅니다. 5xx면 모두 금지로 보는데, 이전에 받아 둔 규칙이 있으면 잠시 그 규칙을 쓸 수 있습니다. HTTP redirect는 5회까지만 따라갑니다. robots.txt 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www가 붙은 주소와 붙지 않은 주소, http와 https는 각각 따로 관리해야 합니다. 파일을 고친 뒤에는 웹마스터도구의 robots.txt 도구에서 수집 요청을 누르고 페이지별 수집 가능 여부를 테스트해 보세요.
