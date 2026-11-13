---
id: ai-tools-0414
domain: ai-tools
claim: AI에게 문서 묶음을 정리한 위키를 만들게 하는 것은 여러 문서를 엮어야 답이 나오는 질문이 많을 때만 하고, 문서 하나에서 검색으로
  찾을 수 있는 일에는 만들지 말아야 들인 품만큼 효과를 본다.
status: merged
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-10'
  quote: Claude scored 87% when it consulted the wiki, compared with 73% when it used
    search alone.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 지식관리
- 위키
- 문서검색
verified_by: 실무자 실측(단일 출처)
merged_into: ai-tools-0516
---
Anthropic 실험에서 여러 문서를 합치고 계산이나 판단까지 해야 하는 합병 관련 질문은 위키를 참고했을 때 87%, 검색만 썼을 때 73%를 맞혔습니다. 반대로 대부분 기준을 문서 하나에서 찾을 수 있는 과제에서는 위키의 효과가 뚜렷하지 않았습니다. 어떤 과제에서는 위키가 원본 문서보다 커져 요약 구실을 전혀 하지 못했습니다. 계약서·서류 묶음을 AI로 정리할 때는 질문이 여러 문서를 넘나드는지 먼저 따져 보고, 위키가 원본보다 커지지 않는지 확인해야 합니다.
