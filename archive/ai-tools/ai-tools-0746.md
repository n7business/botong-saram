---
id: ai-tools-0746
domain: ai-tools
claim: 클로드 코드의 MEMORY.md는 세부 내용을 담는 곳이 아니라 '무엇을 알고 어디에 있는지'를 보여 주는 짧은 목차로 유지해야 한다.
  매 세션에는 앞쪽 200줄 또는 25KB까지만 불러오고, 지침 파일이 길수록 AI가 지침을 덜 따르기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: It loads only the first 200 lines or 25 KB of MEMORY.md.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2026-12-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- MEMORY.md
- auto-memory
- 지침파일
verified_by: 공식 출처
---
클로드 코드의 자동 메모리는 세션마다 MEMORY.md의 앞쪽 200줄 또는 25KB까지만 불러옵니다. 그 뒤에 적은 내용은 자동으로 읽히지 않습니다. Anthropic 문서도 지침 파일이 길어질수록 AI가 지침을 덜 지킨다고 경고합니다. 또 맨 위에 적어 둔 메모리는 매 세션에 들어가므로, 거기 틀린 메모가 있으면 모든 작업에 그 오류가 따라갑니다. 그래서 MEMORY.md에는 한 줄짜리 항목과 세부 파일 링크만 두고, 자세한 내용은 따로 파일로 내려 두는 것이 좋습니다.
