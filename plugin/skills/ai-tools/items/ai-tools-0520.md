# 클로드 코드에서 fast mode를 쓸 거라면 대화 중간에 켜지 말고 세션을 시작할 때 켜야 하는데, 처음 켜는 순간 그때까지 쌓인 대화 전체를 캐시 없이 비싼 fast mode 입력 요금으로 다시 내기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

fast mode를 대화에서 처음 켜면 그때까지의 대화 맥락 전체에 캐시가 적용되지 않은 fast mode 입력 요금이 붙습니다. 대화가 길어진 뒤에 켤수록 이 비용이 커지므로, 세션을 시작할 때 켜는 것이 가장 쌉니다. fast mode와 표준 속도는 캐시를 따로 쓰기 때문에 중간에 켰다 껐다 할 때마다 대화의 일부나 전체를 다시 캐시 없이 읽게 됩니다. 빠르게 해야 할 작업이라면 처음부터 fast mode로 시작하고, 도중에 자주 바꾸지 마세요.

- 근거 policy · 처음 2026-11-13 · 최근 확인 2026-11-13 · 재검토 2026-12-09 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-13 · https://code.claude.com/docs/en/fast-mode
  > enable fast mode at the start of a session rather than switching mid-conversation.
