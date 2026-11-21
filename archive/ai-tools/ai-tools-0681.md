---
id: ai-tools-0681
domain: ai-tools
claim: AI 코딩 도구가 자동으로 커밋하게 훅을 걸 때는 파일을 고칠 때마다가 아니라 응답이 끝날 때 한 번만 커밋하게 해야 한다. 화자 실습에서
  파일 수정마다 커밋하게 했더니 요청 2개에 커밋이 6개 생겼고, 열리지도 않는 중간 상태까지 남아 돌아갈 지점을 고르기 어려웠기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 부탁받은 일을 끝내고 대답을 마쳤을 때 한 번만 커밋하는 방법이에요
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
- claude-code
- hook
- git
- 자동화
---
훅은 메시지를 보낼 때, 파일을 고친 직후, 응답이 끝났을 때처럼 정해진 순간에 정해 둔 작업을 자동으로 실행하는 기능입니다. 응답이 끝날 때 한 번만 커밋하게 바꾸자 같은 요청에서 커밋이 2개만 남았습니다. 커밋 메시지에 요청 문장을 그대로 넣으면 나중에 기록을 찾기도 쉽습니다. '작업이 끝날 때마다 자동으로 커밋하는 훅을 설정하고 커밋 메시지에 내 요청을 넣어 줘'라고 말로 부탁하면 됩니다. 설정 파일이 바뀌므로 승인할 때 바뀌는 내용을 읽어 보고, 적용한 뒤에는 클로드 코드를 재시작하세요(/exit 후 claude --continue).
