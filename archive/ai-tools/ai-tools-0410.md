---
id: ai-tools-0410
domain: ai-tools
claim: AI 에이전트에게 메모리 폴더를 줄 때는 메모리가 무엇에 쓰이는지만 알려 주고 '실패만 기록하라' 같은 고정 규칙을 정하지 말아야, 최신
  모델이 메모리로 얻는 성능 향상을 깎아 먹지 않는다.
status: merged
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-10'
  quote: it helps to tell Claude what memory is for, but not how to use it
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
- 프롬프트
- 클로드
verified_by: 실무자 실측(단일 출처)
merged_into: ai-tools-0511
---
Anthropic이 실험해 보니 메모리 폴더가 있다고만 알려 줘도 최신 모델은 메모리를 잘 활용해 성능이 눈에 띄게 올랐습니다. 반대로 '실패만 기록하라'는 규칙을 주자 Opus 5와 Opus 4.7 모두 메모리로 얻던 향상분의 상당 부분을 잃었습니다. 그러니 클로드 코드 같은 도구에 메모리를 맡길 때는 무엇을 적을지 세세하게 정하지 말고, 요청받았거나 기억할 가치가 분명할 때 적으라는 정도로만 지시하는 편이 낫습니다. 다만 오래된 모델은 이런 판단이 약하므로 따로 안내가 필요할 수 있습니다.
