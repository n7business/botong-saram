---
id: ai-tools-0632
domain: ai-tools
claim: 클로드 코드의 /code-review는 v2.1.328부터 버그와 CLAUDE.md 규칙 위반만 알려 주므로, 중복 코드 정리나 단순화·효율
  개선까지 점검받으려면 /simplify를 따로 실행해야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: run `/simplify` for reuse, simplification and efficiency cleanups
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: reviewing the checked-out branch instead of the pull request without saying
    so
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 코드리뷰
- 검증
- v2.1.328
- v2.1.329
verified_by: 공식 출처
---
v2.1.328부터 대부분의 모델에서 /code-review는 버그와 CLAUDE.md 위반만 보고합니다. 지적 사항마다 중요(Important)·기존 문제(Pre-existing)·사소함(Nit)도 함께 표시합니다. 재사용·단순화·효율 같은 정리 항목은 /simplify의 몫으로 나뉘었습니다. 또 이전 버전에서는 /code-review <PR 번호>가 아무 말 없이 PR 대신 현재 브랜치를 검토하는 경우가 있었는데, v2.1.329에서 고쳐졌습니다. PR 검토에 이 기능을 쓴다면 업데이트한 뒤 쓰세요.
