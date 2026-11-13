---
id: ai-tools-0411
domain: ai-tools
claim: AI 메모리에는 매번 화면이나 자료에서 다시 확인할 수 있는 정보까지 다 쌓지 말고 직접 알아낸 전략·검증된 규칙·계획만 남겨야, 메모리를
  뒤지느라 정작 일을 못 하는 상황을 막을 수 있다.
status: merged
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-10'
  quote: Sonnet 3.7 assumed everything might matter and wrote to memory indiscriminately.
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
- 에이전트메모리
- 컨텍스트관리
verified_by: 실무자 실측(단일 출처)
merged_into: ai-tools-0512
---
포켓몬 게임 실험에서 모든 것을 기록한 Sonnet 3.7은 파일 413개를 폴더 225개에 나눠 만들고도 배지를 1개밖에 얻지 못했습니다. 핵심만 적은 Fable 5는 파일 9개와 global.md 하나로 배지 4개를 얻었습니다. 소지금이나 현재 위치처럼 매번 화면에서 읽을 수 있는 정보는 저장해도 금방 낡고, 저장 자체가 중복입니다. 업무에서도 AI 메모리에는 시스템이 알려 주지 않는 판단 기준, 시도해서 확인한 규칙, 다음 할 일만 남기게 하는 것이 좋습니다.
