---
id: ai-tools-0490
domain: ai-tools
claim: 밖에서 폰으로 사무실 컴퓨터의 클로드 코드 세션을 이어 하려면 Remote Control을, 텔레그램·디스코드 메시지나 웹훅을 세션에
  바로 들여보내려면 Channels를 골라야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-12'
  quote: Push events from Telegram, Discord, iMessage, or my own webhooks into a session
  source: Claude Code 공식 문서
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- remote-control
- channels
- 텔레그램
- 원격
verified_by: 공식 출처
---
클로드 코드 공식 문서는 기기를 옮겨 다니며 일하는 방법을 목적별로 나눠 안내합니다. 내 컴퓨터에서 돌고 있는 세션을 폰이나 다른 기기에서 이어 하는 일은 Remote Control로 합니다. 텔레그램·디스코드·아이메시지나 내가 만든 웹훅의 이벤트를 세션 안으로 보내는 일은 Channels로 합니다. 작업을 클라우드에서 계속 돌리다가 모바일로 확인하려면 claude --cloud로 시작한 뒤 클로드 모바일 앱을 쓰면 됩니다.
