---
id: marketing-0764
domain: marketing
claim: 홈페이지를 새 도메인으로 옮길 때는 이전이 끝나기 전에 옛 사이트에 robots.txt 차단을 걸거나 서버를 먼저 끄지 말고, 옛 주소를
  새 주소에 1:1로 301 이동시킨 뒤 주요 페이지가 바뀐 것을 확인하고 나서 닫아야 합니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: '2027-01-13'
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
mentions: 1
---
검색로봇은 옛 사이트를 직접 방문해야 문서가 옮겨졌는지 알 수 있습니다. robots.txt 차단을 먼저 걸거나 서버를 먼저 멈추면 이 확인조차 할 수 없어서 이전이 제대로 반영되지 않습니다. 절차는 다음과 같습니다. 콘텐츠·이미지·파일을 새 사이트로 옮기고, 새 사이트의 robots.txt는 모두 허용합니다. 옛 주소는 페이지마다 1:1로 새 주소에 301 이동시킵니다. 새 사이트의 모든 페이지에 대표 주소(canonical)를 지정하고, 웹마스터도구에 등록해 사이트맵을 제출합니다. 옛 사이트는 유입이 없어진 뒤에 서버를 끄고 웹마스터도구에서도 삭제합니다.
