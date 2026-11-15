---
id: marketing-0762
domain: marketing
claim: 홈페이지가 잠시 장애를 겪거나 공사 중일 때는 302(임시 이동) redirect로 안내 페이지를 보여 줘야 하며, 그러지 않으면 네이버가
  기존 페이지를 삭제된 것으로 판단해 검색 정보를 지울 수 있습니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: 사이트의 장애나 잠시 페이지를 변경할 경우 302 Temporarily Moved 형식의 redirect를 사용해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- '302'
- 서버장애
- 공사중
merged_into: marketing-0677
---
일시적인 장애로 검색로봇이 응답을 받지 못하면 페이지가 삭제된 것으로 잘못 판단할 수 있습니다. 잠깐 바꾼 내용을 다른 정보로 바뀐 것으로 보고 기존 정보를 지울 수도 있습니다. 공사 중이거나 장애가 났을 때는 서버에서 302 형식으로 공사 안내 페이지에 이동시켜야 기존 수집 정보가 유지됩니다. 영구적으로 옮길 때 쓰는 301과 헷갈리지 않도록 주의해야 합니다.
