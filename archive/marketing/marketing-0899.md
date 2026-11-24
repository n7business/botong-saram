---
id: marketing-0899
domain: marketing
claim: robots.txt로 수집을 막아도 광고·링크 미리보기용 로봇 등은 규칙을 따르지 않을 수 있으므로, 개인정보나 외부에 나가면 안 되는
  내용은 robots.txt에만 기대지 말고 로그인 등 다른 방법으로 보호해야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: 네이버 서치어드바이저
  seen: '2026-11-21'
  quote: 개인 정보를 포함하여 외부에 노출되면 안 되는 콘텐츠의 경우 이 설정 외에 로그인 기능 등 다른 방법을 통하여 보호하거나
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
- robots.txt
- 개인정보
- 홈페이지보안
- 네이버SEO
verified_by: 공식 출처
merged_into: marketing-1002
---
관리자 페이지나 개인정보 페이지는 robots.txt에서 Disallow로 수집을 막아 두는 것이 기본입니다. 하지만 웹마스터와 따로 수집 조건을 협약한 경우나 광고주 정보 취득, 링크 미리보기 생성 같은 특수 용도의 로봇은 robots.txt 규칙을 참조하지 않거나 완벽하게 지키지 않을 수 있습니다. 고객 서류·신청서처럼 노출되면 안 되는 자료는 로그인을 거쳐야만 볼 수 있게 하거나 다른 차단 방법을 함께 써야 합니다. 사이트 전체를 Disallow로 막으면 어떤 페이지도 검색에 나오지 않으므로, 막을 URL 패턴만 지정하세요.
