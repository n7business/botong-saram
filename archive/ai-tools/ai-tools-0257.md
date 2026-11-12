---
id: ai-tools-0257
domain: ai-tools
claim: 코덱스의 Approve for me 모드는 검토 AI가 내 부탁을 기준으로 판단해 삭제도 묻지 않고 실행할 수 있으므로, 지우기처럼 되돌리기
  어려운 일은 기본 모드에서 직접 읽고 승인해야 한다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=zmpXdQmLeYA
  author: 코드깎는노인
  seen: '2026-11-06'
  quote: 검토하는 AI도 결국 내 부탁을 기준으로 판단하므로
  source: 코드깎는노인
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- codex
- 권한
- 샌드박스
- 삭제
verified_by: 실무자 실측(단일 출처)
---
코덱스 /permissions의 2번 Approve for me는 다른 AI가 먼저 검토해 위험해 보이는 일만 묻는 모드입니다. 영상 실험에서 '홈 폴더의 백업 폴더를 통째로 지워줘'라고 하자 약 6초 검토 후 사용자에게 묻지 않고 지웠습니다. 검토 AI도 내 부탁을 기준으로 판단하므로 이 모드에서는 부탁 자체를 신중하게 해야 합니다. 걱정되면 1번 Ask for approval에서 명령을 직접 읽고 누르는 편이 안전합니다. 화면과 동작은 영상 기준인 codex-cli 0.164.0과 달라질 수 있습니다.
