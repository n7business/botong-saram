---
id: ai-tools-0710
domain: ai-tools
claim: 코덱스 같은 다른 AI 코딩 도구용으로 AGENTS.md를 이미 만들어 두었다면 CLAUDE.md를 따로 새로 쓰지 말고 클로드 코드가
  AGENTS.md를 읽게 해서 규칙 파일을 하나로 관리하면 된다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-23'
  quote: Claude Code can read that in place of a CLAUDE.md
  source: Claude Code 공식 문서
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- CLAUDE.md
- AGENTS.md
- 코덱스
- 규칙파일
verified_by: 공식 출처
---
CLAUDE.md는 클로드 코드가 세션을 시작할 때마다 읽는 규칙 파일입니다. 작업 기준, 구조 결정, 검토 체크리스트 같은 내용을 여기에 적어 둡니다. 공식 문서에 따르면 저장소에 다른 코딩 에이전트용 AGENTS.md가 있으면 클로드 코드가 CLAUDE.md 대신 그 파일을 읽을 수 있습니다. 두 도구를 함께 쓸 때 규칙 파일을 두 벌로 관리하면 한쪽만 고쳐져 내용이 어긋나기 쉽습니다. 구체적인 설정 방법은 공식 memory 문서의 AGENTS.md 항목에서 확인하세요.
