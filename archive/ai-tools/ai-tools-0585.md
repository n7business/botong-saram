---
id: ai-tools-0585
domain: ai-tools
claim: 고객 정보가 AI로 넘어갈 수 있는 서비스라면 AI Gateway에서 Zero data retention을 켜 AI 제공사에 요청·응답을
  보관하지 말라고 알리고, 데이터 유출 방지(DLP) 정책으로 금융 정보 같은 민감 정보가 프롬프트나 응답에 들어가면 표시하거나 차단해야 한다.
status: candidate
evidence: anecdote
confidence: 0.5
sources:
- url: https://www.youtube.com/watch?v=f1quywzT-a8
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-16'
  quote: Zero data retention을 켜면 AI 제공사에 요청·응답 데이터를 보관하지 말라고 알린다.
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
- 개인정보
- dlp
---
Zero data retention을 켜면 게이트웨이가 AI 제공사에 요청·응답 데이터를 보관하지 말라고 전달합니다. Guardrails 아래 DLP를 켜고 정책을 추가하면 금융 정보·사회보장번호 같은 탐지 대상을 고르고, 표시할지 차단할지, 프롬프트와 응답 중 어느 쪽을 검사할지 정할 수 있습니다. 고객이 보내면 안 될 정보를 입력하거나 모델이 그런 정보를 내보낼 때 잡아냅니다. 영상은 미국 사회보장번호를 예로 들었으므로, 한국 주민등록번호·계좌번호가 제대로 탐지되는지는 직접 시험해 본 뒤 믿어야 합니다.
