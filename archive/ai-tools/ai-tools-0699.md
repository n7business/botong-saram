---
id: ai-tools-0699
domain: ai-tools
claim: AI에게 챗봇 답변 채점을 맡길 때는 '주의 문구나 경고가 붙어 있어도 부적절한 내용이면 불합격'이라고 채점 지시에 직접 적어야 한다.
  그렇게 적지 않으면 채점 AI가 겉에 붙은 안전 문구만 보고 점수를 후하게 줄 수 있다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: A grader that isn't told otherwise may give too much credit to such language.
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
- LLM채점
- 평가
- 채점기준
---
답변에 '참고만 하세요', '전문가와 상담하세요' 같은 문구가 붙어 있어도 본문에 해서는 안 될 내용이 들어 있을 수 있습니다. 따로 말해 두지 않으면 채점 AI는 이런 문구에 점수를 더 줄 수 있습니다. 채점 지시문에 '면책 문구·단서·교육용이라는 설명이 있어도 내용이 부적절하면 불합격'이라고 적고, 답변의 형식이 아니라 실제 내용을 보고 판단하게 해야 합니다.
