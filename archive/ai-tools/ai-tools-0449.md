---
id: ai-tools-0449
domain: ai-tools
claim: CLAUDE.md처럼 AI가 매 세션 자동으로 읽는 지침 파일은 길게 늘리지 말고 꼭 필요한 내용만 남겨야 하는데, 지침이 길수록 잘
  따르지 않고 그 안의 틀린 메모가 모든 세션에 그대로 따라가기 때문이다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-11'
  quote: longer instruction files reduce adherence
  source: Anthropic Engineering 블로그
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- claude-md
- context-injection
- agent-memory
---
AI가 세션을 시작할 때마다 자동으로 불러오는 지침과 메모는 매번 토큰을 쓰고, 불러온다고 해서 AI가 그대로 따른다는 보장도 없습니다. Anthropic은 클로드 코드 문서에서 지침 파일이 길수록 지키는 정도가 떨어진다고 경고합니다. 이 자리에 틀린 메모가 하나 섞이면 모든 세션이 그 메모를 믿고 시작하게 됩니다. 자세한 내용은 별도 파일로 옮기고 자동으로 읽히는 파일에는 링크만 남겨 짧게 유지하십시오. 자동으로 읽히는 파일에 들어간 내용은 주기적으로 맞는지 다시 확인하십시오.
