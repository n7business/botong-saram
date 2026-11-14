---
id: ai-tools-0576
domain: ai-tools
claim: 클로드 코드의 Bash 허용·차단 규칙으로 위험한 명령을 막고 있다면 v2.1.325 이상으로 업데이트해야 하는데, 이전 버전에서는 일부
  복합 명령이 묻지 않고 실행되거나 허용 규칙이 이름과 다른 프로그램을 실행할 수 있는 문제가 있었기 때문이다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-15'
  quote: Fixed a gap in Bash permission checks where some compound commands could
    run without asking; these now ask for permission
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: '2026-12-15'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 보안
- 권한
- 업데이트
- v2.1.325
verified_by: 공식 출처
---
v2.1.325에서 Bash 권한 검사의 빈틈이 여러 개 고쳐졌습니다. 일부 복합 명령이 확인 없이 실행되던 문제, 허용 규칙이 거기 적힌 것과 다른 프로그램을 실행할 수 있던 문제, 일부 차단·확인 규칙이 특정 Bash 명령에 적용되지 않던 문제입니다. '삭제 전에 묻기' 같은 규칙을 권한 설정으로 걸어 두었다면 버전이 낮을 때는 그 규칙이 다 지켜진다고 장담할 수 없습니다. claude --version으로 버전을 확인하고 업데이트하세요.
