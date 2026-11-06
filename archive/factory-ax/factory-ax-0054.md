---
id: factory-ax-0054
domain: factory-ax
claim: 실린더 순서 제어 회로를 PLC로 짤 때 순차 제어 명령(스텝 컨트롤러)을 쓰면 자기유지와 인터록이 명령에 들어 있어, 작동 중 센서가
  오동작해도 시퀀스가 어긋나지 않는다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=IOxNGcPgOQw
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-06'
  quote: 작동 중에 센서가 오동작을 해도 시퀀스가 어긋나지 않는다.
  source: 공학자의 자동화 실무 (@kwh-Astartech)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
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
- 인터록
- LS일렉트릭
---
PLC 제조사가 액추에이터 순서 제어를 쉽게 하도록 만든 명령으로, 커맨드와 세트 명령을 '조 번호.스텝 번호'로 지정해 씁니다. 자기유지, 보증의 인터록, 보호의 인터록 기능이 들어 있습니다. 입력이 Off가 돼도 출력은 유지되고, 다음 스텝은 전 단계가 동작했다는 신호가 On일 때만 On이 됩니다. 영상의 LS일렉트릭 PLC 기준으로 조 번호는 0~127번, 스텝 번호는 0~99번까지 쓸 수 있습니다. 같은 설비의 스텝에서는 조 번호를 바꾸면 안 됩니다.
