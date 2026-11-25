---
id: ai-tools-0823
domain: ai-tools
claim: 직원들의 AI 에이전트를 회사 시스템(MCP)에 연결할 때는 관리자 계정 하나를 같이 쓰게 하면 안 되고, 직무별로 조회만 할지 수정까지
  할지 권한을 나눠야 한다. MCP에는 아직 자체 권한 기능이 없어서 연결된 계정의 권한이 에이전트에 그대로 넘어가기 때문이다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=f1MqkjGyKsg
  author: 테디노트 TeddyNote (김현민 발표, 넥스클라우드)
  seen: '2026-11-25'
  quote: MCP 프로토콜에는 아직 권한 기능이 없고
  source: 테디노트 TeddyNote
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- MCP
- 권한관리
- 에이전트
- 보안
---
MCP로 연결하면 에이전트는 그 연결에 쓴 계정이 할 수 있는 일을 모두 할 수 있다. 권한을 나누지 않으면 예를 들어 마케팅 담당자의 에이전트가 서버를 내리는 일도 생길 수 있다. 상담 직원에게는 티켓·고객 기록 조회 권한만 주는 식으로, 직무에 필요한 만큼만 권한을 주는 계정이나 역할을 따로 만들어 연결해야 한다. 같은 이유로 여러 고객사를 관리한다면 고객사마다 연결을 따로 두어 한 고객 작업 중에 다른 고객 자료에 접근할 수 없게 해야 한다.
