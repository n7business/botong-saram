---
id: ai-tools-0782
domain: ai-tools
claim: AI 채점기를 믿기 전에 모범 답안을 직접 넣어 합격이 나오는지 먼저 확인해야 하고, 채점에 쓰는 AI 모델이 바뀌면 같은 답안의 점수가
  그대로인지 다시 확인해야 한다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-25'
  quote: does a reference solution exist for every item, and does it pass your grader?
  source: Anthropic Engineering 블로그
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- 평가
- LLM채점
- 모델변경
---
AI 채점기는 고장이 나도 아무 경고 없이 점수를 계속 매길 수 있습니다. 바탕 모델이 바뀌면 전보다 엄하게 또는 후하게 채점하기도 합니다. 시험 질문마다 모범 답안을 준비해 두고 채점기에 넣어 합격이 나오는지 확인합니다. 점수가 갑자기 이상하게 나오면 챗봇보다 채점 설정을 먼저 의심해야 합니다. 채점 AI가 '확신이 낮다'고 표시한 건은 사람이 직접 읽어 봅니다.
