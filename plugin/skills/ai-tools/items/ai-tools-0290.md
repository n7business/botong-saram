# 클로드 코드 작업을 여러 개 백그라운드로 돌릴 때는 `claude agents`로 에이전트 뷰를 열어야, 대화 기록을 일일이 넘겨 보지 않고 내 입력이 필요한 세션을 바로 찾을 수 있다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

에이전트 뷰는 터미널에서 `claude agents`로 엽니다. 한 화면에서 모든 백그라운드 세션의 진행 중, 입력 대기, 완료 상태를 볼 수 있습니다. 새 세션도 이 화면에서 시작할 수 있습니다. 각 세션은 터미널이 연결되어 있지 않아도 계속 돌아가는 온전한 클로드 코드 대화이므로, 필요할 때 열어 답하면 됩니다.

- 근거 policy · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/agent-view
  > Agent view, opened with `claude agents`, is one screen for all your background sessions
