---
id: ai-tools-0702
domain: ai-tools
claim: 챗봇 답변을 '예'라는 단어가 있는지 같은 글자 찾기로 자동 채점할 때는, 정중하게 거절한 답까지 '수락'으로 잘못 세지 않는지 표본을
  직접 읽어 확인해야 한다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic Engineering
  seen: '2026-11-23'
  quote: pattern matching, such as extracting a “Yes” or “No” from the response, can
    miss nuance.
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
- 자동채점
- 평가
- 챗봇
---
답변에서 '예/아니오'나 특정 단어만 뽑아 맞고 틀림을 정하는 방식은 빠르고 객관적이지만 맥락을 놓칩니다. 예를 들어 '네, 기꺼이 돕겠지만 이 요청은 어렵습니다'라는 답이 '예'로 집계될 수 있습니다. 정답이 분명한 항목에만 글자 찾기를 쓰고, 해석이 필요한 항목은 AI 채점이나 사람 검토로 넘기며, 각 문항의 모범 답안이 그 채점 방식을 통과하는지도 먼저 확인합니다.
