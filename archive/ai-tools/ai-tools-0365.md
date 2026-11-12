---
id: ai-tools-0365
domain: ai-tools
claim: CLAUDE.md에 테스트·CSS·API처럼 파일 종류별 규칙이 섞여 있다면 .claude/rules의 주제별 파일로 옮기고 적용 경로를
  지정해야, 관계없는 작업에 그 규칙이 로드되지 않는다.
status: merged
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=FBv8hK_DtJ8
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 각 파일 맨 위에 조건을 설정할 수 있습니다.
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
- rules
- 프론트매터
- 컨텍스트
merged_into: ai-tools-0363
---
먼저 CLAUDE.md를 열어 '테스트는 이렇게', 'CSS는 이렇게', 'API는 이런 형식으로' 같은 규칙이 섞여 있는지 확인합니다. 있다면 .claude/rules 디렉터리에 주제별 파일로 옮깁니다. 각 파일 맨 위에 대시 세 개(---)로 감싼 프론트매터를 두고 적용할 경로 패턴을 적습니다. 예를 들어 src/api 하위의 TypeScript 파일을 지정하면 그 규칙은 해당 파일에만 적용됩니다. 그러면 결제 API 작업 때는 코드 스타일과 API 디자인 규칙만 로드됩니다.
