---
id: marketing-0460
domain: marketing
claim: 홈페이지 메뉴·링크를 자바스크립트로만 처리하거나 내용 전체를 자바스크립트·frame으로 불러오면 네이버 로봇이 내부 페이지를 찾지 못하므로,
  표준 a href 링크와 일반 HTML로 만들어야 한다.
status: verified
evidence: policy
confidence: 0.88
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저 (NAVER Corp.)
  seen: '2026-11-09'
  quote: 표준에 맞는 링크 URL정보를 제공하는 것을 권장합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2027-01-08'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 자바스크립트
- 링크
- 홈페이지제작
verified_by: 공식 출처
mentions: 1
---
링크를 onClick 같은 자바스크립트 함수로만 표현하면 검색로봇은 연결된 URL을 알 수 없어 그 뒤 페이지를 수집하지 못합니다. 페이지 내용이 모두 자바스크립트로 로딩되거나 frame 태그 안에 들어 있으면 검색에 반영되지 않을 수 있습니다. 메인 페이지처럼 중요한 페이지에는 frame 대신 일반 HTML 태그를 쓰세요. 검색에 잡히는 문서 수가 적다면 제작업체에 링크 구조부터 확인을 요청하세요.
