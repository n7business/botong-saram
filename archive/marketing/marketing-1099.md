---
id: marketing-1099
domain: marketing
claim: 홈페이지 주소를 옮길 때 이전이 끝나기 전에 옛 사이트에 robots.txt 차단을 걸거나 서버를 먼저 끄면, 네이버 검색로봇이 페이지가
  옮겨졌는지 확인하러 들어가지 못해 새 주소로 제대로 넘어가지 않을 수 있습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-28'
  quote: 이전이 완료될 때까지 구 사이트에 robots.txt를 먼저 설정하거나 서버의 네트워크를 먼저 정지하거나 블럭하지 마세요
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2027-01-27'
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
- robots.txt
verified_by: 공식 출처
---
robots.txt는 검색로봇의 접근을 막는 설정입니다. 문서가 옮겨졌거나 사라졌다는 뜻으로 읽히지 않습니다. 옛 사이트를 먼저 막거나 서버를 내리면 로봇은 301 redirect를 확인할 수 없습니다. 일시적인 오류인지도 판단하지 못합니다. 새 사이트의 주요 페이지가 검색에 반영되고 옛 주소가 더 이상 노출되지 않는 것을 확인한 뒤에 옛 사이트를 막거나 종료하세요. 옛 사이트로 들어오는 사용자가 없을 때 서버를 끄고 웹마스터도구에서 옛 사이트를 삭제합니다.
