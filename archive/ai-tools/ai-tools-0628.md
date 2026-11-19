---
id: ai-tools-0628
domain: ai-tools
claim: 클로드 코드 예약 작업으로 업무를 자동으로 돌리고 있다면 v2.1.329로 업데이트한 뒤 /tasks에서 예약 작업이 남아 있는지 확인하고
  빠진 것은 다시 등록해야 한다. 이 버전부터는 이전 버전에서 저장한 예약 작업 대부분을 새로 로그인한 세션에서 다시 예약해야 하기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: most saved by earlier versions need scheduling again
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: Fixed saving a scheduled task erasing the project's other saved tasks
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 예약작업
- 자동화
- 업데이트
- v2.1.329
verified_by: 공식 출처
---
v2.1.329부터는 이전 버전에서 저장한 예약 작업 대부분을 새로 로그인한 세션에서 다시 예약해야 합니다. 원래 세션을 --resume으로 다시 열었을 때만 예전 예약 작업이 그대로 실행됩니다. v2.1.328 이전 버전에는 예약 작업 파일을 읽지 못할 때 작업 하나를 저장하면 그 프로젝트의 다른 예약 작업이 모두 지워지는 문제와, 오타가 있는 예약 작업이 다음 저장 때 삭제되는 문제도 있었습니다. 업데이트한 뒤에는 /tasks에서 매일 돌아야 할 작업이 모두 있는지 확인하고, 빠진 것은 다시 등록하세요.
