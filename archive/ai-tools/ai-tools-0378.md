---
id: ai-tools-0378
domain: ai-tools
claim: 테디노트판 Agent Chat UI로 챗봇을 정식 배포할 때는 make dev로 띄운 서버를 내리고 make run으로 프로덕션 빌드를
  해야, 왼쪽 디버그 메뉴가 빠진 화면으로 서비스할 수 있다.
status: candidate
evidence: anecdote
confidence: 0.5
sources:
- url: https://www.youtube.com/watch?v=DMQXpZXdNJ8
  author: 테디노트 TeddyNote
  seen: '2026-11-07'
  quote: 메이크 런으로 주시면은 프로덕션 모드로 서비스가 실행이 됩니다.
  source: 테디노트 TeddyNote
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗봇
- LangGraph
- 배포
---
이 리포지토리는 make dev를 실행하면 개발자 모드로, make run을 실행하면 프로덕션 모드로 뜹니다. 화자는 프런트엔드에서 수정할 부분을 다 검토한 뒤, dev로 띄운 서버를 내리고 프로덕션 빌드를 하라고 안내합니다. 프로덕션 빌드에서는 왼쪽 디버그 메뉴가 사라집니다. 이 안내는 영상에서 소개한 커스텀 리포지토리에 해당하는 내용이며, 2025년 11월 영상 기준입니다.
