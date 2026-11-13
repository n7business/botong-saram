---
id: ai-tools-0419
domain: ai-tools
claim: 클로드 코드 자동 모드에서 '이 세션은 무료 분류기 요청 대상이 아니다'라는 안내가 뜨면 중간에 낀 LLM 게이트웨이나 프록시가 원인인
  경우가 많고, Enter로 계속하면 분류기 요청이 토큰 사용량으로 과금되므로 /status의 Auto mode server 항목부터 확인해야 한다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/auto-mode-classifier-billing
  author: Anthropic
  seen: '2026-11-10'
  quote: On a Pro, Max, Ultra, or Team plan, you never see the notice.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-10'
last_confirmed: '2026-11-11'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 자동모드
- 요금
- 게이트웨이
- status
verified_by: 공식 출처
merged_into: ai-tools-0552
---
자동 모드에서는 셸 명령이나 네트워크 요청을 실행하기 전에 분류기가 검사합니다. 서버 쪽 검사가 켜져 있으면 이 검사는 무료입니다. 이 안내가 떴다는 것은 서버 검사가 세션에 닿지 못해 클로드 코드가 직접 분류기 요청을 보내고 있고, 그 요청이 토큰 사용량으로 잡힌다는 뜻입니다. Pro·Max·Ultra·Team 요금제에서는 이 안내가 뜨지 않습니다. 안내가 뜨면 /status를 실행해 Auto mode server 항목이 Enabled인지 Disabled인지 확인하세요. 회사 게이트웨이를 쓰고 있다면 관리자에게 anthropic-beta 헤더와 safeguards 필드를 바꾸지 말고 그대로 넘기도록 요청해야 합니다.
