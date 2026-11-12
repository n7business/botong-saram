---
id: ai-tools-0456
domain: ai-tools
claim: Claude Agent SDK로 만든 서비스를 고객에게 제공할 때는 claude.ai 로그인이나 구독 사용량을 연결하지 말고 API 키
  인증을 써야 하는데, 사전 승인 없이는 Anthropic이 허용하지 않기 때문이다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/agent-sdk/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: Use the API key authentication methods described in the Quickstart instead.
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
- AgentSDK
- 약관
- API키
- 서비스개발
verified_by: 공식 출처
---
Agent SDK로 고객용 에이전트나 서비스를 만들 경우, 사전 승인을 받지 않았다면 고객이 claude.ai 계정으로 로그인하게 하거나 claude.ai 구독 사용량을 쓰게 할 수 없습니다. 인증은 공식 Quickstart에 나온 API 키 방식을 써야 합니다. 그러면 사용료가 API 요금으로 나가므로, 고객 요금을 정하기 전에 API 비용부터 따져 보세요. 고객에게 제공하는 서비스에도 Anthropic 상용 이용약관(Commercial Terms)이 적용됩니다.
