---
id: marketing-0965
domain: marketing
claim: 'robots.txt 전체를 ''Disallow: /''로 막으면 사이트의 어떤 페이지도 네이버 검색에 나오지 않으므로, 관리자·개인정보
  페이지처럼 수집하면 안 되는 경로만 골라서 막아야 합니다.'
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-create
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-23'
  quote: 수집 대상이 아닌 URL 패턴만 Disallow로 지정하는 것을 권장합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2027-01-22'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- robots.txt
- 사이트맵
verified_by: 공식 출처
---
네이버는 모든 페이지를 수집 금지로 설정하는 방식을 권장하지 않습니다. 대신 'User-agent: Yeti / Disallow: /private*/'처럼 수집 대상이 아닌 URL 패턴만 지정하라고 안내합니다. robots.txt 파일이 없으면 모든 문서를 수집 대상으로 보지만, 파일을 만들어 막을 곳을 정확히 적어 두는 것이 권장됩니다. robots.txt에 'Sitemap:' 줄로 사이트맵 위치를 적어 두면 수집에도 도움이 됩니다.
