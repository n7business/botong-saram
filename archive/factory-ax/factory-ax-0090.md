---
id: factory-ax-0090
domain: factory-ax
claim: PLC에서 세트 코일로 자기유지를 걸면 접점을 끊어도 풀리지 않으므로 해제 조건에 반드시 리셋 명령을 넣어야 한다.
status: candidate
evidence: consensus
confidence: 0.85
sources:
- url: https://www.youtube.com/watch?v=suj-Sy6rdY0
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-07'
  quote: 반드시 리셋 명령을 줘야 됩니다.
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
- 자기유지
- 세트리셋
- LS일렉트릭
---
자기유지 회로가 많이 쓰이기 때문에 모든 PLC에는 동작 유지(세트) 명령과 해제(리셋) 명령이 내장되어 있으며, LS일렉트릭에서는 세트 코일·리셋 코일이라 부른다. 세트 코일을 쓰면 입력 신호와 병렬로 연결하지 않아도 자기유지가 걸린다. 다만 접점을 끊는 것으로는 풀리지 않는다. 그래서 회로를 짤 때 반드시 리셋 명령을 함께 넣어야 한다.
