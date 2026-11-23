---
id: factory-ax-0289
domain: factory-ax
claim: PLC 전원부 배선을 마치면 구간별 결선을 도면 선 번호와 대조한 뒤 통전해서, 전원 램프 → SMPS DC On 표시 → PLC 전원
  모듈 PWR LED 순으로 켜지고 스위치를 끄면 모두 꺼지는지 확인해야 한다.
status: candidate
evidence: consensus
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=L2yrwv0uAao
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-23'
  quote: 전원 램프, SMPS DC On 표시, PLC 전원 모듈 PWR LED 순으로 불이 들어와야 합니다.
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
- 통전점검
- 시운전
- 제어반
---
통전 전에는 CP 2차측, SMPS 1·2차측, 노이즈 필터 1·2차측, PLC 전원 단자의 선 번호와 접지가 도면대로 물렸는지 하나씩 대조합니다. 그다음 CP와 전원 스위치를 차례로 켜고, 전원 램프, SMPS의 DC On 표시, PLC 전원 모듈의 PWR LED가 순서대로 들어오는지 봅니다. 전원 스위치를 껐을 때 모두 꺼져야 정상입니다. 중간에 불이 들어오지 않으면 바로 앞 구간의 결선부터 다시 확인하세요.
