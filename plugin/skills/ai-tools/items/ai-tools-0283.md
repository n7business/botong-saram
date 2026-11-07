# Claude Agent SDK로 만든 제품을 남에게 제공할 때는 사전 승인 없이 claude.ai 로그인이나 사용 한도를 쓰게 하면 안 되며, API 키 인증을 써야 한다.

🏛 공식 발표 · Claude Code 공식 문서

Anthropic은 사전 승인을 받지 않은 서드파티 개발자가 자기 제품에서 claude.ai 로그인이나 사용 한도를 제공하는 것을 허용하지 않습니다. Agent SDK로 만든 에이전트도 여기에 포함됩니다. 대신 Quickstart 문서에 나온 API 키 인증 방식을 사용해야 합니다. 고객과 최종 사용자에게 제공하는 제품에 SDK를 쓰는 경우에도 Anthropic의 Commercial Terms of Service가 적용되니 출시 전에 확인합니다.

- 근거 policy · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/agent-sdk/overview
  > Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/agent-sdk/overview
  > including when you use it to power products and services that you make available to your own customers and end users
