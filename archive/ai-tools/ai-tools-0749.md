---
id: ai-tools-0749
domain: ai-tools
claim: AI로 계약서 여러 건의 조건을 정리시킬 때는 여러 에이전트가 표 하나에 함께 쓰게 하지 말고, 계약서마다 페이지를 하나씩 두고 에이전트
  하나가 맡아 조건을 원문 그대로 인용하게 해야 한다. Anthropic 실험에서 공유 표 방식은 서로 덮어써 사실 57개 중 41개만 남았지만,
  계약서별 페이지 방식은 57개가 모두 남았기 때문이다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: because agents had overwritten one another’s work
  source: Anthropic Engineering 블로그
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2026-12-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 계약서
- 멀티에이전트
- 문서정리
- 원문인용
verified_by: 실무자 실측(단일 출처)
---
Anthropic이 인수 거래 계약서들로 위키를 만들 때 처음에는 여러 에이전트가 계약 조건 표 하나에 동시에 적게 했습니다. 서로의 작업을 덮어쓰고 요약도 부실해서, 채점 대상 사실 57개 중 41개(72%)만 결과물에 남았습니다. 계약서마다 페이지를 따로 두고 에이전트 하나가 맡아 조건을 원문 그대로 인용하게 바꾸자 57개가 모두 남았습니다. 이 개선은 정리 지시에 '계약 조건이 가장 중요하다'는 점을 적어 넣으면서 나왔습니다. 계약서·견적서처럼 조건이 핵심인 자료를 AI에게 정리시킬 때는 무엇이 가장 중요한지 지시에 직접 적고, 문서 한 건에 결과 한 건씩 원문 인용으로 남기게 하는 것이 안전합니다.
