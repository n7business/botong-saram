---
id: ai-tools-0280
domain: ai-tools
claim: AI로 계약서 지식을 정리할 때는 여러 에이전트가 표 하나에 동시에 요약하게 하지 말고 계약서마다 한 에이전트가 한 페이지에 조항을 원문
  그대로 옮기게 해야 사실 누락을 줄일 수 있다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: quoted the terms word for word rather than summarizing them into a shared
    table
  source: Anthropic Engineering 블로그
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- multi-agent
- contracts
- knowledge-base
- accuracy
verified_by: 실무자 실측(단일 출처)
---
기업 인수 시뮬레이션 과제에서 여러 에이전트가 공유 계약 조건표에 동시에 쓰자, 요약이 부실해지고 서로의 작업을 덮어써 일부 조건이 사라졌습니다. 그 결과 위키로 작성한 브리프에는 평가 대상 사실 57개 중 41개(72%)만 담겼습니다. 계약서마다 에이전트 하나가 자기 페이지를 맡아 조항을 그대로 인용하게 바꾸자 57개 전부가 남았습니다. 이 개선안은 Claude가 실패를 되돌아보고 지시문을 고쳐 위키를 다시 만드는 반복 과정에서 나왔습니다. 무엇이 가장 중요한 정보인지 지시문에 밝혀 두어야 하며, 이 수치는 벤치마크 과제 하나의 결과입니다.
