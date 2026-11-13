---
id: marketing-0627
domain: marketing
claim: robots.txt로 사이트 전체를 막으면 어떤 페이지도 네이버 검색에 나오지 않으므로 관리자·개인정보 페이지만 Disallow로 막아야
  하며, robots.txt를 지키지 않는 로봇도 있으므로 개인정보가 담긴 페이지는 로그인 등으로 따로 보호해야 한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-13'
  quote: 개인 정보를 포함하여 외부에 노출되면 안 되는 콘텐츠의 경우 이 설정 외에 로그인 기능 등 다른 방법을 통하여 보호하거나
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2027-01-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
- 개인정보
- 수집차단
verified_by: 공식 출처
---
robots.txt는 사이트 루트(예: www.example.com/robots.txt)에 일반 텍스트 파일로 두어야 합니다. 「User-agent: * / Disallow: /」처럼 전체를 막으면 사이트의 어떤 페이지도 검색에 나오지 않으므로, 수집하면 안 되는 주소 패턴만 Disallow로 지정하세요. 다만 광고 정보 수집이나 링크 미리보기용 로봇처럼 robots.txt 규칙을 완벽하게 지키지 않는 로봇도 있습니다. 그래서 고객 개인정보처럼 밖에 나가면 안 되는 내용은 robots.txt에만 기대지 말고 로그인 기능 같은 다른 방법으로 막아야 합니다.
