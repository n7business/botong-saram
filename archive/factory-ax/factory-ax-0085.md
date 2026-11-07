---
id: factory-ax-0085
domain: factory-ax
claim: 공압 실린더를 고를 때는 이론 출력을 그대로 믿지 말고 부하율 70%를 적용한 출력으로 계산해야 기계에 쓸 수 있는 여유를 확보할 수
  있다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=O8Ytnbdeoig
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-07'
  quote: 이 부하율은 통상 70%를 적용을 합니다.
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
- 공압
- 실린더
- 출력계산
- 부하율
---
실린더 이론 출력은 F = A × P로 구하며, A는 피스톤의 수압 면적이고 P는 작용 압력이다. 후진 때는 피스톤 면적에서 로드 면적을 빼고 계산하므로 후진 출력이 전진 출력보다 작다. 에너지 변환 손실이 있어 실제 출력은 추력 보정 계수(소형 0.8, 중형 0.85, 대형 0.9)를 곱해 구하며, 이론 출력의 약 80%로 보면 된다. 기계에 적용할 때는 여유를 줘야 하므로 통상 부하율 70%를 적용해 이론 출력에 약 0.7을 곱한 값을 쓴다.
