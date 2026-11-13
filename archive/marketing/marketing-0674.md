---
id: marketing-0674
domain: marketing
claim: 홈페이지 메뉴와 글 목록의 링크를 자바스크립트 함수(onClick)로만 만들면 네이버 검색로봇이 연결된 주소를 알 수 없어 안쪽 페이지를
  수집하지 못하므로, 링크는 <a href="주소"> 형태의 표준 링크로 만들어야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-14'
  quote: 대상 링크가 자바스크립트 함수로만 표현되어 있어서 검색로봇은 해당 링크의 정확한 URL을 파악할 수 없음
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
- 홈페이지
- 링크
- 자바스크립트
- nofollow
verified_by: 공식 출처
---
네이버 검색로봇은 페이지 안의 링크를 따라가면서 다른 페이지를 찾습니다. <span onClick="javascript:goto(A)">처럼 자바스크립트 함수로만 만든 링크는 로봇이 정확한 주소를 알 수 없어서 그 뒤의 페이지들을 찾아가지 못합니다. 메뉴, 글 목록, 상세 페이지로 가는 링크는 <a href="http://...">처럼 주소가 드러나는 표준 링크로 만들어야 합니다. 검색에 반영되는 문서 수가 적다면 제작업체에 링크 방식부터 확인해 달라고 요청하세요. 페이지의 robots 메타 태그에 nofollow가 들어 있으면 그 페이지 안의 링크를 수집하지 않으므로, 이것도 함께 확인해야 합니다.
