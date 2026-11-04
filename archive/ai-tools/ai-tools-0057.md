---
id: ai-tools-0057
domain: ai-tools
claim: ChatGPT 프로 API 크레딧은 API 호출 비용에만 쓰이고 ChatGPT 화면이나 로그인형 코덱스의 사용 한도는 늘려 주지 않으며,
  다 쓰면 요청이 429 오류로 실패하므로 그때는 유료 크레딧 구매나 자동 충전을 설정한다.
status: candidate
evidence: policy
confidence: 0.85
sources:
- url: https://www.gpters.org/news/post/how-get-chatgpt-pro-aS69qZQrCJkw6ne
  author: 지피터스_강지인
  seen: '2026-11-03'
  quote: 다 쓰고 남은 크레딧이 없으면 요청이 429 오류와 credit_balance_exhausted 코드로 실패해요.
  source: 지피터스 GPTers
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- ChatGPT
- OpenAI
- API크레딧
- Codex
- 오류대응
---
크레딧은 Responses·Chat Completions·에이전트·이미지·실시간 API 등 API 사용 요금과 기본 도구·저장 요금에 적용된다. ChatGPT 채팅 한도와 로그인해서 쓰는 코덱스 한도는 늘어나지 않고, API 키로 쓰는 코덱스에는 적용되지 않는다. 요청 속도·토큰 속도·모델 제한도 그대로다. 결제 수단을 따로 등록하지 않아도 크레딧을 쓸 수 있고, 프로모션 크레딧이 구매 크레딧보다 먼저 차감된다. 잔액이 0이 되면 요청이 429 오류와 credit_balance_exhausted 코드로 실패하므로 유료 크레딧을 사거나 자동 충전을 켜야 계속 쓸 수 있다. 크레딧이 있는데도 실패하면 크레딧 한도·지출 한도·속도 제한이 서로 다른 한도임을 기억하고 선택한 조직·프로젝트와 잔액·만료일을 먼저 확인한다.
