---
id: ai-tools-0108
domain: ai-tools
claim: Claude Code로 코드를 다룰 때 Serena MCP 플러그인을 붙이면 글자 단위 검색 대신 코드 의미 단위로 찾아 불필요한 탐색
  토큰이 줄어들며, 연결이 failed로 뜨면 파이썬 패키지 매니저 uv를 설치한 뒤 /mcp에서 Reconnect한다.
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=L94yAQR9VvA
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 명시적으로 MCP를 한번 대화해서 언급을 해 주세요.
  source: 짐코딩 (@gymcoding)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- mcp
- serena
- 토큰절약
---
Serena가 없으면 Claude는 '로그인' 같은 단어를 글자 기준으로 검색해 변수명·주석·문자열까지 모두 뒤집니다. 그렇게 쓴 토큰은 대화가 이어지는 동안 컨텍스트에 남아 계속 비용이 쌓입니다. Serena는 IDE의 '정의로 이동'처럼 의미를 이해하고 검색하기 때문에 코드 위치 파악이나 이름 일괄 변경(rename)에서 탐색량이 줄어듭니다. /plugin에서 serena를 검색해 설치하세요. MCP가 failed로 뜨면 'uv install'을 검색해 내 OS에 맞게 uv를 설치하고 /mcp에서 Serena를 Reconnect합니다. 말로 요청했는데 MCP가 동작하지 않으면 대화에서 'Serena'라는 이름을 직접 언급하세요.
