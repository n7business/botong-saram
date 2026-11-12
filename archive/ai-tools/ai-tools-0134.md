---
id: ai-tools-0134
domain: ai-tools
claim: CLAUDE.md가 갈수록 비대해지지 않게 claude-md-management 플러그인을 깔고, 작업이 끝나 세션을 닫기 전에는 revise-claude-md를,
  주기적으로는 claude-md-improver를 돌린다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=L94yAQR9VvA
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 회의 끝나고 작성하는 회의록이라고 보시면 돼요.
  source: 짐코딩 (@gymcoding)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- 플러그인
- 토큰절약
---
CLAUDE.md는 프롬프트를 보낼 때마다 자동으로 함께 들어가는 프로젝트 규칙 파일이라, 규칙이 쌓여 커지면 매번 토큰이 더 듭니다. revise-claude-md는 회의를 마치고 쓰는 회의록처럼, 세션을 닫기 전에 이번 대화에서 새로 알게 된 명령어·작업 방식·함정을 한 줄씩 뽑아 추가할 후보로 보여 줍니다. 남길 내용이 없으면 추가할 것이 없다고 알려 줍니다. claude-md-improver는 프로젝트 안의 모든 CLAUDE.md를 6가지 기준으로 채점해, 잘 안 먹히는 명령어나 빠진 의존성·환경 설정을 찾아 줍니다.
