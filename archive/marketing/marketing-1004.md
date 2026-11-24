---
id: marketing-1004
domain: marketing
claim: 홈페이지 내부 링크를 onClick 같은 자바스크립트 함수로만 만들면 네이버 검색로봇이 링크 주소를 알 수 없어 그 뒤 페이지들을 수집하지
  못하므로, 링크는 <a href="주소"> 같은 표준 형식으로 만들어야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-24'
  quote: 페이지들의 링크 처리 시 자바스크립트만을 사용하면, 검색로봇이 어떤 URL 인지 정확하게 파악할 수 없어서
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: null
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
- 홈페이지
merged_into: marketing-0900
---
네이버 검색에 나오는 페이지 수가 적다면 메뉴와 버튼의 링크가 어떻게 만들어졌는지 확인합니다. <span onClick="javascript:goto(A)">처럼 자바스크립트 함수로만 이동하게 만든 링크는 검색로봇이 어느 주소인지 파악하지 못해 연결된 하위 페이지를 찾아가지 못합니다. 링크는 <a href="http://...">처럼 주소가 드러나는 표준 HTML로 만들어야 합니다. 제작업체에 홈페이지를 맡길 때 이 조건을 미리 요청하면 좋습니다.
