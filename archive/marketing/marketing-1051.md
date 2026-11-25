---
id: marketing-1051
domain: marketing
claim: 주소 이동(redirect)을 여러 번 연달아 걸지 말고 5회를 넘기지 않아야 하며, 이동 중간의 주소와 최종 도착 주소가 모두 수집
  가능한 정상 페이지여야 합니다. 그렇지 않으면 네이버가 그 페이지를 수집하지 못할 수 있습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-25'
  quote: 연속해서 연결되는 리다이렉션 횟수는 최대 5회 이상을 넘기지 않는 것을 추천합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: '2027-01-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- redirect
- 사이트개편
verified_by: 공식 출처
---
이동이 연달아 일어나는 횟수가 검색로봇에 설정된 범위를 넘거나 자기 자신으로 끝없이 이동하면 네이버는 그 페이지를 수집하지 않습니다. 처음 주소와 최종 주소가 수집 가능해도 중간 주소 하나가 robots.txt로 막혀 있으면 수집되지 않을 수 있습니다. 사이트를 개편한 뒤에는 바뀌기 전 주소와 바뀐 주소가 제대로 연결되는지 브라우저 개발자 도구로 확인하세요. 반영에 시간이 걸릴 수 있으니 기존에 검색되던 주소에도 한동안 redirect를 유지하는 편이 좋습니다.
