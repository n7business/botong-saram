---
id: marketing-0027
domain: marketing
claim: 홈페이지를 새 도메인으로 옮길 때는 주요 페이지가 새 주소로 검색에 반영된 것을 확인하기 전까지 옛 사이트의 robots.txt 차단이나
  서버 정지를 하지 말아야 하며, 먼저 막으면 로봇이 이전 사실 자체를 확인하지 못한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-03'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
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
- 사이트이전
- 도메인변경
- robots.txt
verified_by: 공식 출처
---
사이트 이전 순서는 콘텐츠(이미지·파일 포함) 이동 → 새 도메인 할당(로봇 인식에 2~3일) → 새 사이트 robots.txt 전체 허용 + 옛 URL에서 새 URL로 1:1 301 redirect → 새 사이트 전 페이지에 canonical 지정 → 서치어드바이저에 새 사이트 등록·사이트맵 제출 → 옛 사이트 종료다. robots.txt는 '문서가 옮겨졌다'는 뜻이 아니라 접근 차단이므로 옛 사이트에 먼저 걸면 로봇이 redirect를 확인하러 들어올 수조차 없다. 서버를 네트워크 단에서 먼저 끊어도 로봇은 일시 오류인지 폐쇄인지 구분하지 못한다. 중소규모 사이트는 카테고리별이 아니라 모든 URL을 한 번에 옮기는 것을 권장하며, 도메인을 자주 바꾸면 품질 평가가 매번 초기화되므로 브랜드 변경 같은 꼭 필요한 때만 한다.
