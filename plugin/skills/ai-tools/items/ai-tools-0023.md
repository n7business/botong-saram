# 서브에이전트가 메인 세션의 높은 추론 강도를 그대로 물려받아 비용이 새는 걸 막으려면 CLAUDE_CODE_SUBAGENT_EFFORT로 서브에이전트 기본 강도를 따로 낮게 지정한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

2.1.316에서 CLAUDE_CODE_SUBAGENT_EFFORT 환경변수가 추가됐다. 다른 곳에서 강도를 지정하지 않은 서브에이전트는 세션 강도를 상속하는 대신 이 값으로 실행된다. 2.1.317부터는 메인 대화와 다른 모델을 쓰는 서브에이전트·팀원은 세션 강도가 아니라 그 모델에 저장된 강도나 기본값을 쓴다. 메인 세션을 high로 올려 두고 파일 찾기·로그 읽기 같은 조회성 서브에이전트를 많이 띄우면 그 비용이 전부 high로 나가므로, 이 변수를 low나 medium으로 두면 검증 작업 품질은 유지하면서 조회 비용을 줄일 수 있다. 서브에이전트 정의 파일(.claude/agents/*.md)에 명시한 강도가 있으면 그쪽이 우선한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 공식 출처

## 출처
- anthropics · 2026-11-03 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  > Added `CLAUDE_CODE_SUBAGENT_EFFORT` to set the effort level subagents run at when nothing else names one
- anthropics · 2026-11-03 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317
  > Changed subagents and teammates on a different model from the main conversation to use that model's saved effort level or its default
