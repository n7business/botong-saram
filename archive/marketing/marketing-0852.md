---
id: marketing-0852
domain: marketing
claim: robots.txt로 파비콘이나 자바스크립트·CSS 파일 경로를 막지 말고, 검색에 노출할 페이지와 같은 규칙을 적용하거나 수집을 허용해야
  네이버가 페이지를 의도와 다르게 해석하지 않습니다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: 네이버 서치어드바이저
  seen: '2026-11-20'
  quote: 이들 리소스 URL도 참조하는 웹 문서와 규칙을 동일하게 설정해주시거나 기본적으로 수집을 허용해주시도록 설정 부탁드립니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2027-01-19'
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
verified_by: 공식 출처
---
네이버 검색로봇은 파비콘, 자바스크립트, CSS를 그 파일을 쓰는 웹 페이지의 일부로 봅니다. 이 리소스를 분석하지 못하면 페이지가 운영자의 의도와 전혀 다른 문서로 해석될 수 있습니다. 페이지는 허용하면서 그 리소스 경로만 막으면 규칙이 서로 어긋나 혼란이 생깁니다. robots.txt에서 이 파일들의 경로를 막지 말고, 참조하는 페이지와 같은 규칙을 적용하거나 기본적으로 수집을 허용하세요.
