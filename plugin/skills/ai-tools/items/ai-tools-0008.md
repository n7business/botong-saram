# Claude Code를 안정적으로 쓰려면 Homebrew의 stable 채널(claude-code)을 설치하고, 신기능을 바로 쓰려면 latest 채널(claude-code@latest)을 설치한다.

🏛 공식 발표 · Claude Code 공식 문서

Homebrew는 두 개의 cask를 제공한다. `claude-code`는 stable 채널로 보통 1주일 정도 늦게 나오지만 큰 회귀가 있는 버전은 건너뛴다. `claude-code@latest`는 새 버전이 나오는 즉시 받는다. 업무용으로 안정성이 중요하면 stable, 최신 기능 검증이 목적이면 latest를 고른다. 어느 쪽이든 자동 갱신은 안 되니 직접 업그레이드해야 한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03

## 출처
- Anthropic (Claude Code Docs) · 2026-11-03 · https://code.claude.com/docs/en/overview
  > claude-code tracks the stable release channel, which is typically about a week behind and skips releases with major regressions.
