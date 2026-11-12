# Claude Agent SDK로 만든 서비스를 고객에게 제공할 때는 claude.ai 로그인이나 구독 사용량을 연결하지 말고 API 키 인증을 써야 하는데, 사전 승인 없이는 Anthropic이 허용하지 않기 때문이다.

🏛 공식 발표 · Claude Code 공식 문서

Agent SDK로 고객용 에이전트나 서비스를 만들 경우, 사전 승인을 받지 않았다면 고객이 claude.ai 계정으로 로그인하게 하거나 claude.ai 구독 사용량을 쓰게 할 수 없습니다. 인증은 공식 Quickstart에 나온 API 키 방식을 써야 합니다. 그러면 사용료가 API 요금으로 나가므로, 고객 요금을 정하기 전에 API 비용부터 따져 보세요. 고객에게 제공하는 서비스에도 Anthropic 상용 이용약관(Commercial Terms)이 적용됩니다.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-11 · https://code.claude.com/docs/en/agent-sdk/overview
  > Use the API key authentication methods described in the Quickstart instead.
