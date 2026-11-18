---
id: marketing-0822
domain: marketing
claim: robots.txt는 사이트 루트에 일반 텍스트 파일(text/plain)로 두어야 하며, HTML 문서로 응답하면 안의 규칙이 무시되고
  '모두 허용'으로 해석될 수 있고 서버 오류(5xx)로 응답하면 '모두 허용하지 않음'으로 해석됩니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 만약, robots.txt가 HTML 문서로 반환된다면 그 안에 유효한 규칙이 있더라도 robots.txt가 없음 (모두 허용)으로
    해석될 수도 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2027-01-18'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
verified_by: 공식 출처
---
robots.txt는 반드시 http://www.example.com/robots.txt처럼 사이트 루트에 두고, 일반 텍스트 파일로 열리게 하세요. 이 파일이 HTML 문서로 응답되면 안에 막아 둔 규칙이 있어도 파일이 없는 것처럼 '모두 허용'으로 해석될 수 있습니다. 반대로 서버 오류(5xx)가 나면 네이버 검색로봇은 '모두 허용하지 않음'으로 해석하므로, 사이트 전체가 수집되지 않을 수 있습니다. robots.txt 규칙은 같은 호스트·프로토콜에만 적용됩니다. 그래서 www 주소의 robots.txt는 www 없는 주소나 https 주소에는 적용되지 않는다는 점에 주의하세요. 파일을 고친 뒤에는 웹마스터도구의 robots.txt 도구에서 수집 요청을 눌러 네이버에 바로 알리세요.
