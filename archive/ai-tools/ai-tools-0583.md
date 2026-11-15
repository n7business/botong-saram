---
id: ai-tools-0583
domain: ai-tools
claim: '고객마다 AI를 쓰게 하는 서비스라면 요청 헤더에 user ID 메타데이터를 붙이고 AI Gateway 라우트에 사용자별 레이트 리밋과
  예산 한도(예: 1인 1달러)를 걸어, 넘으면 더 싼 모델로 돌아가게 해야 한 사람이 비용을 다 써 버리는 일을 막을 수 있다.'
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=f1quywzT-a8
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-16'
  quote: 모든 사용자에게 AI 예산을 줄 수 있다
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- cloudflare
- ai-gateway
- 사용자별예산
- 메타데이터
---
요청 헤더 하나에 user ID를 담은 JSON을 넣으면 대시보드에서 요청마다 사용자가 표시되고, 그 값을 기준으로 지출 한도와 레이트 한도를 걸 수 있습니다. 라우트에 분당 100건 같은 사용자별 레이트 리밋과 사용자별 예산을 추가하고, 한도를 넘으면 fallback 경로로 가게 해 거기에 싼 모델을 연결합니다. 이렇게 하면 한도를 넘은 고객도 서비스가 끊기지 않고 저렴한 모델로 계속 쓸 수 있습니다. 화자는 이 사용자별 지출 한도를 가장 좋아하는 기능으로 꼽습니다.
