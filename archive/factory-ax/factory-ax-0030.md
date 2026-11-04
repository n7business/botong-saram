---
id: factory-ax-0030
domain: factory-ax
claim: PLC 스텝 컨트롤러(순차 제어 명령)로 단동 솔레노이드 밸브 실린더를 제어할 때 다음 스텝이 켜지면 이전 스텝이 자동으로 리셋되므로,
  출력을 자기유지하거나 다음 스텝 접점을 병렬로 넣지 않으면 실린더가 의도치 않게 복귀한다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=yV0H7jk1hLo
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-03'
  quote: 2번 스텝이 On되면 문법적으로 1번 스텝이 리셋됩니다
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
- 솔레노이드밸브
- 공압실린더
---
순차 제어 명령에서는 문법상 2번 스텝이 켜지면 1번 스텝이 리셋됩니다. 단동 솔 밸브는 전기가 끊기면 스프링으로 돌아가므로, 그대로 두면 B가 전진하는 순간 A도 후진해 버립니다. 막는 방법은 두 가지입니다. SOL1 회로에 다음 스텝 접점을 병렬로 넣거나, 출력 접점으로 자기유지를 거는 것입니다. 스텝이 짧고 간단하면 스텝 접점 병렬이, 스텝이 길면 출력 자기유지가 회로를 더 간단하게 만듭니다. 출력 자기유지를 썼다면 해당 실린더를 복귀시킬 스텝의 b접점으로 자기유지를 끊어야 합니다.
