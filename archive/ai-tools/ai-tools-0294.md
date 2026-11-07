---
id: ai-tools-0294
domain: ai-tools
claim: AI의 답변이 길어 계획을 끝까지 읽기 어렵다면 답변 방식을 정하는 스타일 파일을 적용해 짧게 받아야, 불필요한 코드가 만들어지기 전
  계획 단계에서 잡기 쉽다.
status: verified
evidence: observed
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=3JCgiVYlLFo
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-07'
  quote: 적용 전에는 400단어 이상, 적용 후에는 94단어로 같은 정보가 나왔다.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 코딩에이전트
- 출력스타일
- 계획
- AttentionSpan
verified_by: 실무자 실측(단일 출처)
---
Attention Span은 에이전트의 답변 방식을 정하는 마크다운 파일 모음입니다. 클로드 코드에서는 output style로 설치하고, Codex나 OpenCode에서는 AGENTS.md에서 스타일 파일을 링크합니다. 영상의 예시에서는 데이터베이스 선택 질문의 답이 적용 전 400단어 이상에서 적용 후 94단어로 줄었고, 화자는 같은 정보가 나왔다고 평가했습니다. 화자는 구현 계획을 지치지 않고 끝까지 읽을 수 있게 된 점이 중요하다고 말합니다. 이 수치는 질문 하나의 사례이므로 내 작업에서 빠진 정보가 없는지 직접 확인해야 합니다.
