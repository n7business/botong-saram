---
id: ai-tools-0493
domain: ai-tools
claim: 구글 Vertex로 클로드 코드를 쓰면서 fast mode를 켰다면 global·us·eu 리전에서만 지원되고 Vertex가 거부하면
  표준 속도로 돌아가므로, 속도가 빨라지지 않았다면 리전 설정부터 확인해야 한다.
status: verified
evidence: policy
confidence: 0.6
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-12'
  quote: falling back to standard speed if Vertex refuses it
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- fast-mode
- vertex
- 리전
verified_by: 공식 출처
---
클로드 코드 2.1.322부터 Vertex에서도 fast mode를 쓸 수 있지만 global, us, eu 리전에 한정됩니다. Vertex가 fast mode 요청을 거부하면 작업이 멈추지 않고 표준 속도로 이어집니다. 그래서 fast mode를 켰는데 체감 속도가 그대로라면 오류로 생각하지 말고 사용 중인 리전이 지원 리전인지 확인해야 합니다. 클로드 코드를 Vertex로 쓰지 않는다면 신경 쓰지 않아도 됩니다.
