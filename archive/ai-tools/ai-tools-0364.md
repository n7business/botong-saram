---
id: ai-tools-0364
domain: ai-tools
claim: 매 세션 자동으로 불러오는 CLAUDE.md와 메모는 파일당 200줄 이하의 짧은 색인으로 유지하고 세부 규칙은 하위 파일로 내려 링크만
  남겨야, 토큰 낭비와 지시 불이행을 줄일 수 있다.
status: verified
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=G1JxVbTmCEc
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: Anthropic 공식 문서는 CLAUDE.md 파일당 200줄 이하를 권장하지만
  source: 짐코딩 (@gymcoding)
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: longer instruction files reduce adherence
  source: Anthropic Engineering 블로그
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- 메모리
mentions: 2
verified_by: 독립 2곳 weight 1.7
---
영상에 따르면 Anthropic 공식 문서는 CLAUDE.md 파일당 200줄 이하를 권장합니다. 영상 제작자는 프로젝트가 클수록 더 짧게, 예를 들어 70줄 이내가 좋다고 합니다. 70줄은 공식 기준이 아니라 제작자의 권장치입니다. GitHub 스타 29,000개가 넘고 여러 기술이 한 저장소에 모인 CopilotKit의 루트 CLAUDE.md는 약 30줄입니다.
