---
id: ai-tools-0285
domain: ai-tools
claim: 클로드 코드 예약 작업은 컴퓨터가 꺼져 있어도 돌아가야 하면 클라우드 예약으로, 내 컴퓨터의 파일과 도구가 필요하면 데스크톱 예약으로
  만든다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: run in the cloud, so they keep running even when your computer is off
  source: Claude Code 공식 문서
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: run on your machine, with direct access to your local files and tools
  source: Claude Code 공식 문서
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
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
클라우드 예약 작업은 클라우드에서 실행되므로 컴퓨터를 꺼도 계속 돌아가고, API 호출이나 GitHub 이벤트로 시작할 수도 있습니다. 웹, 데스크톱 앱 또는 CLI의 `/schedule`로 만듭니다. 데스크톱 예약 작업은 내 컴퓨터에서 실행되어 로컬 파일과 도구에 바로 접근합니다. CLI 세션 안에서 잠깐 상태를 반복 확인할 때는 `/loop`를 씁니다.
