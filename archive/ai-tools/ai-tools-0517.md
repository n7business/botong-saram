---
id: ai-tools-0517
domain: ai-tools
claim: 클로드 코드의 자동 메모리 파일 MEMORY.md는 세션마다 앞부분 200줄(또는 25KB)만 읽히므로, 내용을 그 안에 다 적지 말고
  무엇이 어느 파일에 있는지 알려 주는 목차로만 써야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: It loads only the first 200 lines or 25 KB of MEMORY.md.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- auto-memory
- MEMORY.md
verified_by: 실무자 실측(단일 출처)
mentions: 1
---
클로드 코드는 자동 메모리를 매 세션 모두 불러오지 않고 MEMORY.md의 첫 200줄 또는 25KB까지만 읽습니다. 이보다 뒤에 적은 내용은 세션 시작 때 자동으로 반영되지 않습니다. 그래서 MEMORY.md에는 한 줄짜리 목차와 링크만 두고, 자세한 내용은 따로 파일로 나눠 필요할 때 찾아 읽게 하는 편이 좋습니다. 세션마다 들어가는 메모가 길어질수록 토큰이 들고, 그 안의 틀린 메모가 모든 세션에 따라간다는 점도 함께 기억해야 합니다.
