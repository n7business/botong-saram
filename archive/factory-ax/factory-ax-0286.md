---
id: factory-ax-0286
domain: factory-ax
claim: 2층 단자를 쓰는 PLC는 접지 단자부터 먼저 배선해야 하며, 접지선은 규정상 녹황색을 쓰고 SMPS·노이즈 필터·PLC의 접지를 각각
  빼서 프레임 접지 단자에 연결해야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=L2yrwv0uAao
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-23'
  quote: 접지선은 규정으로 녹황색을 쓰셔야죠.
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
- 접지
- 제어반
- 전장배선
---
공간을 줄이려고 단자를 2층으로 배치한 PLC는 다른 선을 먼저 물리면 아래쪽 접지 단자에 손이 닿지 않습니다. 그래서 접지 단자를 먼저 작업합니다. 접지선은 규정에 따라 녹황색을 쓰고, SMPS·노이즈 필터·PLC의 접지 단자에서 각각 선을 빼 프레임 접지 단자에 연결합니다. 배선 전에는 제조사가 제공하는 단자대 배치도로 기기마다 접지 단자 위치를 먼저 확인하세요.
