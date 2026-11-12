---
id: marketing-0024
domain: marketing
claim: 홈페이지 메인이나 특정 페이지가 네이버 검색에 안 뜨면 HTML head의 meta robots 태그에 noindex가 있는지 먼저 확인해
  제거해야 하며, noindex가 있는 페이지는 검색에서 통째로 제외된다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-03'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
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
- noindex
- 검색누락
- 홈페이지
verified_by: 공식 출처
merged_into: marketing-0197
---
제작업체가 테스트 중 넣어둔 <meta name="robots" content="noindex"> 태그가 남아 있으면 아무리 콘텐츠를 잘 써도 네이버 검색에 반영되지 않는다. 브라우저에서 페이지 소스 보기로 'noindex'를 검색해 있으면 지운다. 같은 자리에 nofollow가 있으면 그 페이지 안의 링크를 따라가지 않아 하위 페이지 수집이 끊기므로 함께 확인한다. 추가로 robots.txt와 방화벽이 네이버 로봇(Yeti)을 막고 있지 않은지, 메인 페이지가 frame 태그로 감싸져 있지 않은지도 같이 본다.
