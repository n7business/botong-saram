# Homebrew로 클로드 코드를 설치할 때 큰 결함이 있는 버전을 피하고 싶으면 `claude-code`를, 새 버전을 바로 받고 싶으면 `claude-code@latest`를 고른다.

🏛 공식 발표 · Claude Code 공식 문서

Homebrew에는 두 가지 cask가 있습니다. `claude-code`는 안정 채널을 따르며, 보통 최신보다 일주일쯤 늦고 큰 회귀가 있는 릴리스는 건너뜁니다. `claude-code@latest`는 최신 채널을 따르며 새 버전이 나오는 즉시 받습니다. 어느 쪽이든 자동으로 업데이트되지는 않으므로 설치한 cask에 맞는 업그레이드 명령을 직접 실행해야 합니다.

- 근거 policy · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/overview
  > `claude-code` tracks the stable release channel, which is typically about a week behind and skips releases with major regressions.
