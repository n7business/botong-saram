---
id: ai-tools-0744
domain: ai-tools
claim: AI에게 메모리(기억 노트)를 쓰게 할 때는 '실패한 것만 적어라' 같은 고정 규칙을 주지 말고 메모리가 무엇에 쓰이는지만 알려 줘야
  한다. Anthropic 실험에서 '실패만 기록' 규칙을 주자 최신 모델들이 메모리로 얻던 성능 향상의 상당 부분을 잃었기 때문이다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: it helps to tell Claude what memory is for, but not how to use it
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
- claude-code
- 프롬프트
- 메모리
verified_by: 실무자 실측(단일 출처)
---
클로드 코드의 메모리나 프로젝트 지침에 무엇을 기억하라고 적을 때, 적을 항목을 하나하나 정한 규칙은 오히려 결과를 나쁘게 만들 수 있습니다. Anthropic은 데이터베이스 질문 과제에서 메모리 폴더가 있다는 사실만 알렸는데, Opus 4.7과 Opus 5는 그것만으로 메모리를 잘 써서 성능이 눈에 띄게 올랐습니다. 반대로 '실패만 기록하라'는 규칙을 주자 두 모델 모두 메모리로 얻던 향상의 상당 부분을 잃었습니다. 그래서 '나중에 다시 쓸 만한 것을 기억해 두라' 정도로 목적만 알려 주고, 무엇을 적을지는 AI에게 맡기는 편이 낫습니다. 다만 구형 모델은 '답하기 전에 메모리 파일부터 읽고, 추측은 직접 확인하라'고 시키면 점수가 두 배 가까이 올랐으므로, 오래된 모델을 쓴다면 이런 안내를 붙이는 것이 좋습니다.
