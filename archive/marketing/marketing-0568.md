---
id: marketing-0568
domain: marketing
claim: 페이지 사이 링크를 자바스크립트 함수(onClick 등)로만 걸면 네이버 검색로봇이 주소를 알 수 없어 다른 페이지를 찾아가지 못하므로,
  링크는 <a href="주소"> 형식의 표준 링크로 걸어야 한다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-12'
  quote: 대상 링크가 자바스크립트 함수로만 표현되어 있어서 검색로봇은 해당 링크의 정확한 URL을 파악할 수 없음
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
- 내부링크
- 자바스크립트
- 홈페이지
merged_into: marketing-0460
---
<span onClick="javascript:goto(A)">처럼 함수로만 만든 링크는 검색로봇이 어떤 주소인지 파악하지 못합니다. 그러면 그 뒤에 있는 서비스 소개나 후기 페이지가 수집되지 않을 수 있습니다. 메뉴와 버튼 링크는 <a href="http://...">처럼 실제 주소가 드러나게 만들어야 합니다. 검색되는 문서 수가 적을 때 함께 점검할 항목입니다.
