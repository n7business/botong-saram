---
id: ai-tools-0698
domain: ai-tools
claim: 고객 응대용 AI 챗봇을 시험할 때는 거절해야 할 질문만 던지지 말고, 같은 주제의 평범한 질문도 짝지어 함께 시험해 '거절해야 할 때
  거절했나'와 '답해야 할 때 괜히 거절하지 않았나'를 둘 다 세어야 한다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: A good eval also needs to measure both compliance with harmful requests and
    over-refusal of benign requests.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- 평가
- 과잉거절
- 시험설계
---
무엇이든 거절하는 챗봇은 '위험한 답을 안 했나'만 보는 시험에서는 만점을 받지만, 실제 손님에게는 쓸모가 없습니다. 그래서 같은 주제 안에서 거절해야 할 질문(예: 없는 할인을 약속해 달라는 요구)과 답해야 할 질문(예: 실제 할인 조건 문의)을 짝지어 시험 목록을 만듭니다. 결과는 '위험한 요청에 제대로 대응한 비율'과 '정상 질문을 거절한 비율' 두 숫자로 따로 봅니다. 경계에 걸친 질문을 어느 쪽에 넣을지는 업무를 잘 아는 사람이 정해야 합니다.
