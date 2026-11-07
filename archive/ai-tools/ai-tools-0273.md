---
id: ai-tools-0273
domain: ai-tools
claim: AI 에이전트의 메모리에는 화면이나 시스템에서 바로 확인되는 정보를 쌓지 말고, 직접 알아낸 전략·계획·검증된 규칙만 적어야 오래된 기록을
  뒤지느라 작업이 늦어지는 일을 줄일 수 있다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: Fable 5, by comparison, wrote nine files in two folders
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
- memory-design
- claude
verified_by: 실무자 실측(단일 출처)
---
Anthropic이 포켓몬 레드 플레이로 두 모델의 메모리를 약 10,000스텝 시점에 비교했습니다. 모든 것을 기록한 Sonnet 3.7은 225개 폴더에 파일 413개를 쓰고 배지 1개를 얻었고, Fable 5는 폴더 2개의 파일 9개와 global.md 하나로 배지 4개를 얻었습니다. Sonnet 3.7의 기록은 상태가 바뀔 때마다 낡았고, 한때는 17스텝 동안 파일만 정리하며 게임을 진행하지 못했습니다. 현재 목표와 계획은 맨 위 파일 하나에 모으고, 다시 조회할 수 있는 값은 저장하지 않는 편이 좋습니다. 다만 각 모델 1회씩을 게임 환경에서 비교한 결과이므로 업무에도 같은 차이가 난다고 단정할 수는 없습니다.
