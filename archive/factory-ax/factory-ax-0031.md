---
id: factory-ax-0031
domain: factory-ax
claim: PLC 스텝 컨트롤러 회로는 스텝 번호를 반드시 1번부터 시작하고, 마지막 스텝 뒤에 0번 스텝으로 전체를 리셋해야 다음 사이클을 돌릴
  수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=yV0H7jk1hLo
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-03'
  quote: 스텝 번호는 반드시 1번으로 시작을 해야 된다고 그랬습니다
  source: 공학자의 자동화 실무 (@kwh-Astartech)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- PLC
- 순차제어
- 스텝컨트롤러
- 리셋회로
---
조 번호는 아무 번호나 써도 되지만, 같은 조 안에서 스텝 번호는 반드시 1번부터 시작해 하나씩 올라가야 합니다. 조를 중간에 바꾸면 안 됩니다. 마지막 스텝이 켜진 채로 남으면 다음 사이클이 시작되지 않습니다. 그래서 원위치 센서 신호(예: LS1·LS3)와 마지막 스텝 신호를 AND로 묶어 0번 스텝을 세트하는 리셋 회로를 넣어야 합니다. 0번 스텝이 켜지면 모든 스텝이 리셋되어 연속 운전이 가능해집니다.
