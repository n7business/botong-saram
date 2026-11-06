---
id: marketing-0245
domain: marketing
claim: 페이지 콘텐츠가 네이버 검색에 반영되지 않으면 내용 전체가 자바스크립트로 로딩되거나 frame 태그로 감싸인 구조인지 확인하고, 중요한
  콘텐츠는 일반 HTML로 제공해야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp.
  seen: '2026-11-06'
  quote: 페이지 내의 모든 콘텐츠가 자바스크립트로 로딩되는 구조인지 확인하세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2027-01-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 자바스크립트
- frame
- 색인
verified_by: 공식 출처
---
콘텐츠가 검색에 반영되지 않을 때는 noindex 설정과 함께 페이지 구조를 확인해야 합니다. 페이지 내 모든 콘텐츠가 자바스크립트로 로딩되는지, HTML frame 태그로 감싸여 있는지 점검하세요. 네이버 가이드는 표준 HTML 마크업으로 콘텐츠를 제공하고 중요한 콘텐츠에는 frame 대신 일반 HTML 태그를 쓰라고 권장합니다. 메인 페이지처럼 중요한 페이지도 frame 대신 일반 HTML 태그를 쓰는 것이 권장됩니다. 제작 도구나 업체로 만든 사이트라면 어떤 구조로 출력되는지 확인을 요청하세요.
