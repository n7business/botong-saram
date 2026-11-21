---
id: marketing-0932
domain: marketing
claim: 홈페이지 메인 화면이 자바스크립트나 meta refresh로 다른 주소로 넘어가게 되어 있으면 네이버 웹마스터도구에서 사이트 소유 확인이
  되지 않으므로, HTTP redirect 방식으로 바꿔야 합니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-22'
  quote: 사이트의 메인 페이지가 자바스크립트 혹은 meta refresh 기법을 사용하여 redirect 된다면 지원이 불가능합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-22'
last_confirmed: '2026-11-22'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- 웹마스터도구
- 소유확인
- redirect
- 홈페이지
merged_into: marketing-0846
---
네이버 검색에 홈페이지를 올리려면 먼저 서치어드바이저 웹마스터도구에 사이트를 등록하고 소유 확인을 해야 합니다. 등록은 www.mysite.com이나 blog.mysite.com 같은 호스트 단위로만 됩니다. www.mysite.com/myid 같은 하위 경로는 등록할 수 없습니다. 소유 확인은 HTML meta 태그를 넣거나 HTML 파일을 올리는 방식으로 합니다. 메인 페이지가 자바스크립트나 meta refresh로 이동하거나, 확인용 태그가 frame 태그 안에 들어 있거나, 방화벽이 네이버 로봇을 막고 있으면 확인에 실패합니다. 직접 고치기 어렵다면 제작업체에 'HTTP redirect로 바꿔 달라'고 요청하세요.
