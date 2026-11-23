---
id: ai-tools-0716
domain: ai-tools
claim: 건너뛴 클로드 코드 예약 작업을 다시 돌리려면 실행 중인 세션 안에서 /resume을 입력하지 말고, 클로드 코드를 --resume 옵션으로
  새로 시작해야 합니다. 세션 안에서 /resume을 입력해서는 그 작업이 실행되지 않습니다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-23'
  quote: '`/resume` inside a running session doesn''t run the task'
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
- 예약작업
- resume
verified_by: 공식 출처
---
컴퓨터가 꺼져 있었거나 세션이 닫혀 있어서 예약 작업을 건너뛰면 클로드 코드가 안내 문구를 보여 줍니다. v2.1.330부터 이 안내는 클로드 코드를 --resume으로 시작하라고 알려 줍니다. 이미 열려 있는 세션에서 /resume을 입력해서는 건너뛴 작업이 실행되지 않기 때문입니다. 그러니 터미널에서 claude --resume으로 새로 시작해 건너뛴 작업을 실행하세요. 컴퓨터가 꺼져 있어도 돌아야 하는 작업이라면 처음부터 클라우드 예약 작업으로 옮기는 편이 낫습니다.
