---
id: ai-tools-0141
domain: ai-tools
claim: AI로 만든 웹페이지의 움직임은 버튼 같은 작은 반응은 0.1~0.2초, 화면에 큰 요소가 들어올 때는 0.3~0.5초로 지정하면 무난하다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=r7iS0Gw3Jq4
  author: 코드깎는노인
  seen: '2026-11-03'
  quote: 버튼 같은 작은 반응은 0.1~0.2초, 화면에 큰 요소가 들어올 때는 0.3~0.5초가 무난합니다.
  source: 코드깎는노인
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- 애니메이션
- UX
---
움직이는 데 걸리는 시간(듀레이션)과 움직이기 전 기다리는 시간(딜레이)을 숫자로 지정해야 AI가 임의로 정하지 않습니다. 버튼 반응은 0.1~0.2초, 모달·카드처럼 큰 요소의 등장은 0.3~0.5초가 기본값으로 쓸 만합니다. 화면에 들어오고 나가는 요소는 이즈인아웃(또는 등장 시 이즈아웃)을 함께 지정하면 대부분 자연스럽습니다. 여러 요소는 딜레이를 차례로 조금씩 주는 스태거로 순서를 만듭니다.
