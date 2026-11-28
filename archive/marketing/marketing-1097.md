---
id: marketing-1097
domain: marketing
claim: 서버 장애나 공사로 홈페이지를 잠시 다른 페이지로 돌릴 때는 301이 아니라 302 redirect를 써야 네이버 검색로봇이 기존 페이지를
  삭제된 것으로 오해하지 않고, 원래 수집해 둔 정보를 지웁니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-28'
  quote: 사이트의 장애나 잠시 페이지를 변경할 경우 302 Temporarily Moved 형식의 redirect를 사용해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2027-01-27'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- redirect
- '302'
- 서버장애
verified_by: 공식 출처
---
사이트에 일시적인 장애가 있거나 잠시 페이지를 바꾸는 경우, 검색로봇은 응답을 받지 못하면 그 페이지가 삭제됐다고 판단할 수 있습니다. 바뀐 내용을 다른 정보로 받아들여 기존 정보를 지울 수도 있습니다. 이를 막으려면 서버에서 302(임시 이동) 형식으로 redirect 해야 합니다. 주소를 아예 옮길 때만 301(영구 이동)을 씁니다.
