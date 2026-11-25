# IntelliJ·PyCharm 같은 JetBrains 프로그램에서 클로드 코드를 쓰려면 마켓플레이스에서 플러그인만 깔아서는 안 되고, 클로드 코드 CLI를 따로 설치한 뒤 프로그램을 다시 시작해야 한다.

🏛 공식 발표 · Claude Code 공식 문서

VS Code 확장과 달리 JetBrains용 클로드 코드 플러그인은 CLI가 깔려 있어야 돌아갑니다. 먼저 터미널에서 클로드 코드 CLI를 설치하고 claude --version으로 버전이 나오는지 확인합니다. 그다음 JetBrains Marketplace에서 Claude Code 플러그인을 설치하고 IDE를 다시 시작합니다.

- 근거 policy · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 2026-12-25 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-25 · https://code.claude.com/docs/en/overview
  > The plugin requires the Claude Code CLI, installed separately
