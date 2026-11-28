# 클로드 에이전트 SDK로 고객에게 팔 서비스를 만들 때는 고객이 claude.ai 계정으로 로그인해 내 구독 한도를 쓰게 해서는 안 되고, API 키 인증 방식으로 만들어야 한다. Anthropic이 미리 승인하지 않은 경우 이를 허용하지 않기 때문이다.

🏛 공식 발표 · Claude Code 공식 문서

에이전트 SDK를 쓰면 클로드 코드와 같은 도구와 작업 방식으로 내 서비스용 AI 에이전트를 만들 수 있습니다. 하지만 Anthropic은 사전 승인 없이 외부 개발자가 자기 제품에 claude.ai 로그인이나 claude.ai 사용 한도를 제공하는 것을 허용하지 않습니다. 고객용 서비스는 Quickstart에 안내된 API 키 인증으로 만드세요. 그러면 비용도 API 요금으로 나갑니다. 고객에게 제공하는 서비스에는 Anthropic 상업 이용약관(Commercial Terms of Service)이 적용됩니다.

- 근거 policy · 처음 2026-11-28 · 최근 확인 2026-11-28 · 재검토 2026-12-28 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-28 · https://code.claude.com/docs/en/agent-sdk/overview
  > Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products
