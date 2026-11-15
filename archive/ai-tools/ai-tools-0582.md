---
id: ai-tools-0582
domain: ai-tools
claim: 'AI 기능을 고객에게 유료로 제공한다면 AI Gateway의 Routing에서 비싼 모델에 fallback(예: OpenAI 실패 시
  Claude)을 걸어 두어야 하는데, 한 제공사가 장애를 일으켜도 유료 고객은 오류를 보지 않기 때문이다.'
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=f1quywzT-a8
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-16'
  quote: your paid users never see an error
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
- 라우팅
- fallback
---
Routing에서 새 route를 만들고 if-else 조건을 넣어 유료 플랜 고객은 비싼 모델로, 무료 고객은 DeepSeek 같은 싼 모델로 보낼 수 있습니다. 비싼 모델 단계에 fallback을 추가하면 OpenAI 호출이 실패할 때 자동으로 Claude로 넘어갑니다. 저장할 때는 오른쪽 위 Save and deploy를 누르고, 코드에서는 모델명을 dynamic/라우트이름으로 바꾸고 메타데이터에 plan 값을 넣으면 됩니다. 화자는 이런 분기·fallback·재시도를 많은 사람이 필요 없이 직접 코드로 만든다고 지적합니다.
