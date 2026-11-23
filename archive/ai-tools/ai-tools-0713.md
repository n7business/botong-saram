---
id: ai-tools-0713
domain: ai-tools
claim: VS Code에서 클로드 코드 답변의 코드 블록을 복사해 터미널에 붙여 넣는다면 확장 프로그램을 v2.1.330 이상으로 업데이트해야
  합니다. 이전 버전에서는 복사할 때 끝에 줄바꿈이 붙어서 붙여 넣는 순간 명령이 바로 실행됐습니다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-23'
  quote: copying a code block adding a trailing newline that ran the command on paste
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- vscode
- 업데이트
- 안전
verified_by: 공식 출처
---
VS Code용 클로드 코드 확장 프로그램 이전 버전에서는 답변의 코드 블록을 복사하면 끝에 줄바꿈이 함께 복사됐습니다. 그래서 터미널에 붙여 넣기만 해도 Enter를 누른 것처럼 명령이 실행됐습니다. 이 문제는 v2.1.330에서 고쳐졌습니다. 업데이트하기 전에는 텍스트 편집기 같은 곳에 먼저 붙여 넣어 명령 내용을 확인한 뒤 터미널로 옮기세요. 삭제나 배포처럼 되돌리기 어려운 명령은 특히 조심해야 합니다.
