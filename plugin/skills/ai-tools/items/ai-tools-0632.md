# 클로드 코드의 /code-review는 v2.1.328부터 버그와 CLAUDE.md 규칙 위반만 알려 주므로, 중복 코드 정리나 단순화·효율 개선까지 점검받으려면 /simplify를 따로 실행해야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

v2.1.328부터 대부분의 모델에서 /code-review는 버그와 CLAUDE.md 위반만 보고합니다. 지적 사항마다 중요(Important)·기존 문제(Pre-existing)·사소함(Nit)도 함께 표시합니다. 재사용·단순화·효율 같은 정리 항목은 /simplify의 몫으로 나뉘었습니다. 또 이전 버전에서는 /code-review <PR 번호>가 아무 말 없이 PR 대신 현재 브랜치를 검토하는 경우가 있었는데, v2.1.329에서 고쳐졌습니다. PR 검토에 이 기능을 쓴다면 업데이트한 뒤 쓰세요.

- 근거 policy · 처음 2026-11-20 · 최근 확인 2026-11-20 · 재검토 2026-12-20 · 검증 공식 출처

## 출처
- Anthropic (anthropics/claude-code) · 2026-11-20 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > run `/simplify` for reuse, simplification and efficiency cleanups
- Anthropic (anthropics/claude-code) · 2026-11-20 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > reviewing the checked-out branch instead of the pull request without saying so
