---
id: ai-tools-0541
domain: ai-tools
claim: 계약서 여러 건을 AI 에이전트 여러 개에게 나눠 정리시킬 때는 한 표에 같이 쓰게 하지 말고, 계약서마다 한 에이전트가 자기 페이지를
  따로 만들어 조건을 요약 없이 원문 그대로 옮기게 해야 한다. 여러 에이전트가 한 표에 함께 쓰면 서로 쓴 내용을 덮어써서 핵심 조건이 빠지기
  때문이다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic
  seen: '2026-11-14'
  quote: agents had overwritten one another’s work.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 에이전트
- 계약서
- 위키
- 멀티에이전트
- 요약
verified_by: 실무자 실측(단일 출처)
mentions: 1
---
Anthropic 실험에서 에이전트 여러 개가 계약 조건 표 하나에 동시에 쓰게 했더니 서로 쓴 내용을 덮어썼습니다. 그 결과 채점 대상 사실 57개 중 41개(72%)만 남았습니다. 계약서마다 에이전트 하나가 자기 페이지를 맡아 조건을 원문 그대로 인용하게 바꾸자 57개가 모두 남았습니다. 금액·기한·해지 조건처럼 틀리면 안 되는 내용은 AI가 요약하게 두지 말고 원문 문장을 그대로 옮기게 하세요. 여러 AI에게 일을 나눌 때는 한 파일을 함께 고치게 하지 말고 각자 맡은 파일을 따로 정해 주는 것이 안전합니다.
