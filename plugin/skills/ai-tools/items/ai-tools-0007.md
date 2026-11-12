# Homebrew나 WinGet으로 설치한 Claude Code는 자동 업데이트되지 않으므로 주기적으로 직접 업그레이드 명령을 실행해야 최신 기능과 보안 패치를 받는다.

🏛 공식 발표 · Claude Code 공식 문서

네이티브 설치(curl 스크립트)는 백그라운드에서 자동 갱신되지만, Homebrew와 WinGet 설치본은 자동 갱신되지 않는다. Homebrew는 `brew upgrade claude-code`(또는 `claude-code@latest`), WinGet은 `winget upgrade Anthropic.ClaudeCode`를 주기적으로 돌린다. 버전이 오래되면 성능 저하나 이미 고쳐진 버그를 겪을 수 있으니, 이상 증상이 있으면 먼저 `claude --version`으로 버전을 확인한다. 자동 갱신을 원하면 네이티브 설치 방식을 택한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03

## 출처
- Anthropic (Claude Code Docs) · 2026-11-03 · https://code.claude.com/docs/en/overview
  > Homebrew installations do not auto-update.
