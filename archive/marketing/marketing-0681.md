---
id: marketing-0681
domain: marketing
claim: robots.txt는 사이트 루트에 일반 텍스트 파일로 두고 정상(2xx) 응답이 나오게 해야 하며, 서버 오류(5xx)가 나면 네이버가
  '모두 수집 금지'로 해석하고 HTML 문서로 내보내면 규칙이 무시될 수 있습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: 만약, robots.txt가 HTML 문서로 반환된다면 그 안에 유효한 규칙이 있더라도 robots.txt가 없음 (모두 허용)으로
    해석될 수도 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2027-01-13'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
- 응답 코드
- 웹마스터도구
verified_by: 공식 출처
---
네이버 검색로봇은 robots.txt의 응답 코드에 따라 다르게 움직입니다. 2xx면 규칙을 읽어 따르고, 4xx(파일 없음 등)면 모두 허용으로 봅니다. 5xx 서버 오류면 모두 허용하지 않음으로 해석해 사이트 전체가 수집에서 막힐 수 있습니다. robots.txt가 HTML 문서로 내보내지면 안에 규칙이 있어도 파일이 없는 것(모두 허용)으로 해석될 수 있으므로 text/plain 형식으로 만들어야 합니다. 규칙은 같은 호스트·프로토콜·포트에만 적용되므로 www가 있는 주소와 없는 주소, http와 https 각각에 맞게 두어야 합니다. 파일을 고친 뒤에는 웹마스터도구의 robots.txt 도구에서 수집 요청과 검증을 하세요.
