---
id: ai-tools-0484
domain: ai-tools
claim: AI가 만든 문서 정리 위키는 한두 번 만들어 보고 쓸모를 판단하지 말고, 여러 번에 걸쳐 내용을 보태고 고치고 정리하게 해야 하는데,
  처음 위키는 신입 직원 수준이라 이것만으로는 답을 잘 찾지 못하기 때문이다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-12'
  quote: performance on the 25 questions grew from 13% to 48% of graded criteria
  source: Anthropic Engineering 블로그
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 위키
- 에이전트메모리
- 드리밍
- 문서정리
verified_by: 실무자 실측(단일 출처)
---
AI 위키는 한 번에 완성되지 않습니다. 처음 만든 뒤 여러 차례 보태고, 틀린 내용을 고치고, 중복을 합치고, 원본과 대조하면서 점점 나아집니다. Anthropic 실험에서는 회사 내부 문서로 위키를 만드는 작업을 2회에서 128회로 늘리자 정답률이 13%에서 48%로 올랐습니다. 작업을 여러 번 나눠 돌린다면 공용 작업 기록을 두어 다음 작업이 앞선 진행 상황을 이어받게 하세요. 다만 반복할수록 비용이 들어갑니다. 그러니 여러 문서를 엮어야 답이 나오는 질문이 많을 때만 이렇게 하고, 원본 검색 기능도 함께 켜 두세요.
