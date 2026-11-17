---
id: marketing-0712
domain: marketing
claim: robots.txt로 파비콘이나 자바스크립트·CSS 파일 경로를 막지 말고, 검색에 나오는 페이지와 같은 규칙을 주거나 수집을 허용해야
  하며, 막아 두면 페이지가 의도와 다르게 해석될 수 있습니다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-15'
  quote: 파비콘(favicon) 수집을 허용해 주세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: '2027-01-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
- 파비콘
- CSS
- 자바스크립트
verified_by: 공식 출처
mentions: 1
---
네이버 검색로봇은 파비콘, 자바스크립트, CSS를 그 파일을 쓰는 웹 페이지의 일부로 봅니다. 페이지는 수집을 허용하면서 이런 파일 경로만 robots.txt로 막으면 규칙이 서로 부딪칩니다. 이때 로봇이 규칙을 따르지 않고 수집을 시도하거나, 리소스를 읽지 못해 페이지를 의도와 다르게 해석할 수 있습니다. 이런 파일에는 참조하는 페이지와 같은 규칙을 주거나 기본으로 수집을 허용하세요.
