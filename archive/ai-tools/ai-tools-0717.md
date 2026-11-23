---
id: ai-tools-0717
domain: ai-tools
claim: 크롬이 열려 있고 로그인도 돼 있는데 Claude in Chrome이 계속 '연결 안 됨'으로 나온다면 확장 프로그램을 다시 설치하기
  전에 클로드 코드를 v2.1.330 이상으로 업데이트해야 합니다. 이전 버전에서는 잠깐 연결이 끊긴 뒤 다시 연결되지 않는 문제가 있었습니다.
status: verified
evidence: policy
confidence: 0.7
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-23'
  quote: Claude in Chrome staying "not connected" after a brief connection problem
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
- chrome
- 업데이트
verified_by: 공식 출처
---
클로드 코드에서 Claude in Chrome으로 브라우저를 조작할 때, 이전 버전에서는 잠깐 연결이 끊기면 그 뒤로 계속 'not connected' 상태에 머무는 문제가 있었습니다. 크롬이 열려 있고 로그인돼 있어도 마찬가지였습니다. 이 문제는 v2.1.330에서 고쳐졌습니다. 확장 프로그램을 지우고 다시 설치하거나 로그인을 다시 하기 전에 클로드 코드 버전부터 확인하세요.
