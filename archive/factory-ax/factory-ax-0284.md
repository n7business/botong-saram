---
id: factory-ax-0284
domain: factory-ax
claim: PLC 전원에 노이즈 필터나 노이즈 컷 트랜스를 쓰는 제어반은 필터를 거치기 전 1차측 선과 거친 뒤 2차측 선을 한 묶음으로 묶거나
  같은 덕트로 지나가게 하면 안 된다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=L2yrwv0uAao
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-23'
  quote: 1차측 선과 필터를 통과한 2차측 선을 함께 묶으면 안 됩니다.
  source: 공학자의 자동화 실무 (@kwh-Astartech)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- PLC
- 제어반
- 노이즈필터
- 전장배선
---
노이즈 필터는 1차측(입력)과 2차측(출력)을 나눠야 제 역할을 합니다. 두 선을 함께 묶거나 같은 덕트로 보내면 1차측의 노이즈가 2차측 선으로 다시 옮겨 갑니다. 그러면 필터를 단 의미가 줄어듭니다. 제어반 배선을 외주로 맡겼다면 필터 앞뒤 선이 따로 지나가는지 덕트 안까지 확인하세요.
