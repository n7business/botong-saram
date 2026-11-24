---
id: marketing-0999
domain: marketing
claim: 서버 부담 때문에 네이버 검색로봇을 잠시 막아야 한다면 robots.txt로 차단하지 말고 웹마스터도구 수집 설정에서 트래픽 제한량을
  최소로 지정해야 하며, robots.txt로 막으면 그 기간에 이미 수집된 문서가 네이버 검색에서 빠질 수 있습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp.
  seen: '2026-11-24'
  quote: robots.txt로 검색로봇을 차단하는 방법도 있지만 이 경우 해당 기간 동안에 수집된 사이트 내의 문서는 네이버 검색에서 제외될
    수 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2027-01-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- 웹마스터도구
- robots.txt
- 트래픽제한
verified_by: 공식 출처
mentions: 1
---
이벤트로 접속이 몰리거나 서버 성능이 부족해 네이버 검색로봇의 방문을 잠시 줄여야 할 때가 있습니다. 이때는 네이버 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 낮춥니다. robots.txt로 막아도 방문은 줄지만, 막아 둔 기간에 이미 검색에 나오던 문서가 빠질 수 있습니다. 잠깐 막을 생각이라면 robots.txt를 건드리지 않는 편이 안전합니다.
