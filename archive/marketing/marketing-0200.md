---
id: marketing-0200
domain: marketing
claim: 사이트를 이전할 때 구 사이트에 robots.txt 차단을 먼저 걸거나 서버를 먼저 끄면 검색로봇이 변경 사실을 확인하지 못하므로, 301
  redirect로 이전을 마친 뒤 구 사이트를 종료해야 한다.
status: verified
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
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
- 사이트이전
- 도메인변경
- '301'
verified_by: 공식 출처
---
중소규모 사이트는 모든 URL을 동시에 옮기는 것이 권장됩니다. 신규 사이트의 robots.txt를 모두 허용하고, 구 사이트 URL은 신규 URL로 1:1 대응되게 301 redirect를 설정합니다. 신규 사이트의 모든 페이지에 canonical URL을 지정하고, 웹마스터도구에 등록해 사이트맵을 제출합니다. 구 사이트의 차단 설정은 주요 페이지가 모두 변경되거나 미노출된 것을 확인한 뒤에 하고, 사용자 유입이 없어지면 서버를 종료합니다. 대표 주소를 자주 바꾸면 사이트 품질 평가에 영향을 주므로 이전은 브랜드 변경처럼 꼭 필요할 때만 합니다.
