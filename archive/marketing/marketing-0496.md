---
id: marketing-0496
domain: marketing
claim: robots.txt로 자바스크립트·CSS·파비콘 경로를 막지 말고, 이 파일들은 해당 페이지와 같은 규칙을 적용하거나 수집을 허용해야
  검색로봇이 페이지를 의도대로 해석한다.
status: verified
evidence: policy
confidence: 0.82
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: 기본적으로 수집을 허용해주시도록 설정 부탁드립니다.
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
- 자바스크립트
- 파비콘
verified_by: 공식 출처
---
요즘 검색로봇은 HTML만 읽지 않습니다. 페이지에 딸린 자바스크립트·CSS·파비콘도 그 페이지의 일부로 보고 함께 분석합니다. 페이지는 허용하면서 이런 파일이 든 폴더만 robots.txt로 막으면, 페이지 내용이 사장님 의도와 다르게 해석될 수 있습니다. 규칙이 서로 어긋나 로봇이 예외적으로 수집을 시도하는 혼란도 생깁니다. 제작업체가 robots.txt에 /js, /css 같은 경로를 Disallow로 넣었는지 확인하고, 페이지와 같은 규칙을 적용하거나 허용으로 바꾸세요.
