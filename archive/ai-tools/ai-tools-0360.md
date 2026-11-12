---
id: ai-tools-0360
domain: ai-tools
claim: 클로드 코드 프로젝트가 커지면 규칙을 루트 CLAUDE.md에 몰아넣지 말고 폴더별 하위 CLAUDE.md로 나눠야, 지금 작업하는 폴더의
  규칙만 읽혀 더 정확하게 동작한다.
status: merged
evidence: anecdote
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=G1JxVbTmCEc
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 필요할 때만 읽는다. 그게 전부입니다.
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
- 컨텍스트
- 메모리
merged_into: ai-tools-0364
---
루트 CLAUDE.md는 시작하자마자 읽히고, 하위 폴더(예: src/api)의 CLAUDE.md는 그 폴더 파일을 작업할 때 자동으로 읽힙니다. frontend, backend, core처럼 폴더별로 규칙을 나누면 '공통 규칙 + 현재 폴더 규칙'만 읽힙니다. 규칙을 줄이는 것이 아니라 지금 필요한 규칙만 보이게 하는 방법입니다. 오픈소스 Umbraco CMS는 CLAUDE.md 23개를 두고, core 작업 때는 루트와 core 파일만 읽히게 합니다. 이 영상은 프로젝트가 클수록 중요한 전략이라고 설명합니다.
