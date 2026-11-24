---
id: marketing-0900
domain: marketing
claim: 홈페이지의 메뉴·내부 링크를 onClick 같은 자바스크립트 함수로만 만들면 네이버 검색로봇이 연결된 주소를 알 수 없어 안쪽 페이지를
  수집하지 못하므로, <a href="전체주소"> 같은 표준 링크로 만들어야 합니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: 대상 링크가 자바스크립트 함수로만 표현되어 있어서 검색로봇은 해당 링크의 정확한 URL을 파악할 수 없음
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: 스팸 문서 처리 과정에서 불필요하게 중요도가 낮은 것으로 저평가를 받을 수도 있습니다.
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
- 자바스크립트
- 내부링크
- 홈페이지제작
verified_by: 공식 출처
mentions: 2
---
<span onClick="javascript:goto(A)">처럼 링크를 자바스크립트 함수로만 표현하면 검색로봇은 정확한 URL을 알 수 없어 그 뒤의 페이지를 찾아가지 못합니다. <a href="http://www.A.com">처럼 주소가 드러나는 표준 링크로 만들어야 합니다. 페이지 이동을 자바스크립트로 처리하는 것도 피해야 합니다. 이동 정보를 숨기는 페이지는 스팸 문서에서 자주 발견되기 때문에, 좋은 페이지도 중요도가 낮게 평가될 수 있습니다. 네이버 검색에 잡히는 문서 수가 적다면 제작업체에 메뉴와 링크가 어떤 방식으로 만들어졌는지 확인해 보세요.
