---
id: ai-tools-0293
domain: ai-tools
claim: AI 코드의 품질 기준은 '깔끔하게 써 줘'라는 지시로 끝내지 말고 린터 규칙으로 만들어 문제가 0개가 될 때까지 고치게 해야, 지시를
  무시하고 넘어가는 일을 줄일 수 있다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=3JCgiVYlLFo
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-07'
  quote: 모델은 마크다운 지시는 무시할 수 있어도 실패한 lint 명령은 무시할 수 없다.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 코딩에이전트
- 린터
- Oxlint
- 품질관리
---
마크다운 지시는 모델이 놓칠 수 있고, 컨텍스트가 커지고 세션이 지저분해질수록 잘 따르지 못합니다. 린터는 AI 없이 코드를 읽어 규칙 위반 줄을 표시하므로 같은 코드에는 항상 같은 지적이 나옵니다. 규칙을 설치한 뒤 에이전트에게 lint를 실행하고, 고치고, 문제가 0개가 될 때까지 다시 돌리게 합니다. JavaScript·TypeScript 프로젝트라면 Oxlint용 규칙 세트인 Anti-Slop을 쓸 수 있습니다. 다만 이 규칙들은 작성자의 취향일 뿐 보편 표준이 아니므로 내 프로젝트에 맞게 바꿔야 합니다.
