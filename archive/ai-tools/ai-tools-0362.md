---
id: ai-tools-0362
domain: ai-tools
claim: CLAUDE.md에서 맥락만 알려 줄 파일은 경로만 적고 꼭 읽어야 하는 파일은 경로 앞에 @를 붙여야, 시작할 때 불러올 내용을 구분할
  수 있다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=G1JxVbTmCEc
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 경로 앞에 @를 붙이면 Claude Code를 시작할 때 그 파일 내용을 통째로 불러오고
  source: 짐코딩 (@gymcoding)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- 메모리
- import
---
메모리 파일에 경로만 적으면 그런 파일이 있다는 맥락만 전달되고, 실행할 때 그 내용을 메모리에 올리지 않습니다. 경로 앞에 @를 붙이면 Claude Code를 시작할 때 파일 내용을 통째로 불러옵니다. 실제로 불러왔는지는 /memory 명령어로 확인합니다. @로 참조한 파일은 시작할 때 전부 읽히므로 꼭 필요한 파일에만 붙입니다.
