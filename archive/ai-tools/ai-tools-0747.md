---
id: ai-tools-0747
domain: ai-tools
claim: AI가 쌓아 둔 메모리 노트는 그대로 믿지 말고, 주기적으로 원래 대화 기록과 대조해 틀린 내용을 고치게 해야 한다. 작업 중에 잘못
  적힌 메모는 다음 세션에서도 사실처럼 쓰이는데, Anthropic 실험에서 틀린 메모를 고치지 않은 AI는 같은 함정에 세 번 빠진 끝에 목표에
  닿지 못했기 때문이다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: Dreaming gives Claude a way to test its notes against the original transcripts
  source: Anthropic Engineering 블로그
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2026-12-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- dreaming
- 메모리점검
- 검증
verified_by: 실무자 실측(단일 출처)
---
AI는 작업 도중 중요해 보이는 것을 메모리에 적는데, 처음부터 틀렸거나 상황이 바뀌어 낡은 메모도 다음 세션에서 그대로 믿고 씁니다. Anthropic 실험에서 클로드는 건물 위치를 반대편으로 잘못 적고 '통과 완료'라고 기록했습니다. 그 뒤로 같은 함정에 세 번 빠졌고 결국 다음 도시에 도착하지 못했습니다. 메모를 원래 대화 기록과 대조하는 정리 작업('드리밍')을 돌리자 클로드가 스스로 오류를 찾아 고쳤고, 고친 메모로 다시 하자 목표에 도달했습니다. 업무에서도 AI가 남긴 메모리 파일을 한가할 때 '원본 기록과 대조해서 틀린 메모를 고쳐 줘'라고 시켜 점검하는 것이 좋습니다.
