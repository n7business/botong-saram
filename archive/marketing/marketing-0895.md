---
id: marketing-0895
domain: marketing
claim: 서버 점검이나 잠깐의 장애로 페이지를 임시로 다른 곳에 보낼 때는 302 redirect를 써야 네이버가 기존 페이지를 지워진 것으로
  오판해 검색 정보를 삭제하지 않습니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: 사이트의 장애나 잠시 페이지를 변경할 경우 302 Temporarily Moved 형식의 redirect를 사용해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2027-01-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- redirect
- '302'
- '301'
- 서버점검
verified_by: 공식 출처
merged_into: marketing-0998
---
사이트에 일시적인 장애가 있거나 잠시 공사 중 페이지로 돌릴 때는 서버에서 302(임시 이동) 형식으로 redirect해야 합니다. 응답이 없거나 다른 내용으로 바뀐 것으로 보이면 검색로봇은 그 페이지가 삭제됐다고 판단해 수집해 둔 기존 정보를 지울 수 있습니다. 반대로 주소를 아주 바꿀 때는 301(영구 이동)을 써야 기존 주소에 쌓인 검색 정보와 이용자 선호도 정보를 새 주소가 이어받습니다. 두 경우 모두 자바스크립트가 아닌 HTTP redirect로 처리해야 합니다.
