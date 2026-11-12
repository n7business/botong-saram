---
id: ai-tools-0448
domain: ai-tools
claim: 계약서 여러 건을 AI에게 정리시켜 자료집을 만들 때는 여러 AI가 표 하나에 함께 요약해 넣게 하지 말고, 계약서마다 한 AI가 페이지를
  따로 맡아 조건을 원문 그대로 옮기게 해야 중요한 조건이 빠지지 않는다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-11'
  quote: quoted the terms word for word rather than summarizing them into a shared
    table
  source: Anthropic Engineering 블로그
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- wiki
- contracts
- multi-agent
- summarization
verified_by: 실무자 실측(단일 출처)
---
Anthropic이 시험해 보니, 여러 에이전트가 계약 조건 표 하나에 동시에 쓰게 했을 때는 서로 쓴 내용을 덮어써서 채점 대상 사실 57개 중 41개(72%)만 남았습니다. 계약서마다 에이전트 하나가 페이지를 따로 맡고 조건을 요약 없이 원문 그대로 옮기게 바꾸자 57개가 모두 남았습니다. 계약 조건·약관·고시처럼 문구 하나가 결론을 바꾸는 자료는 AI에게 '요약해 줘'보다 '해당 조항을 그대로 옮겨 줘'라고 맡겨야 합니다. 여러 AI를 한꺼번에 돌릴 때는 같은 파일이나 표를 동시에 고치지 않도록 각자 맡을 범위를 나눠 주십시오.
