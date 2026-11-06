---
id: factory-ax-0059
domain: factory-ax
claim: 인버터 트립 신호 단자를 운전 지령 릴레이 코일과 연결해 두면 전동기 운전 중 과전류 트립이 났을 때 지령 신호가 자동으로 끊긴다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=xjcQp1lpU7A
  author: 공학자의 자동화 실무 (@kwh-Astartech)
  seen: '2026-11-06'
  quote: 전동기 운전 중 과전류 트립이 나면 지령 신호가 자동으로 끊기도록 릴레이 코일과 연결한다.
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
- 인버터
- 트립
- 과전류
- 릴레이
- 배선
---
운전 지령은 공통 단자 CM에서 릴레이 a접점을 거쳐 P1 단자로 연결합니다. 트립 단자(A·B·C접점)는 인버터 내부 과전류 보호기가 동작했을 때 신호를 내므로, 이 신호를 릴레이 코일 회로에 물립니다. 영상의 기종에서는 3B에 04번선을 물려 릴레이 코일 쪽으로, 3C에 단자대의 T220을 연결했습니다. 단자 이름은 제조사마다 조금씩 다르므로 메이커 결선도를 확인한 뒤 배선합니다.
