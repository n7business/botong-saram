---
id: ai-tools-0290
domain: ai-tools
claim: 클로드 코드 작업을 여러 개 백그라운드로 돌릴 때는 `claude agents`로 에이전트 뷰를 열어야, 대화 기록을 일일이 넘겨 보지
  않고 내 입력이 필요한 세션을 바로 찾을 수 있다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/agent-view
  author: Anthropic
  seen: '2026-11-07'
  quote: Agent view, opened with `claude agents`, is one screen for all your background
    sessions
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- agent-view
- 병렬작업
verified_by: 공식 출처
---
에이전트 뷰는 터미널에서 `claude agents`로 엽니다. 한 화면에서 모든 백그라운드 세션의 진행 중, 입력 대기, 완료 상태를 볼 수 있습니다. 새 세션도 이 화면에서 시작할 수 있습니다. 각 세션은 터미널이 연결되어 있지 않아도 계속 돌아가는 온전한 클로드 코드 대화이므로, 필요할 때 열어 답하면 됩니다.
