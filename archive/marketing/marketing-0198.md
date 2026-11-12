---
id: marketing-0198
domain: marketing
claim: 개인정보처럼 외부에 노출되면 안 되는 페이지는 일부 로봇이 robots.txt를 완벽히 따르지 않을 수 있으므로, robots.txt
  설정만 믿지 말고 로그인 기능 등으로 함께 보호해야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: 이 설정 외에 로그인 기능 등 다른 방법을 통하여 보호하거나 다른 차단 방법을 사용해야 합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2027-01-04'
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
- 보안
verified_by: 공식 출처
---
관리자 페이지와 개인정보 페이지는 robots.txt에서 수집 비허용으로 설정합니다. 다만 광고주 정보 취득이나 링크 미리보기 생성 같은 특수 용도의 로봇은 이 규칙을 참조하지 않거나 완벽하게 준수하지 않을 수 있습니다. 그래서 이런 페이지는 로그인 기능 등 다른 방법으로도 보호해야 합니다. 사이트 전체를 Disallow로 막으면 어떤 페이지도 검색에 노출되지 않으므로, 수집 대상이 아닌 URL 패턴만 지정합니다.
