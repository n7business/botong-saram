# WSL이 아닌 일반 윈도우에서 클로드 코드를 쓴다면 Git for Windows를 먼저 설치해야 한다. 설치하지 않으면 클로드 코드가 Bash 대신 PowerShell로 명령을 실행한다.

🏛 공식 발표 · Claude Code 공식 문서

공식 문서는 일반 윈도우 환경에 Git for Windows 설치를 권장합니다. 이것이 있어야 클로드 코드가 Bash 도구를 쓸 수 있고, 없으면 PowerShell을 셸 도구로 씁니다. 인터넷 안내나 AI가 알려 주는 명령은 대부분 Bash 기준이라, PowerShell로만 돌리면 그대로 실행되지 않을 수 있습니다. WSL을 쓴다면 Git for Windows는 필요 없습니다.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-23 · https://code.claude.com/docs/en/quickstart
  > Git for Windows is recommended on native Windows
