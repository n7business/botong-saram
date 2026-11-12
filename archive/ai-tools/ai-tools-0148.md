---
id: ai-tools-0148
domain: ai-tools
claim: A2A 공식 SDK의 태스크 저장소 기본값은 파드 메모리라서 재시작하면 맡겨 둔 일의 상태가 사라지므로, 재시작해도 남는 저장소로 바꿔야
  한다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 태스크 저장소는 기본값이 파드 메모리라 재시작하면 상태가 사라지니
  source: 요즘IT
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2026-12-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- A2A
- 에이전트 운영
- 태스크 저장소
verified_by: 실무자 실측(단일 출처)
---
SDK 기본값인 InMemoryTaskStore는 태스크를 파드 메모리에 담습니다. 백엔드를 재시작하면 맡겨 둔 일의 상태가 함께 사라집니다. 처음 띄워 볼 때는 눈에 띄지 않을 수 있으니 운영 전에 저장소부터 바꿉니다. 바꾼 뒤에는 진행 중인 태스크를 둔 채 서버를 재시작해 상태가 남는지 확인합니다.
