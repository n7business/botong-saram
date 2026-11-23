# 클로드 코드를 Homebrew나 WinGet으로 설치했다면 자동으로 업데이트되지 않으므로, brew upgrade claude-code나 winget upgrade Anthropic.ClaudeCode를 주기적으로 직접 실행해야 한다.

🏛 공식 발표 · Claude Code 공식 문서

공식 설치 명령(curl·irm)으로 설치하는 기본 방식은 백그라운드에서 최신 버전으로 자동 업데이트됩니다. 반면 Homebrew와 WinGet으로 설치하면 자동 업데이트가 되지 않습니다. 이 상태로 두면 새 기능은 물론 보안 수정도 받지 못합니다. Homebrew 사용자는 설치한 cask에 따라 brew upgrade claude-code 또는 brew upgrade claude-code@latest를, WinGet 사용자는 winget upgrade Anthropic.ClaudeCode를 정기적으로 실행해야 합니다. '특정 버전 이상으로 업데이트하라'는 안내를 받았다면 claude --version으로 실제 버전을 먼저 확인하세요.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-23 · https://code.claude.com/docs/en/overview
  > Homebrew installations do not auto-update.
- Anthropic · 2026-11-23 · https://code.claude.com/docs/en/quickstart
  > WinGet installations do not auto-update.
