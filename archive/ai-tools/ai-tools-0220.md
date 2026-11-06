---
id: ai-tools-0220
domain: ai-tools
claim: 회의를 녹음해 전사·요약본을 쌓는 자동화를 만들어 두면 회의록 작성에 바로 쓸 수 있고 나중에 AI 에이전트에게 줄 양질의 컨텍스트도
  확보된다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=wf-Xf1Ushq4
  author: 일잘러 장피엠
  seen: '2026-11-06'
  quote: 회의록 자동화 정도는 그냥 한 번 정도 시도해 보자.
  source: 일잘러 장피엠
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- n8n
- 회의록
- STT
- 노션
- 컨텍스트
---
회의를 녹음한 음성 파일을 올리면 STT로 텍스트로 바꾸고 원본을 구글 드라이브에 올립니다. 이어 문법 교정, 회의 요약, 하이라이트·세 줄 요약을 프롬프트로 처리해 노션에 올리며, 담당자가 있으면 액션 아이템까지 정리합니다. 아이폰 단축어 매크로를 쓰면 녹음 직후 워크플로로 바로 보낼 수 있습니다. 많은 사람이 에이전트에 어떤 컨텍스트를 줘야 할지 몰라 막히는데, 쌓아 둔 회의록은 그 자체로 쓸모 있고 AX를 할 때도 도움이 된다고 합니다. 화자는 소개한 사례 중 이것만큼은 꼭 한 번 시도해 보라고 권합니다.
