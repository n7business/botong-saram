---
id: ai-tools-0417
domain: ai-tools
claim: AI가 남기는 업무 메모에는 규칙만 적지 말고 그 규칙이 맞는지 어떻게 알았는지, 확인된 것인지 아직 추측인지, 빠지기 쉬운 함정까지
  함께 적게 해야 다음 작업에서 틀린 추측을 사실로 믿지 않는다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-10'
  quote: began marking which facts it had checked and which were still unconfirmed
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
- 검증
- 업무노트
verified_by: 실무자 실측(단일 출처)
mentions: 1
---
실험에서 메모리를 가장 잘 쓴 모델은 규칙과 함께 그 규칙이 참이라는 근거, 앞선 질문의 답, 발견한 함정에 대한 경고를 남겼습니다. 성능이 낮은 모델의 메모는 검증하지 않은 추측을 여러 파일에 흩어 둔 수준이었습니다. Opus 4.7은 메모를 참고 문서 하나로 모으고 확인한 사실과 아직 확인하지 않은 사실을 나눠 표시하기 시작했습니다. AI에게 업무 노트를 맡길 때도 '확인됨/미확인'과 근거를 함께 적게 하면 다음 세션에서 메모를 믿어도 될지 판단할 수 있습니다.
