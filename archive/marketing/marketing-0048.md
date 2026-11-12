---
id: marketing-0048
domain: marketing
claim: 네이버 검색에 반영된 우리 사이트 문서 수가 적으면 내부 링크가 자바스크립트 onClick만으로 되어 있는지, meta robots에
  nofollow가 있는지, 사이트맵·RSS 링크가 상대 경로나 다른 호스트로 적혀 있는지 확인해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: nofollow가 표기된 페이지의 경우 페이지 내 링크 수집을 진행하지 않습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2027-01-02'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 내부링크
- nofollow
- 사이트맵
verified_by: 공식 출처
---
검색로봇은 표준 a href 링크로만 다음 페이지 URL을 정확히 파악하므로, 메뉴·상품 목록이 span onClick 같은 자바스크립트 함수로만 연결되어 있으면 그 뒤의 페이지를 찾아가지 못한다. 페이지 meta 태그에 'robots nofollow'가 있으면 그 페이지 안의 링크 수집을 하지 않으므로 해제한다. 웹마스터도구에 제출한 사이트맵·RSS 안의 링크가 상대 경로이거나 등록한 사이트와 호스트가 다르면 수집하지 않으므로 전체 URL로 적는다. 본문이 전부 자바스크립트로만 로딩되거나 frame 태그로 감싸져 있어도 반영이 안 될 수 있으니 중요한 콘텐츠는 일반 HTML로 둔다. 확인은 네이버 검색창에 'site:내도메인'을 입력해 반영된 문서 수를 보는 것으로 시작한다.
