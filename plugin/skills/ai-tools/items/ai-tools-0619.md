# 클로드 코드 권한 설정이나 훅·스킬 파일을 고친 뒤에는 v2.1.327 이상에서 /status를 열어 무시된 권한 설정이나 한 번도 걸리지 않는 훅 조건이 없는지 확인해야 한다. 설정이 잘못돼도 오류 없이 무시될 수 있기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

v2.1.327부터 /status에 문제가 있는 설정 목록이 표시됩니다. 깨진 에이전트·스킬·명령·출력 스타일 파일, 단축키 오류, 쓸 수 없는 샌드박스, 무시된 권한 설정, 어떤 도구 호출과도 맞지 않는 훅 조건이 여기에 나옵니다. 위험한 명령을 막으려고 만든 규칙이나 훅도 형식이 틀리면 조용히 적용되지 않을 수 있습니다. 설정을 바꿀 때마다 /status를 한 번 열어 두 목록이 비어 있는지 보는 습관을 들이세요.

- 근거 policy · 처음 2026-11-19 · 최근 확인 2026-11-19 · 재검토 2026-12-19 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-19 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > Added a list in `/status` of broken agent, skill, command and output style files, keybinding errors, an unavailable sandbox, ignored permission settings and hook matchers that never match
