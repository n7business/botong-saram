---
id: ai-tools-0511
domain: ai-tools
claim: AI에게 기억 메모 폴더를 맡길 때는 '실패한 것만 적어라'처럼 무엇을 적을지 정해 주지 말고 메모 폴더가 무엇에 쓰이는지만 알려 줘야
  하는데, 최신 모델은 고정 규칙을 주면 메모로 얻던 성능 향상을 상당 부분 잃었기 때문이다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: it helps to tell Claude what memory is for, but not how to use it
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
- claude
verified_by: 실무자 실측(단일 출처)
mentions: 1
---
클로드 같은 AI 에이전트에 세션이 바뀌어도 남는 메모 폴더를 쓰게 할 때는 '이 폴더에 다음 작업에 도움이 될 내용을 남길 수 있다' 정도로 목적만 알려 주는 편이 낫습니다. Anthropic 실험에서는 메모 폴더가 있다고만 알려 준 경우에도 Opus 4.7과 Opus 5가 메모를 잘 활용해 성능이 눈에 띄게 올랐습니다. 반대로 '실패만 기록하라'는 규칙을 주자 두 모델 모두 메모로 얻던 성능 향상을 상당 부분 잃었습니다. 성능이 좋은 모델일수록 무엇이 중요한지는 AI가 판단하게 두고, 사람이 기억하라고 직접 말한 것이나 분명히 남길 가치가 있는 것을 적으라는 정도로만 안내하는 것이 좋습니다.
