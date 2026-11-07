---
id: ai-tools-0287
domain: ai-tools
claim: 저장소에 다른 코딩 에이전트용 AGENTS.md가 이미 있다면 클로드 코드가 이를 CLAUDE.md 대신 읽을 수 있으므로, 지시문을
  처음부터 따로 만들지 않아도 된다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: If your repository already has an `AGENTS.md` for other coding agents
  source: Claude Code 공식 문서
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- claude-md
- agents-md
- 지시문
verified_by: 공식 출처
---
CLAUDE.md는 프로젝트 루트에 두는 마크다운 파일로, 클로드 코드가 세션을 시작할 때마다 읽습니다. 다른 코딩 에이전트용 AGENTS.md가 저장소에 이미 있으면 클로드 코드는 이를 CLAUDE.md 대신 읽을 수 있습니다. 코딩 표준, 아키텍처 결정, 선호 라이브러리, 리뷰 체크리스트를 여기에 적어 둡니다. 설정 방법은 메모리 문서의 AGENTS.md 항목에서 확인합니다.
