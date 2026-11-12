---
id: marketing-0571
domain: marketing
claim: 사이트 장애나 공사 등으로 잠시 페이지를 바꿀 때는 302 이동을 써야 하며, 그렇지 않으면 네이버 검색로봇이 페이지가 삭제됐거나 다른
  내용으로 바뀐 것으로 보고 기존 검색 정보를 지울 수 있다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-12'
  quote: 사이트의 장애나 잠시 페이지를 변경할 경우 302 Temporarily Moved 형식의 redirect를 사용해 주세요.
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
- '302'
- 사이트점검
- 리다이렉트
merged_into: marketing-0461
---
검색로봇은 응답을 받지 못하면 페이지가 삭제된 것으로 잘못 판단할 수 있습니다. 잠깐 바뀐 것을 알아채지 못하면 기존 정보를 지울 수도 있습니다. 리뉴얼 공사나 서버 점검 동안 '공사중' 페이지로 보낼 때는 301이 아닌 302로 응답하게 하세요. 영구적인 주소 변경에만 301을 씁니다.
