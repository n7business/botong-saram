# 업무용 컴퓨터에 Homebrew로 클로드 코드를 설치할 때는 claude-code@latest 대신 claude-code를 고르는 편이 좋은데, 일주일쯤 늦게 받는 대신 큰 문제가 생긴 버전은 건너뛰기 때문이다.

🏛 공식 발표 · Claude Code 공식 문서

Homebrew에는 클로드 코드 패키지가 두 가지 있습니다. claude-code는 안정(stable) 채널로, 보통 최신판보다 일주일쯤 늦고 큰 오류(회귀)가 있었던 버전은 건너뜁니다. claude-code@latest는 새 버전이 나오는 즉시 받습니다. 새 기능보다 매일 쓰는 업무가 멈추지 않는 게 중요하다면 안정 채널이 낫습니다. 어느 쪽이든 자동 업데이트는 되지 않으니 업그레이드는 직접 실행해야 합니다.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-11 · https://code.claude.com/docs/en/overview
  > skips releases with major regressions
