---
id: ai-tools-0518
domain: ai-tools
claim: Sonnet 4.6 같은 이전 세대 모델에 메모 기능을 쓰게 한다면 '답하기 전에 메모 파일을 먼저 읽고, 틀린 이유에 대한 추측은 직접
  확인하라'고 지시문에 적어야 하는데, 이 지시만으로 점수가 두 배 가까이 올랐기 때문이다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: prompting Claude to read its memory files before answering
  source: Anthropic Engineering 블로그
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- 프롬프트
- 모델선택
verified_by: 실무자 실측(단일 출처)
mentions: 1
---
예전 모델은 메모 폴더가 있어도 읽지 않거나, 틀린 이유를 추측만 하고 확인하지 않는 경우가 많았습니다. Anthropic 실험에서 Sonnet 4.6은 답하기 전에 메모를 읽은 경우가 절반이 안 됐지만, Sonnet 5는 지시가 없어도 10번 중 9번은 메모를 먼저 읽었습니다. Sonnet 4.6에 메모를 먼저 읽고 추측을 직접 확인하라고 지시하자 점수가 두 배 가까이 올랐습니다. 비용 때문에 이전 모델을 쓴다면 이런 지시를 명시하고, 최신 모델이라면 목적만 알려 주는 것으로 충분합니다.
