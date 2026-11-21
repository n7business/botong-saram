---
id: ai-tools-0680
domain: ai-tools
claim: AI로 만든 프로젝트를 GitHub에 올릴 때는 처음부터 에이전트에게 '비밀 키가 든 파일은 커밋도 업로드도 하지 말라'고 시켜 .gitignore에
  넣게 해야 한다. GitHub의 비밀 키 차단 기능은 기본적으로 공개 저장소에서만 동작하고 무료 개인 계정의 비공개 저장소에서는 막아 주지 않기
  때문이다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 한 번 커밋되면 나중에 파일에서 지워도 옛 커밋에 남고
  source: 코드깎는노인
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- github
- 보안
- api-key
- gitignore
---
API 키가 새어 나가면 다른 사람이 내 계정으로 유료 서비스를 쓸 수 있습니다. 한 번 커밋한 키는 나중에 파일에서 지워도 예전 커밋에 남고, 푸시하면 그 예전 커밋까지 함께 올라갑니다. 그래서 작업을 시작할 때 비밀 키 파일은 커밋하지도 올리지도 말라고 에이전트에게 말해 두세요. 이미 올라갔다면 파일을 지우는 것으로는 부족합니다. 키를 발급한 서비스에서 그 키를 폐기하고 새로 발급받아야 합니다.
