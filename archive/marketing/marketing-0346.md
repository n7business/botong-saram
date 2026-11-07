---
id: marketing-0346
domain: marketing
claim: 네이버 검색에 반영되는 문서 수가 적으면 자바스크립트로만 처리한 내부 링크를 표준 <a href> 링크로 바꾸고, 사이트맵·RSS의 링크는
  상대 경로가 아닌 등록 호스트의 전체 주소로 고쳐야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-07'
  quote: 대상 링크가 자바스크립트 함수로만 표현되어 있어서 검색로봇은 해당 링크의 정확한 URL을 파악할 수 없음
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2027-01-04'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 내부링크
- 사이트맵
- nofollow
verified_by: 공식 출처
mentions: 1
---
링크를 자바스크립트 함수로만 처리하면 검색로봇이 정확한 URL을 파악하지 못해 다른 페이지를 찾아가기 어렵습니다. 내부 링크는 <a href="..."> 같은 표준 형식으로 제공합니다. 제출한 사이트맵과 RSS 안의 링크가 상대 경로이거나 링크의 호스트가 등록된 사이트와 다르면 네이버는 수집을 진행하지 않습니다. 페이지의 meta 태그에 nofollow가 있으면 페이지 내 링크를 수집하지 않으므로 이것도 해제합니다.
