---
id: ai-tools-0278
domain: ai-tools
claim: AI 지식 위키를 만들어도 검색 도구를 없애지 말고 함께 제공해야 답변 점수가 더 높고 토큰도 절약된다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: the wiki helped Claude the most when we also gave it access to a search tool
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
- knowledge-base
- wiki
- search
- token-cost
verified_by: 실무자 실측(단일 출처)
---
Anthropic은 약 35만 개 파일, 약 4억 2천만 토큰 규모의 내부 문서에 대해 질문 25개로 시험했습니다. 위키만 쓴 경우 최고 점수는 48%, 검색만 쓴 경우는 53%였습니다. 위키와 검색을 함께 쓰자 위키가 커지면서 54%에서 61%로 올랐고, 질문당 약 20,000토큰도 절약되었습니다. 위키는 128세션에 걸쳐 만들었으므로, 규모가 작은 문서 묶음에서도 같은 효과가 난다고 볼 수는 없습니다.
