---
id: marketing-0493
domain: marketing
claim: 홈페이지 주소를 바꾸며 이동(redirect)을 여러 번 이어 걸 때는 5회를 넘기지 말고, 거쳐 가는 주소와 최종 주소가 모두 수집
  가능한 정상 페이지인지 확인해야 한다.
status: verified
evidence: policy
confidence: 0.87
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-10'
  quote: 연속해서 연결되는 리다이렉션 횟수는 최대 5회 이상을 넘기지 않는 것을 추천합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2027-01-09'
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
---
주소를 여러 번 개편하면서 A→B→C처럼 이동이 꼬리를 물면, 횟수가 검색로봇의 허용 범위를 넘어 수집되지 않을 수 있습니다. 네이버는 연속 이동을 최대 5회 안으로 줄이라고 권장합니다. 자기 자신으로 끝없이 이동하는 오류도 수집되지 않습니다. 처음과 마지막 주소가 정상이어도 중간 주소 하나가 robots.txt로 막혀 있으면 수집이 안 될 수 있습니다. 이동 경로는 눈으로 확인하기 어려우니 브라우저 개발자 도구를 쓰거나 제작업체와 함께 점검하세요.
