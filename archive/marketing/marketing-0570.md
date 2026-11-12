---
id: marketing-0570
domain: marketing
claim: 페이지 이동(redirect)을 자바스크립트로 처리하면 검색로봇이 이동할 주소를 파악하기 어렵고 스팸 문서처럼 저평가될 수 있으므로,
  서버에서 HTTP 301 이동으로 처리해야 한다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-12'
  quote: 양질의 좋은 페이지임에도 스팸 문서 처리 과정에서 불필요하게 중요도가 낮은 것으로 저평가를 받을 수도 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 리다이렉트
- '301'
- 자바스크립트
merged_into: marketing-0461
---
location.href 같은 자바스크립트 이동은 검색로봇이 이해하기 어려운 방식입니다. 이동 정보를 숨기는 페이지는 스팸 문서에서 많이 보여서 좋은 페이지도 중요도가 낮게 평가될 수 있습니다. 주소를 영구히 바꿀 때는 서버에서 301로 응답하게 설정하세요. 방문자에게 이동 사실을 보여 주고 싶다면 meta refresh도 인식되지만, 네이버는 가능하면 HTTP 이동을 쓰라고 권장합니다.
