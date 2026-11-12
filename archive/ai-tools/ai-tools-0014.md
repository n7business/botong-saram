---
id: ai-tools-0014
domain: ai-tools
claim: Claude Code 세션 도중 모델 변경·MCP 연결/해제·빠른 모드 켜기·compact는 캐시를 새로 쓰게 하므로, 이런 설정은 세션
  시작 때 정하고 모델을 바꿀 땐 /compact를 먼저 돌린다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/3993/
  author: 비벙 (요즘IT)
  seen: '2026-11-03'
  quote: 빠른 모드가 필요한 작업이라면 시작할 때 켜두는 편이 낫습니다.
  source: 요즘IT
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 캐시
- MCP
- compact
- 토큰절약
---
프롬프트 캐시는 요청 앞부분(접두어)이 직전 요청과 일치하는 만큼만 재사용되므로, 작업 중 앞부분이 바뀌면 그 뒤를 전부 다시 써야 한다. 캐시를 새로 쓰게 만드는 행동은 캐시 수명보다 오래 쉬기, 세션 중 처음 빠른 모드 켜기, MCP 서버 연결·해제, 모델 변경, 대화 compact이다(Bedrock·Google Cloud·게이트웨이에서는 추론 강도 변경도 해당). 그러니 세션을 열 때 /mcp로 안 쓰는 서버를 끄고, 빠른 모드가 필요하면 시작부터 켜둔다. 모델을 바꿔야 하면 일이 자연스럽게 끊기는 지점에서 /compact를 먼저 돌린 뒤 바꾼다. 구독·API 키 사용자는 추론 강도(effort)를 바꿔도 캐시가 유지되므로 작업에 맞춰 조절해도 된다.
