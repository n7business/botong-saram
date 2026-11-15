---
id: marketing-0766
domain: marketing
claim: robots.txt로 막아도 광고·링크 미리보기용 로봇 등은 규칙을 따르지 않을 수 있으므로, 개인정보나 관리자 페이지처럼 외부에 나가면
  안 되는 내용은 robots.txt에만 기대지 말고 로그인 등 다른 방법으로 보호해야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: 외부에 노출되면 안 되는 콘텐츠의 경우 이 설정 외에 로그인 기능 등 다른 방법을 통하여 보호하거나 다른 차단 방법을 사용해야 합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- robots.txt
- 개인정보
- 보안
- 네이버
merged_into: marketing-0627
---
네이버 검색로봇은 robots.txt 규칙을 지킵니다. 하지만 광고주 정보 수집, 링크 미리보기 생성 같은 특수 용도 로봇은 이 규칙을 참조하지 않거나 완벽히 지키지 않을 수 있습니다. 관리자 페이지와 개인정보 페이지는 robots.txt에서 수집 금지로 설정합니다. 그와 별도로 로그인 기능 같은 접근 제한을 반드시 걸어야 합니다. 사이트 전체를 수집 금지로 막으면 어떤 페이지도 검색에 나오지 않으므로, 막을 주소 패턴만 Disallow로 지정합니다.
