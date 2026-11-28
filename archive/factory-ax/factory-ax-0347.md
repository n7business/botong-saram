---
id: factory-ax-0347
domain: factory-ax
claim: 비전 AI 위험 감지 결과로 경보를 울리는 사업자는 탐지 즉시 경보가 나가게 하지 말고 2차 검증을 거치게 해야 오경보를 줄일 수 있다.
  한 실증에서는 30일 동안 탐지한 위험 이벤트 4,967건 가운데 462건이 VLM 재검증에서 오경보로 걸러졌다.
status: candidate
evidence: observed
confidence: 0.65
sources:
- url: https://www.kidd.co.kr/news/248297
  author: 이도엽 콘티랩 기술연구소장(산업일보 임지원 기자)
  seen: '2026-11-28'
  quote: 곧바로 경보를 발생시키지 않고 VLM으로 재검증하는 방식으로 실증했다
  source: 산업일보
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 비전AI
- 오탐
- 경보
- 재검증
- 안전관제
---
VLM은 위험 상황을 놓치지 않고 찾아내는 비율(재현율)은 높지만, 위험하지 않은 상황까지 위험으로 판정하는 경우가 많다. 원거리 촬영처럼 화질이 떨어지는 조건에서도 오탐이 생긴다. 오경보가 잦으면 작업자와 관리자가 경보를 믿지 않게 되므로, 1차 탐지 뒤 바로 경보를 울리지 말고 VLM 등으로 한 번 더 확인하는 단계를 넣는다. 콘티랩이 건설현장 6곳의 CCTV 9대로 30일간 실증했을 때, 탐지한 4,967건 가운데 462건(약 9%)이 2차 검증에서 오경보로 빠졌다. 다만 이 수치는 공급사 한 곳이 발표한 실증 결과다.
