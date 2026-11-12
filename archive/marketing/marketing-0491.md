---
id: marketing-0491
domain: marketing
claim: robots.txt 주소가 서버 오류(5xx)를 내면 네이버는 사이트 전체를 수집 금지로 해석하므로, robots.txt는 사이트 맨
  위 경로에서 정상 응답(2xx)을 주는 일반 텍스트 파일로 두어야 한다.
status: verified
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: '''모두 허용하지 않음''으로 해석합니다.'
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
- robots.txt
- 서버오류
verified_by: 공식 출처
---
네이버 검색로봇은 robots.txt를 열었을 때 받은 응답 코드에 따라 다르게 움직입니다. 5xx 서버 오류이면 '모두 허용하지 않음'으로 해석하고, 4xx이면 '모두 허용'으로 봅니다. robots.txt가 HTML 문서로 내려가면 안에 규칙을 적어 두었어도 파일이 없는 것으로 취급될 수 있습니다. 이동(redirect)은 HTTP 방식으로 5번까지만 따라가고 HTML·자바스크립트 이동은 해석하지 않습니다. 브라우저에서 내 사이트 주소 뒤에 /robots.txt를 붙여 열어 보고, 웹마스터도구의 robots.txt 도구로 검증하세요.
