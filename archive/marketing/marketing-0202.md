---
id: marketing-0202
domain: marketing
claim: 사이트 내부 링크를 자바스크립트 함수로만 처리하면 검색로봇이 URL을 파악하지 못해 다른 페이지를 찾아가지 못하므로, 표준 <a href>
  링크를 써야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: 대상 링크가 자바스크립트 함수로만 표현되어 있어서 검색로봇은 해당 링크의 정확한 URL을 파악할 수 없음
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
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
- 자바스크립트
- nofollow
verified_by: 공식 출처
---
네이버 검색에 반영된 문서 수가 적다면 페이지 내 링크 방식을 먼저 확인합니다. <a href="http://www.A.com">처럼 쓰면 검색로봇이 URL을 정확히 알 수 있지만, onClick 자바스크립트 함수로만 표현한 링크는 알 수 없습니다. 페이지 meta 태그의 nofollow도 해제해야 하며, nofollow가 있으면 페이지 내 링크를 수집하지 않습니다. 페이지의 모든 콘텐츠가 자바스크립트로 로딩되는 구조인지도 함께 점검합니다.
