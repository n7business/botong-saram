---
id: marketing-0490
domain: marketing
claim: robots.txt는 검색로봇에게 보내는 요청일 뿐 보안 장치가 아니므로, 고객 개인정보·관리자 페이지처럼 노출되면 안 되는 내용은 로그인
  등 다른 방법으로 막아야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: 로그인 기능 등 다른 방법을 통하여 보호하거나 다른 차단 방법을 사용해야 합니다.
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
- 개인정보
- 보안
verified_by: 공식 출처
---
네이버 일반 검색로봇은 robots.txt 규칙을 지키지만, 광고 정보 수집이나 링크 미리보기용 로봇처럼 특수한 용도의 로봇은 이 규칙을 보지 않거나 완전히 지키지 않을 수 있습니다. 그래서 고객 명단, 상담 신청 내역, 관리자 화면 같은 페이지를 robots.txt의 Disallow만으로 숨겼다고 생각하면 위험합니다. 이런 페이지는 로그인을 거쳐야만 열리게 하거나 다른 차단 방법을 함께 써야 합니다. robots.txt는 검색에 노출하고 싶지 않은 경로를 알려 주는 용도로만 쓰세요.
