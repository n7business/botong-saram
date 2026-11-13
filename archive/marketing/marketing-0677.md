---
id: marketing-0677
domain: marketing
claim: 홈페이지 점검·공사 등으로 잠시 다른 페이지를 보여 줄 때는 302 이동을 써야 하며, 그러지 않으면 네이버 검색로봇이 페이지가 삭제됐다고
  판단해 기존 검색 정보를 지울 수 있습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: 302형식의 redirect를 사용하여 서버에서 응답해주시기 바랍니다.
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
- '302'
- redirect
- 점검
- 자바스크립트
verified_by: 공식 출처
---
일시적인 장애나 잠깐의 페이지 변경 중에 로봇이 응답을 받지 못하면 그 페이지가 삭제된 것으로 잘못 판단할 수 있습니다. 공사 중 안내 페이지로 보낼 때는 서버에서 302(임시 이동) 응답으로 이동시켜야 기존에 수집된 정보가 유지됩니다. 반대로 주소를 영구히 바꿀 때는 301을 씁니다. 자바스크립트로 이동시키면 로봇이 이해하기 어렵고 스팸 문서처럼 낮게 평가될 수 있으므로, 이동은 서버의 HTTP redirect로 처리하세요.
