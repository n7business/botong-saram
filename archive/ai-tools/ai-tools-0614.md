---
id: ai-tools-0614
domain: ai-tools
claim: AI 에이전트에 기획·제작·검토 역할을 나눠 붙이면 결과물은 좋아지지만 시간과 비용이 크게 늘므로, 지금 쓰는 AI가 혼자서는 제대로
  못 하는 어려운 작업에만 이 구성을 써야 한다. 앤트로픽 실험에서는 혼자 만들게 하면 20분에 9달러였는데 역할을 나눈 구성은 6시간에 200달러가
  들었다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/harness-design-long-running-apps
  author: Anthropic
  seen: '2026-11-19'
  quote: It is worth the cost when the task sits beyond what the current model does
    reliably solo.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 에이전트
- 비용
- 멀티 에이전트
- 코딩
verified_by: 실무자 실측(단일 출처)
---
앤트로픽 실험에서 같은 한 문장 요청으로 앱을 만들게 하자, 에이전트 하나는 20분 9달러가 들었고 기획·제작·검토로 나눈 구성은 6시간 200달러로 20배 넘게 들었습니다. 품질 차이는 컸지만, 모델이 좋아지자 혼자서도 잘하는 작업에서는 검토용 AI가 불필요한 비용이 됐습니다. 앤트로픽은 검토용 AI를 무조건 붙일지 말지로 정하지 말라고 합니다. 작업이 지금 모델이 혼자 안정적으로 해내는 범위를 넘을 때만 비용을 들일 가치가 있다는 것입니다. 쉬운 작업은 혼자 시키고, 어려운 작업에만 검토 단계를 붙이세요.
