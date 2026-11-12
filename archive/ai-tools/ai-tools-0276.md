---
id: ai-tools-0276
domain: ai-tools
claim: AI가 남긴 메모는 원본 대화 기록과 대조해 고쳐야, 처음부터 틀렸거나 낡은 메모를 다음 세션에서 그대로 믿고 같은 실패를 반복하는 일을
  막을 수 있다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: Dreaming gives Claude a way to test its notes against the original transcripts
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
- dreaming
- verification
verified_by: 실무자 실측(단일 출처)
---
AI는 세션 안에서 중요하다고 판단한 내용을 메모하므로, 틀린 메모도 다음 세션에서 그대로 읽고 신뢰할 수 있습니다. Anthropic의 포켓몬 실험에서 Claude는 건물 위치를 잘못 적은 뒤 같은 낭떠러지로 세 번 떨어졌고, 그 실행에서는 다음 도시에 끝내 도착하지 못했습니다. 유휴 시간에 메모를 기록과 대조해 고치는 '드리밍'을 돌리자 Claude가 오류를 찾아 메모를 고쳤고, 고친 메모로 다음 도시에 도착했습니다. 대조하려면 작업 기록이 남아 있어야 하므로 로그나 대화 기록을 함께 보관해야 합니다. 이 결과는 특정 함정 하나를 대상으로 한 실험입니다.
