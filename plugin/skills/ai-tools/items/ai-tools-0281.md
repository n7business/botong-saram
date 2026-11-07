# 클로드 코드를 Homebrew나 WinGet으로 설치했다면 자동 업데이트가 되지 않으므로, 업그레이드 명령을 직접 실행해야 최신 기능과 보안 수정을 받을 수 있다.

🏛 공식 발표 · Claude Code 공식 문서

네이티브 설치본은 백그라운드에서 자동으로 업데이트되지만 Homebrew와 WinGet 설치본은 자동으로 업데이트되지 않습니다. Homebrew는 설치한 cask에 맞춰 `brew upgrade claude-code` 또는 `brew upgrade claude-code@latest`를 실행합니다. WinGet은 `winget upgrade Anthropic.ClaudeCode`를 주기적으로 실행합니다. 직접 업데이트하지 않으면 보안 수정도 받지 못합니다.

- 근거 policy · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/overview
  > Homebrew installations do not auto-update.
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/overview
  > WinGet installations do not auto-update.
