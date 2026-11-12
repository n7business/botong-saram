# 클로드 코드 플러그인은 켜 두기만 해도 모든 대화에서 토큰을 쓰므로, 요즘 쓰지 않는 플러그인은 지우지 않더라도 꺼 두어야 사용량과 컨텍스트 낭비를 줄일 수 있다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

켜져 있는 플러그인은 그 플러그인을 쓰지 않는 세션에도 매번 함께 실립니다. 플러그인에 든 스킬·에이전트·명령의 이름과 설명이 매 턴 컨텍스트에 들어가 사용량에 잡히고, 플러그인의 MCP 서버도 세션마다 같이 실행됩니다. 공식 마켓플레이스 플러그인은 설치하기 전에 /plugin 화면에서 예상 컨텍스트 비용(Context cost)을 볼 수 있습니다. 설치한 뒤에는 Installed 탭의 'Not used recently' 목록을 확인하고, /plugin이나 claude plugin disable로 꺼 두십시오.

- 근거 policy · 처음 2026-11-09 · 최근 확인 2026-11-09 · 재검토 2026-12-09 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-09 · https://code.claude.com/docs/en/plugins
  > An enabled plugin is part of every session, not only the sessions where you use it.
