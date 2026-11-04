# 프롬프트에 'ultrathink'라는 단어가 들어가면 그 턴이 가장 높은 추론 강도(xhigh)로 실행돼 시간과 비용이 늘어나므로, 붙여넣은 글 등에서 의도치 않게 켜지는 걸 막으려면 CLAUDE_CODE_DISABLE_ULTRATHINK=1로 끈다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

ultrathink는 Claude Code의 매직 키워드로, 프롬프트에 포함되면 해당 턴의 추론 강도를 xhigh로 올린다. 2.1.316부터 VS Code 확장에서도 터미널과 같게 xhigh로 동작하며 입력창에 무지개색으로 표시된다. 같은 버전에서 CLAUDE_CODE_DISABLE_ULTRATHINK 환경변수가 추가돼 이 키워드를 완전히 끌 수 있다. 문서나 로그를 그대로 붙여넣어 작업하는 사람은 그 안에 든 단어 때문에 의도치 않게 고비용 턴이 생길 수 있으니 꺼 두는 편이 예측 가능하다. 깊은 추론이 필요할 때는 /effort나 모델 변경으로 명시적으로 조절한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 공식 출처

## 출처
- anthropics · 2026-11-03 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  > Added `CLAUDE_CODE_DISABLE_ULTRATHINK`, which turns the `ultrathink` keyword off
- anthropics · 2026-11-03 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  > Changed `ultrathink` to run its turn at `xhigh` effort
