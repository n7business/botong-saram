# CLAUDE.md나 출력 스타일에 적은 지시는 강제되지 않으므로, 매번 반드시 실행돼야 하는 일(포맷터·린트 등)은 훅(hook)으로 건다.

🏛 공식 발표 · Claude Code 공식 문서

CLAUDE.md와 출력 스타일은 모두 Claude가 '지시'로 따르는 것이지 시스템이 강제하는 것이 아니다. 따라서 '파일 수정 후 항상 포맷터 실행', '커밋 전 린트' 같은 빠지면 안 되는 작업은 훅으로 설정한다. 훅은 Claude Code의 특정 이벤트(파일 편집 후, 커밋 전 등)에 셸 명령·HTTP 요청·MCP 호출을 자동 실행한다. '하지 말 것' 규칙을 CLAUDE.md에 적어도 가끔 어길 수 있다는 점을 전제로 설계한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03

## 출처
- Anthropic (Claude Code Docs) · 2026-11-03 · https://code.claude.com/docs/en/features-overview
  > Claude follows both as instructions, so neither is enforced. For anything that has to happen every time, use a hook.
