---
id: ai-tools-0542
domain: ai-tools
claim: AI가 정리한 결과물에서 중요한 내용이 자꾸 빠진다면 지시문을 직접 계속 고치기만 하지 말고, AI에게 무엇을 놓쳤는지 돌아보게 한 뒤
  지시문 수정안을 내게 하고 그 지시문으로 다시 만들게 해야 한다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic
  seen: '2026-11-14'
  quote: Claude reflected on its failures, proposed a change to the instructions,
    and rebuilt the wiki.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2026-12-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 지시문
- 프롬프트개선
- 반복업무
- 위키
verified_by: 실무자 실측(단일 출처)
---
Anthropic은 계약서 위키를 만들 때 처음 지시문에 '계약 조건이 가장 중요하다'는 말이 없어 핵심 사실이 빠졌습니다. 그래서 AI가 실패 원인을 돌아보고, 지시문 수정안을 내고, 위키를 다시 만드는 과정을 반복하게 했습니다. 이 과정에서 AI는 계약 조건을 원문 그대로 따라야 한다는 점을 스스로 찾아 지시문에 반영했습니다. 그 결과 채점 기준 충족률이 72%에서 100%로 올랐습니다. 반복 업무라면 빠진 항목을 AI에게 보여 주고 '이게 왜 빠졌는지, 지시문을 어떻게 바꾸면 되는지'를 물어보세요. 바뀐 지시문은 사람이 확인한 뒤 확정해야 합니다.
