---
id: ai-tools-0483
domain: ai-tools
claim: AI에게 계약서 같은 자료를 정리한 위키나 요약집을 만들게 할 때는 어떤 정보가 가장 중요한지 지시문에 분명히 적어야 하는데, 이를 적지
  않으면 핵심 조건이 요약 과정에서 빠질 수 있기 때문이다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-12'
  quote: The contract terms were the most important part of the wiki, but the instructions
    didn't say that.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 위키
- 지시문
- 계약서
- 문서정리
- 프롬프트
verified_by: 실무자 실측(단일 출처)
---
AI에게 자료 정리를 맡길 때 '정리해 줘'라고만 하면, AI는 무엇이 중요한지 모른 채 고르게 요약합니다. 그러면 꼭 필요한 정보가 빠질 수 있습니다. Anthropic 실험에서 인수합병 계약서로 위키를 만들었을 때, 계약 조건이 가장 중요하다는 점을 지시문에 적지 않자 평가 항목 57개 가운데 41개만 남았습니다. 결과물에 빠진 내용이 있다면 AI에게 무엇이 왜 빠졌는지 돌아보게 하세요. 그다음 지시문 고칠 곳을 제안받아 다시 만들게 하면 됩니다. 실험에서는 지시문을 고치고 계약서마다 한 AI가 원문 그대로 옮기게 하자 57개가 모두 남았습니다.
