---
id: marketing-0572
domain: marketing
claim: 도메인을 옮길 때는 이전이 끝나기 전에 옛 사이트에 robots.txt로 수집을 막거나 서버를 먼저 끄면 안 되고, 주요 페이지가 모두
  새 주소로 바뀐 것을 확인한 뒤에 막아야 한다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-12'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 사이트이전
- 도메인
- robots.txt
merged_into: marketing-0462
---
robots.txt는 로봇의 접근을 막을 뿐, 문서가 옮겨졌다는 사실을 알려 주지 않습니다. 먼저 막아 버리면 이전 여부를 확인하러 오는 로봇도 들어오지 못합니다. 서버를 먼저 꺼도 로봇은 일시적 오류인지 알 수 없어 이전이 반영되지 않을 수 있습니다. 주소를 자주 바꾸면 사이트 품질 평가에도 영향을 주므로 브랜드 변경처럼 꼭 필요할 때만 옮기세요.
