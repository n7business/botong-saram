---
id: ai-tools-0374
domain: ai-tools
claim: 클로드 코드는 사용자 폴더에서 바로 켜지 말고 작업 폴더를 만들어 들어간 뒤 켜야, 내 파일 전체가 작업 공간이 되는 일을 막을 수 있다.
status: verified
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=xjHR00fV-XQ
  author: 코드깎는노인
  seen: '2026-11-07'
  quote: 꼭 작업 폴더에 들어간 다음 켜세요.
  source: 코드깎는노인
- url: https://www.youtube.com/watch?v=QI2KVJ2ciiY
  author: 테디노트 TeddyNote
  seen: '2026-11-06'
  quote: 얘가 건드렸으면 하는 폴더를 지정해 두는게 매우매우 중요해요.
  source: 테디노트 TeddyNote
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드 코드
- 작업 폴더
- 입문
- 안전
mentions: 2
verified_by: 독립 2곳 weight 1.4
---
Claude Code는 지금 있는 폴더를 작업 공간으로 쓰고, 새 터미널은 늘 사용자 폴더에서 시작합니다. 먼저 'mkdir todo-app'으로 폴더를 만들고 'cd todo-app'으로 들어간 다음 'claude'를 실행합니다. 폴더 신뢰 창에서는 직접 만든 폴더일 때만 Yes를 고르고, 모르는 폴더는 내용부터 확인합니다. 신뢰 창에서 생각 없이 Enter를 치면 No가 선택되어 프로그램이 꺼지는데, 이때는 'claude'를 다시 치면 됩니다.
