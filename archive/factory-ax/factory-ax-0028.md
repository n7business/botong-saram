---
id: factory-ax-0028
domain: factory-ax
claim: 운전 중인 설비의 LS일렉트릭 PLC 프로그램을 고칠 때는 XG5000에서 '런 중 수정 시작'으로 고친 뒤 반드시 '런 중 수정 쓰기'를
  실행해야 하며, 그러면 설비를 멈추지 않고 수정 내용을 바로 반영할 수 있다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=aauTtWZRA4E
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-03'
  quote: 런 중 수정 쓰기를 실행을 하셔야 돼요.
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
- LS일렉트릭
- XG5000
- 런에디터
- 설비보전
---
XG5000에서 PLC에 온라인으로 접속한 뒤 PLC 메모리에 있는 현재 프로그램을 먼저 PC로 읽어 옵니다. 손대기 전에 지금 동작이 정상인지 시험해 둡니다. 온라인 메뉴에서 '런 중 수정 시작'을 누르면 화면 바탕색이 바뀌고, 이 상태에서 회로를 고칠 수 있습니다. 예를 들어 실린더 전진 신호로 2초 타이머를 만들고 그 타이머 접점을 복귀 조건에 넣으면 '2초 작업 후 복귀'로 바뀝니다. 수정이 끝나면 반드시 '런 중 수정 쓰기'를 실행해야 합니다. 그래야 바탕색이 원래대로 돌아오고 변경 내용이 운전 중인 설비에 바로 적용됩니다.
