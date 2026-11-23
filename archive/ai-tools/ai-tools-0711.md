---
id: ai-tools-0711
domain: ai-tools
claim: 클로드 코드로 반복 업무를 예약할 때, 컴퓨터를 꺼 둔 시간에도 돌아야 하는 작업은 클라우드 예약 작업으로, 내 컴퓨터의 파일이나 프로그램을
  써야 하는 작업은 데스크톱 예약 작업으로 등록해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-23'
  quote: they keep running even when your computer is off
  source: Claude Code 공식 문서
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
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
클로드 코드의 예약 방식은 세 가지입니다. 클라우드 예약 작업(이전 이름 routines)은 클라우드에서 돌아가서 컴퓨터가 꺼져 있어도 실행됩니다. API 호출이나 깃허브 이벤트로 실행되게 할 수도 있고, 웹·데스크톱 앱이나 CLI의 /schedule로 만듭니다. 데스크톱 예약 작업은 내 컴퓨터에서 돌아가서 로컬 파일과 도구에 바로 접근할 수 있지만, 그만큼 컴퓨터가 켜져 있어야 합니다. /loop는 CLI 세션 안에서 같은 지시를 잠깐 반복하는 용도라 장기 예약용으로는 맞지 않습니다.
