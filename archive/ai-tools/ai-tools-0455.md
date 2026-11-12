---
id: ai-tools-0455
domain: ai-tools
claim: 클로드에게 정기 작업을 맡길 때 컴퓨터가 꺼져 있어도 돌아야 하면 클라우드 예약 작업을, 내 컴퓨터의 파일과 프로그램이 필요하면 데스크톱
  예약 작업을 골라야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: they keep running even when your computer is off
  source: Claude Code 공식 문서
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 예약작업
- 자동화
- 클라우드
verified_by: 공식 출처
---
클로드 코드의 정기 작업은 두 가지입니다. 클라우드 예약 작업(예전 이름 routines)은 클라우드에서 돌기 때문에 내 컴퓨터가 꺼져 있어도 실행되고, API 호출이나 GitHub 이벤트로 시작할 수도 있습니다. 데스크톱 예약 작업은 내 컴퓨터에서 돌기 때문에 로컬 파일과 프로그램을 바로 쓸 수 있지만, 그 시간에 컴퓨터가 켜져 있어야 합니다. 사무실 PC의 문서를 다루는 작업이라면 데스크톱 예약 작업을 쓰고, 그 PC가 잠자기 상태로 들어가지 않게 설정해 두세요.
