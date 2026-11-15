---
id: ai-tools-0580
domain: ai-tools
claim: OpenAI SDK로 만든 앱에 Cloudflare AI Gateway를 붙일 때는 요청 URL, API 키(Cloudflare 토큰으로
  교체), 모델명 앞 제공사 표기, 이 세 줄만 바꾸면 되므로 기존 코드를 크게 고치지 않아도 된다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=f1quywzT-a8
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-16'
  quote: all you have to do to start using it is change three lines of code
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- cloudflare
- ai-gateway
- openai-sdk
- 도입
---
AI Gateway는 OpenAI SDK와 호환되어 접속 주소를 게이트웨이 URL로 바꾸고, OpenAI API 키 자리에 Cloudflare 토큰을 넣고, 모델명 앞에 openai·anthropic 같은 제공사 이름을 붙이면 됩니다. 제공사를 붙이는 것은 Cloudflare가 요청을 어디로 보낼지 알아야 하기 때문입니다. 모델명만 Anthropic 모델로 바꾸면 같은 코드로 Claude도 쓸 수 있고, Google·Azure·Amazon Bedrock·DeepSeek 등도 지원합니다. 요금은 Cloudflare 크레딧을 사서 Cloudflare가 대신 내게 하거나, 대시보드에 내 API 키를 등록해 직접 내는 방식 중 하나를 고릅니다.
