---
id: ai-tools-0643
domain: ai-tools
claim: 업무 흐름 전체를 AI 코딩 도구 하나에 맡기고 있다면, 클로드 코드와 코덱스처럼 두 도구가 같은 규칙 파일과 스킬을 읽게 맞춰 두어야
  한다. 한 서비스에 장애가 나면 열어 둔 세션이 모두 멈추기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4043/
  author: 곰씨네 IT 블로그
  seen: '2026-11-20'
  quote: 9월 초 클로드 서비스에 장애 가 발생하면서 반나절 동안 열어 둔 세션이 모두 멈춘 일이 발생했습니다.
  source: 요즘IT
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 코덱스
- 장애대비
- AGENTS.md
- 이중화
---
화자는 9월 초 클로드 서비스 장애로 열어 둔 세션 열 개 가까이가 반나절 동안 모두 멈추는 일을 겪었습니다. 그 뒤 오픈AI 코덱스를 추가하고, 어느 도구에서 작업하든 같은 절차를 따르게 했습니다. 방법은 이렇습니다. 클로드 코드가 읽는 CLAUDE.md 맨 위에 @AGENTS.md를 넣어 코덱스용 AGENTS.md와 같은 규칙을 쓰게 합니다. 스킬 원본은 .agents/skills 폴더 한 곳에 두고 동기화 스크립트로 다른 폴더에 반영합니다. 이렇게 해 두자 클로드로 하던 작업을 코덱스가 인계 문서를 읽고 이어받을 수 있었습니다.
