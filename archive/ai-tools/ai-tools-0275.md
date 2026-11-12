---
id: ai-tools-0275
domain: ai-tools
claim: 구형 AI 모델을 쓸 때는 답하기 전에 메모리를 읽고 자기 가설을 직접 시험하라고 지시해야 메모리 효과를 제대로 얻을 수 있다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: nearly doubled its benchmark score
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
- agent-memory
- prompting
- model-selection
verified_by: 실무자 실측(단일 출처)
---
Sonnet 4.6은 메모리 파일을 읽지 않는 경우가 많았고, 오답 원인에 대한 가설도 시험하지 않았습니다. 답하기 전에 메모리를 읽고 가설을 명시적으로 시험하라고 지시하자 벤치마크 점수가 거의 두 배가 되었습니다. Sonnet 5는 지시 없이도 10번 중 9번 답하기 전에 메모리를 읽었지만, Sonnet 4.6은 절반도 되지 않았습니다. 따라서 이런 지시가 필요한지는 쓰는 모델이 메모리를 실제로 읽는지 확인한 뒤 정하는 것이 좋습니다. 앞의 수치는 CL-Bench 데이터베이스 과제의 결과입니다.
