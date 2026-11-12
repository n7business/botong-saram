---
id: factory-ax-0091
domain: factory-ax
claim: PLC 카운터로 동작 횟수를 세어 자동 정지시키는 회로에는 초기화(리셋) 명령을 넣어야 하며, 그래야 카운트업 뒤 다음 사이클을 돌릴
  수 있다.
status: candidate
evidence: consensus
confidence: 0.85
sources:
- url: https://www.youtube.com/watch?v=suj-Sy6rdY0
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-07'
  quote: 다음 사이클을 하려면 카운터에 초기화(리셋) 명령이 반드시 들어가야 한다.
  source: 공학자의 자동화 실무 (@kwh-Astartech)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- PLC
- 카운터
- 자동정지
- 리셋
---
가산 카운터에 목표값(예: 5회)을 설정하고 솔레노이드가 작동할 때마다 세도록 구성한다. 카운트업되면 카운터 b접점이 열려 설비가 정지한다. 다음 사이클을 하려면 카운터에 초기화(리셋) 명령이 반드시 들어가야 한다. 동작 횟수는 모니터 화면에서 확인할 수 있다.
