---
id: ai-tools-0839
domain: ai-tools
claim: 지메일·캘린더를 내 대시보드에 연결하려고 발급받은 구글 OAuth 토큰이 테스트용이라면 약 7일 뒤 만료되므로, 계속 쓸 생각이면 영구적으로
  쓸 수 있게 설정을 바꿔 달라고 따로 요청해야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=mYCdZJIT9Ks
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-28'
  quote: 지금 발급받은 토큰은 테스터 계정이라서 아마 7일 뒤에 만료가 됩니다
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- google-oauth
- gmail-api
- 토큰만료
- 에이전트
---
Google Cloud Console에서 Gmail API를 켜고 OAuth 출입증을 처음 발급받으면 보통 테스터 계정용으로 만들어집니다. 화자에 따르면 이 토큰은 약 7일 뒤 만료되고, 만료되면 새 토큰을 다시 연결해야 합니다. 에이전트를 매일 쓸 생각이라면 처음 만들 때 영구적으로 쓸 수 있게 업데이트해 달라고 AI에게 꼭 요청해야 합니다. 그래야 일주일 뒤에 갑자기 연결이 끊기는 일을 막을 수 있습니다.
