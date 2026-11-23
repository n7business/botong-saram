---
id: marketing-0964
domain: marketing
claim: robots.txt로 파비콘·자바스크립트·CSS 파일 경로를 막지 말고, 검색에 내보내는 페이지와 같은 규칙으로 두거나 수집을 허용해야
  합니다.
status: merged
evidence: policy
confidence: 0.8
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-23'
  quote: 파비콘(favicon) 수집을 허용해 주세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- robots.txt
- 파비콘
- CSS
merged_into: marketing-0852
---
네이버 검색로봇은 파비콘, 자바스크립트, CSS를 그 파일을 쓰는 웹 페이지의 일부로 봅니다. 이 파일들이 막혀 있으면 페이지가 홈페이지 주인의 의도와 전혀 다르게 해석될 수 있습니다. 규칙이 서로 모순되면 로봇이 예외적으로 수집을 시도하기도 합니다. 관리자 페이지나 개인정보 페이지처럼 꼭 막아야 할 경로만 Disallow로 지정하고, 나머지 리소스는 허용해 두는 것이 안전합니다.
