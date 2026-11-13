# 클로드 코드에서 Read(./.env)처럼 상대 경로로 적은 읽기 금지·확인 규칙에 기대고 있다면 v2.1.325 이상으로 업데이트해야 하는데, 이전 버전에서는 작업 중 폴더를 옮기면(cd) 이 규칙이 프로젝트에 더 이상 적용되지 않는 문제가 있었기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

권한 설정의 deny·ask 규칙은 AI가 인증 파일 같은 민감한 파일을 읽지 못하게 막는 실제 장치입니다. 그런데 v2.1.325 릴리스 노트를 보면, 그 전에는 Read(./.env)처럼 상대 경로로 적은 규칙이 cd 이후에는 프로젝트를 더 이상 덮지 못했다가 이번 버전에서 고쳐졌습니다. 이제는 추가한 작업 폴더에도 같은 규칙이 적용됩니다. claude --version으로 버전을 확인하고, 낮으면 claude update를 실행하세요. 업데이트한 뒤에도 자격증명 파일은 되도록 작업 폴더 밖에 두는 편이 안전합니다.

- 근거 policy · 처음 2026-11-14 · 최근 확인 2026-11-14 · 재검토 2026-12-14 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-14 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > Fixed relative deny and ask permission rules (e.g. `Read(./.env)`) no longer covering the project after a `cd`
