---
id: factory-ax-0322
domain: factory-ax
claim: 이메일·문서 요약처럼 외부 콘텐츠를 읽는 업무를 AI 에이전트에 맡기는 사업자는 콘텐츠 안에 숨은 악의적 지시를 에이전트가 정상 명령으로
  실행할 수 있다는 점을 알고, 보안 통제장치를 두고 최종 답변뿐 아니라 중간 처리 과정까지 살펴야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.kidd.co.kr/news/248256
  author: 산업일보 임지원 기자(포티넷 다니엘 퀑 CISO 발언)
  seen: '2026-11-25'
  quote: 에이전트가 이를 정상적인 명령으로 인식해 수행할 수 있다고 경고했다
  source: 산업일보
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI보안
- 프롬프트인젝션
- AI에이전트
- 이메일
---
외부 콘텐츠로 AI의 행동을 조작하는 공격을 '간접 프롬프트 인젝션'이라고 합니다. 예를 들어 에이전트에 이메일 요약을 시켰는데 그 이메일에 악의적인 지시가 들어 있으면, 통제장치가 없는 에이전트는 그 지시를 정상 명령으로 알고 실행할 수 있습니다. 사용자의 요청과 최종 답변에 이상이 없어 보여도 중간 처리 과정에서 정보가 빠져나갈 수 있습니다. 외부 메일이나 문서를 읽는 에이전트에는 파일 전송, 외부 발송, 결제 같은 실행 권한을 주지 않거나 사람이 승인한 뒤에만 실행되게 하십시오.
