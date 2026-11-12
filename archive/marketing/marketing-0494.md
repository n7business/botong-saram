---
id: marketing-0494
domain: marketing
claim: www가 붙은 주소와 붙지 않은 주소가 둘 다 열리면 한쪽을 대표 주소로 정해 HTTP 301로 보내고, 그게 어려우면 rel="canonical"로
  대표 주소를 표시해야 한다.
status: verified
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: www가 있는 경우와 없는 경우는 여러분의 선호도에 따라 한 쪽으로 redirect 해야 합니다.
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
- canonical
- '301'
- 대표주소
verified_by: 공식 출처
---
www.내가게.com과 내가게.com처럼 같은 내용이 여러 주소로 열리면 중복으로 판정될 수 있습니다. 어느 한쪽을 대표 주소로 정하고, 다른 주소로 들어오면 서버에서 301 redirect로 대표 주소로 보내야 합니다. 이동은 자바스크립트가 아니라 HTTP 방식으로 처리해야 합니다. 301 설정이 어렵다면 페이지 HTML에 rel="canonical" 링크로 대표 주소를 적으면 됩니다. robots.txt 규칙은 호스트·프로토콜별로 따로 적용되므로 www/비www, http/https 각각에서 설정을 확인하세요.
