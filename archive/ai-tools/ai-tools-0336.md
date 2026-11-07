---
id: ai-tools-0336
domain: ai-tools
claim: AI 에이전트 설계서에는 AI가 할 일과 코드 스크립트가 할 일을 나눠 적어야, 번역 같은 판단 작업까지 스크립트로 처리해 품질이 떨어지는
  일을 막을 수 있다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=C6xlOsQFyOQ
  author: 일잘러 장피엠
  seen: '2026-11-07'
  quote: 설계서에서 LLM 에이전트가 할 부분과 코드 스크립트가 할 부분을 나눠 지정해야 한다.
  source: 일잘러 장피엠
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드 코드
- 에이전트 설계
- 스크립트
- 품질
---
에이전트를 세팅하기 전에 설계서에서 단계별 담당을 AI와 스크립트로 나눠 둡니다. 상황 판단이 필요하거나 비정형 결과물을 만드는 일은 AI 몫으로 지정합니다. 정확하고 빠르지만 융통성이 없어도 되는 일은 스크립트에 맡깁니다. 따로 지정하지 않으면 클로드 코드가 번역까지 스크립트로 처리하려 해 품질이 떨어질 수 있습니다.
