# 저장소에 다른 AI 코딩 도구용 AGENTS.md가 이미 있다면 클로드 코드용 CLAUDE.md를 따로 만들 필요가 없다. 클로드 코드가 CLAUDE.md 대신 AGENTS.md를 읽을 수 있다.

🏛 공식 발표 · Claude Code 공식 문서

CLAUDE.md는 클로드 코드가 대화를 시작할 때마다 읽는 규칙 파일입니다. 코딩 규칙, 설계 결정, 선호하는 라이브러리, 검토 체크리스트를 적어 둡니다. 코덱스 같은 다른 코딩 에이전트를 위해 AGENTS.md를 이미 만들어 두었다면, 클로드 코드는 그 파일을 CLAUDE.md 대신 읽을 수 있습니다. 같은 규칙을 두 파일에 나눠 적으면 한쪽만 고치고 다른 쪽은 놓치기 쉬우므로, 규칙은 한 곳에서 관리하는 편이 낫습니다.

- 근거 policy · 처음 2026-11-28 · 최근 확인 2026-11-28 · 재검토 2026-12-28 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-28 · https://code.claude.com/docs/en/overview
  > If your repository already has an `AGENTS.md` for other coding agents, Claude Code can read that
