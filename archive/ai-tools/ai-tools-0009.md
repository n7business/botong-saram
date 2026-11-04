---
id: ai-tools-0009
domain: ai-tools
claim: CLAUDE.md는 200줄 이내로 유지하고, 가끔만 필요한 참고 자료는 스킬이나 .claude/rules/ 파일로 분리한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/features-overview
  author: Anthropic (Claude Code Docs)
  seen: '2026-11-03'
  quote: 'Rule of thumb: Keep CLAUDE.md under 200 lines.'
  source: Claude Code 공식 문서
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- 컨텍스트
- 스킬
---
CLAUDE.md는 매 세션 자동으로 로드되므로 길어질수록 컨텍스트를 계속 잡아먹는다. 공식 권장 기준은 200줄 이내다. 빌드 명령·코딩 규칙·'절대 하지 말 것' 같은 항상 필요한 내용만 남기고, API 문서나 배포 체크리스트처럼 가끔 쓰는 내용은 스킬로 옮긴다. 언어별·디렉터리별 지침은 `.claude/rules/`에 paths 지정으로 두면 해당 파일을 다룰 때만 로드되어 컨텍스트를 아낀다.
