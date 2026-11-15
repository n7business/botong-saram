---
id: marketing-0761
domain: marketing
claim: 홈페이지 주소를 옮길 때 자바스크립트로 이동시키면 네이버가 스팸성 문서처럼 낮게 평가할 수 있으므로, 서버에서 301 HTTP redirect로
  옮겨야 기존 검색 평가를 이어받을 수 있습니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: 자바스크립트를 이용한 redirect 처리는 자제해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: '2027-01-15'
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
- 사이트개편
verified_by: 공식 출처
---
자바스크립트(location.href 등)로 이동시키면 검색로봇이 어느 주소로 가는지 파악하기 어렵습니다. 이동 정보를 숨기는 방식은 스팸 문서에 많이 쓰여서, 좋은 페이지도 중요도가 낮게 평가될 수 있습니다. 주소를 아예 바꿨다면 서버에서 301(영구 이동)로 응답해야 기존 검색 정보와 이용자 선호도 정보를 새 주소가 이어받습니다. 연속 이동은 5회를 넘기지 말고, 거쳐 가는 주소와 최종 주소가 모두 수집 가능한 정상 페이지인지 확인해야 합니다. 개편 뒤 한동안은 예전에 검색에 나오던 주소에도 이동 설정을 남겨 두는 것이 좋습니다.
