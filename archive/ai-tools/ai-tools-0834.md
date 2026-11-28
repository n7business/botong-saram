---
id: ai-tools-0834
domain: ai-tools
claim: 클로드에게 반복 작업을 예약해 맡길 때는, 컴퓨터가 꺼져 있어도 돌아가야 하는 일은 클라우드 예약 작업으로, 내 컴퓨터의 파일이나 프로그램을
  써야 하는 일은 데스크톱 예약 작업으로 만들어야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-28'
  quote: they keep running even when your computer is off
  source: Claude Code 공식 문서
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2026-12-28'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 예약작업
- 자동화
verified_by: 공식 출처
---
클로드 코드의 예약 작업은 세 가지입니다. 클라우드 예약 작업(예전 이름 routines)은 클라우드에서 실행되므로 컴퓨터를 꺼 둬도 돌아갑니다. API 호출이나 GitHub 이벤트가 생길 때 실행되게 할 수도 있습니다. 데스크톱 예약 작업은 내 컴퓨터에서 실행되므로 컴퓨터 안의 파일과 도구를 바로 쓸 수 있습니다. 대신 컴퓨터가 켜져 있어야 합니다. /loop는 열어 둔 CLI 대화 안에서 같은 지시를 짧은 간격으로 반복할 때만 씁니다.
