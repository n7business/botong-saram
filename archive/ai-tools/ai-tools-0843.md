---
id: ai-tools-0843
domain: ai-tools
claim: 지메일 데이터를 내가 만든 대시보드에서 실시간으로 쓰려면 Claude 데스크톱 커넥터(MCP)에 기대지 말고 구글 API를 OAuth로
  대시보드에 직접 연결해야 한다. 커넥터를 쓰면 데이터가 Claude 앱을 거쳐 돌아와야 해서 바로 반영되지 않고 시간이 더 걸린다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=mYCdZJIT9Ks
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-28'
  quote: Claude 데스크톱의 커넥터(MCP)는 외부 대시보드에서 쓰기엔 제한이 있다.
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
- mcp
- 커넥터
- google-api
- oauth
- 대시보드
---
Claude에 지메일 커넥터를 붙이면 채팅에서 답장을 쓸 수는 있습니다. 하지만 화자에 따르면 그 커넥터를 외부 대시보드에서 쓰기에는 제한이 있습니다. 데이터가 Claude 앱을 거쳐 돌아와야 해서 실시간 자동 반영이 어렵기 때문입니다. 그래서 Google Cloud Console에서 Gmail API를 켜고 OAuth 출입증을 발급받아 대시보드에 직접 연결했습니다. 같은 출입증으로 구글 캘린더도 바로 연동할 수 있습니다.
