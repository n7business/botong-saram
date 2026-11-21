---
id: ai-tools-0678
domain: ai-tools
claim: AI 코딩 도구에게 예전 상태로 되돌려 달라고 하기 전에는 먼저 '현재 상태부터 커밋해 줘'라고 시켜야 한다. 프로젝트 전체를 이전 커밋으로
  되돌리면 그 뒤의 작업이 폴더에서 사라질 수 있고, 커밋하지 않은 작업은 복구할 방법이 없기 때문이다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 커밋하지 않은 작업은 복구할 방법이 없습니다.
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
- git
- 바이브코딩
- 되돌리기
- 백업
---
Git으로 되돌리는 방법은 두 가지입니다. 문제가 된 커밋 하나만 취소하면 '취소했다'는 새 커밋이 추가되고 그 뒤 작업은 그대로 남습니다. 프로젝트 전체를 이전 커밋 상태로 되돌리면 그 뒤 작업이 폴더에서 사라질 수 있습니다. 커밋해 둔 작업은 에이전트에게 부탁하면 번거롭더라도 복구할 수 있지만, 커밋하지 않은 작업은 되살릴 방법이 없습니다. 그러니 되돌리기 전에는 항상 현재 상태부터 커밋하게 하세요.
