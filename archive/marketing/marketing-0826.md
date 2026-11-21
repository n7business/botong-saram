---
id: marketing-0826
domain: marketing
claim: 주소가 여러 번 이어서 넘어가는 연속 redirect는 5회를 넘지 않게 최소화해야 하며, 중간 주소나 최종 도착 주소 중 하나라도 robots.txt로
  막혀 있거나 없는 페이지면 네이버가 수집하지 못합니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: 네이버 서치어드바이저
  seen: '2026-11-19'
  quote: 연속해서 연결되는 리다이렉션 횟수는 최대 5회 이상을 넘기지 않는 것을 추천합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2027-01-18'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- redirect
- 사이트개편
verified_by: 공식 출처
mentions: 1
---
사이트 개편을 거듭하며 A→B→C처럼 주소가 연달아 넘어가게 되면, 그 횟수가 검색로봇이 허용하는 범위를 넘어 수집되지 않을 수 있습니다. 연속 redirect는 5회를 넘기지 않게 하고, 가능하면 옛 주소에서 최종 주소로 바로 넘어가게 정리하세요. 자기 자신으로 계속 되돌아오는 무한 redirect도 수집되지 않습니다. 처음과 마지막 주소가 정상이어도 중간 주소 하나가 robots.txt로 막혀 있으면 수집이 안 될 수 있습니다. 이런 문제는 브라우저 화면만으로는 알기 어려우니, 개발자 도구로 확인하거나 제작업체에 점검을 요청하세요.
