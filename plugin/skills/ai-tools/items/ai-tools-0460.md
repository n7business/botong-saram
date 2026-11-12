# 클로드 코드 자동 모드에서 쓰는 LLM 게이트웨이가 서버 측 검사를 지원하지 못한다는 것을 이미 안다면 세션 시작 전에 CLAUDE_CODE_AUTO_MODE_SERVER=0을 설정해 매번 뜨는 안내를 없앨 수 있지만, 분류기 요청 비용은 그대로 나가고 이 설정은 나중 버전에서 없어질 수 있다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

게이트웨이나 프록시가 anthropic-beta 헤더와 safeguards 필드를 그대로 넘기지 않으면 자동 모드의 무료 서버 검사가 동작하지 않습니다. 게이트웨이를 직접 운영하지 않는다면 회사 관리자나 게이트웨이 업체에 이 두 항목과 응답의 safeguard_results 필드를 그대로 전달해 달라고 요청하는 것이 먼저입니다. 고칠 수 없다는 것이 확실할 때만 셸이나 settings의 env에 CLAUDE_CODE_AUTO_MODE_SERVER=0을 넣으세요. 이렇게 하면 안내는 사라지지만 분류기 요청은 계속 토큰 사용량으로 과금됩니다. Anthropic API에 직접 연결한 경우에는 v2.1.281 이상에서만 동작하고, 임시 설정이라 이후 릴리스에서 빠질 수 있습니다.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-11 · https://code.claude.com/docs/en/auto-mode-classifier-billing
  > `CLAUDE_CODE_AUTO_MODE_SERVER` is a temporary setting and may be removed in a later release.
