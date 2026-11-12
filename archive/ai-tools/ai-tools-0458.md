---
id: ai-tools-0458
domain: ai-tools
claim: 다른 AI 코딩 도구용 AGENTS.md가 이미 있는 프로젝트라면 같은 내용으로 CLAUDE.md를 따로 만들지 않아도 되는데, 클로드
  코드가 CLAUDE.md 대신 AGENTS.md를 읽을 수 있기 때문이다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: Claude Code can read that in place of a CLAUDE.md
  source: Claude Code 공식 문서
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- CLAUDE.md
- AGENTS.md
- 지침파일
verified_by: 공식 출처
---
CLAUDE.md는 클로드 코드가 세션을 시작할 때마다 읽는 지침 파일입니다. 프로젝트에 다른 코딩 에이전트용 AGENTS.md가 이미 있으면 클로드 코드가 그 파일을 대신 읽을 수 있습니다. 지침 파일을 두 벌로 관리하면 한쪽만 고쳐져 내용이 어긋나기 쉬우므로, 여러 AI 도구를 함께 쓴다면 한 파일로 관리하는 편이 낫습니다. 이 경우에도 지침은 꼭 필요한 내용만 짧게 유지하세요.
