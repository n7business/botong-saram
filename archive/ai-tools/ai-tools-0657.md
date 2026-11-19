---
id: ai-tools-0657
domain: ai-tools
claim: AI 코딩 도구에 그림·화면·애니메이션 작업을 맡길 때는 코드만 쓰고 끝내게 하지 말고, 결과를 직접 렌더링하거나 브라우저로 띄워 확인하며
  고치게 해야 한다.
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=VJDXrpCpyv0
  author: 코드깎는노인
  seen: '2026-11-20'
  quote: 6개 모두 모델이 자기 결과물을 직접 그려 보거나 검사하면서 고쳤다
  source: 코드깎는노인
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 코딩에이전트
- 검증
- Codex
- 렌더링
---
화자는 Codex에서 펠리컨 그림을 아스키아트, SVG, 캔버스, CSS, Three.js, 셰이더 6가지 방법으로 그리게 했다. 6개 모두 모델이 결과물을 직접 그려 보거나 검사하면서 고쳤다. SVG에서는 렌더링한 그림을 보고 체인 덮개에 가려진 발을 찾아 페달 위치를 고쳤다. 이전 모델이 한 번에 써낼 때 못 했던 다리 배치였다. Three.js에서는 부두 받침이 화면 아래에서 잘리는 것을 찾아 구도를 고쳤다. 작업을 맡길 때 '다 만든 뒤 화면으로 확인하고 고쳐라'를 지시나 규칙 파일에 넣어 두면 좋다.
