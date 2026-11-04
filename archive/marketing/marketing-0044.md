---
id: marketing-0044
domain: marketing
claim: 'robots.txt가 없으면 네이버 검색로봇은 사이트의 모든 페이지를 수집하므로, 관리자·회원정보 페이지처럼 검색에 나오면 안 되는
  경로만 Disallow로 지정하고 ''Disallow: /''로 전체를 막지 않아야 한다.'
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: 네이버 서치어드바이저
  seen: '2026-11-03'
  quote: robots.txt 파일이 없다면 모든 콘텐츠를 수집할 수 있도록 간주합니다.
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
- robots.txt
- 홈페이지
- 검색노출
verified_by: 공식 출처
---
robots.txt는 사이트 최상위(예: 내도메인/robots.txt)에 일반 텍스트 파일로 두어야 하며, 파일이 없으면 네이버 검색로봇(Yeti)은 사이트 내 모든 문서를 수집 대상으로 간주한다. 관리자 페이지·개인정보 페이지 같은 경로만 'Disallow: /admin/'처럼 패턴으로 지정하고, 나머지는 허용으로 둔다. 'User-agent: * / Disallow: /'를 쓰면 사이트의 어떤 페이지도 검색에 노출되지 않으므로 홈페이지 제작업체가 넣어둔 기본 설정을 반드시 확인한다. 자바스크립트·CSS·파비콘 경로는 본문과 같은 규칙으로 허용해 두어야 로봇이 페이지를 의도대로 해석한다. 단, 일부 로봇은 robots.txt를 지키지 않으므로 개인정보처럼 외부에 노출되면 안 되는 내용은 robots.txt가 아닌 로그인 등으로 보호해야 한다. 네이버 웹마스터도구의 robots.txt 도구로 간단 생성·검증·수집 요청을 할 수 있다.
