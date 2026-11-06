---
id: marketing-0240
domain: marketing
claim: robots.txt는 사이트 루트에 일반 텍스트 파일로 두고 2xx로 응답하게 해야 하며, 서버 오류(5xx)가 나면 네이버 검색로봇이
  '모두 허용하지 않음'으로, HTML로 반환되면 '모두 허용'으로 해석할 수 있다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp.
  seen: '2026-11-06'
  quote: 만약, robots.txt가 HTML 문서로 반환된다면 그 안에 유효한 규칙이 있더라도 robots.txt가 없음 (모두 허용)으로
    해석될 수도 있습니다.
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
- robots.txt
- HTTP응답코드
verified_by: 공식 출처
---
robots.txt는 사이트 루트 디렉터리에 두고 text/plain 형식으로 접근할 수 있어야 합니다. 응답이 5xx이면 '모두 허용하지 않음'으로 해석되며, 이전에 정상 수집된 규칙이 있으면 그 규칙이 일시적으로 쓰일 수 있습니다. 응답이 4xx이면 '모두 허용'으로 해석됩니다. HTML 문서로 반환되면 안에 유효한 규칙이 있어도 파일이 없는 것(모두 허용)으로 해석될 수 있어, 막아 둔 페이지의 수집 금지 규칙이 무시될 위험이 있습니다. 수정한 뒤에는 웹마스터도구의 robots.txt 도구로 수집 요청과 검증을 하세요.
