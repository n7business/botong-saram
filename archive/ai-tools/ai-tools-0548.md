---
id: ai-tools-0548
domain: ai-tools
claim: 직원들이 실험 기능인 클로드 코드 Code Mode를 쓰지 않게 하려면 관리 설정(managed settings)에 CLAUDE_CODE_EXPERIMENTAL_CODE_MODE
  값을 0으로 넣어야 하고, 내려받은 저장소의 프로젝트 설정으로는 이 기능이 켜지지 않는다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/code-mode
  author: Anthropic
  seen: '2026-11-14'
  quote: You can't turn on Code Mode for your users from managed settings.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2026-12-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- code-mode
- 관리설정
- 조직관리
verified_by: 공식 출처
---
Code Mode는 환경 변수 CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1로 켭니다. 회사 전체에서 막으려면 관리 설정의 env 항목에 이 변수를 "0"으로 넣으면 됩니다. 이미 Code Mode로 작업 중인 직원은 종료하거나 재시작할 때까지 그대로 쓰고, 그 뒤에는 Code Mode 없이 시작하며 이전 Code Mode 세션도 다시 열 수 없습니다. 반대로 관리 설정으로 직원 모두에게 켜 줄 수는 없습니다. 클로드 코드는 프로젝트 설정 파일에 들어 있는 이 변수를 무시하므로, 남이 만든 저장소를 내려받아도 그 저장소가 Code Mode를 몰래 켜지는 못합니다.
