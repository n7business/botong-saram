---
id: ai-tools-0165
domain: ai-tools
claim: Claude Code v2.1.317부터 웹·셸 도구가 계정 이메일을 네트워크로 보내기 전에 확인을 요청하므로, 보내는 곳과 이유를 보고
  필요할 때만 승인해야 업무 계정 주소가 불필요하게 외부로 나가지 않는다.
status: merged
evidence: policy
confidence: 0.82
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.317
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Added a check that asks before a web or shell tool call sends your account
    email address to the network
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 개인정보
- 권한
- 이메일
merged_into: ai-tools-0024
---
v2.1.317에는 웹 또는 셸 도구 호출이 계정 이메일 주소를 네트워크로 보내기 전에 묻는 확인 절차가 추가됐다. 이 확인이 뜨면 습관적으로 승인하지 말고 어느 서비스로, 왜 보내는지 먼저 살핀다. 작업에 꼭 필요하지 않으면 승인하지 않는다.
