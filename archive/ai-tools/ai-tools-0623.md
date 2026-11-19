---
id: ai-tools-0623
domain: ai-tools
claim: AI가 만든 답변이나 결과물의 채점을 다른 AI에게 맡길 때는 그 채점 결과를 바로 믿지 말고, 일부를 사람이 채점 결과를 보지 않은
  채 따로 채점해 서로 얼마나 일치하는지부터 확인해야 한다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic
  seen: '2026-11-20'
  quote: Validate against human labels.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- LLM채점
- 품질검수
- 평가
---
AI 채점기는 수백 건을 금방 보지만, 고장이 나도 아무 표시 없이 점수를 계속 매기고, 바탕 모델이 바뀌면 조용히 더 엄격해지거나 더 너그러워질 수 있습니다. 그래서 먼저 표본 몇십 건을 사람이 AI 판정을 보지 않고 따로 판정해 AI 채점과 비교하세요. 사람끼리는 판정이 맞는데 AI와 자주 어긋나면 채점 기준을 고쳐야 하고, 사람끼리도 판정이 갈리면 무엇을 잴지부터 다시 정해야 합니다. 채점 지시는 이 분야를 모르는 유능한 동료에게 설명하듯 전문용어 없이 구체적으로 쓰세요.
