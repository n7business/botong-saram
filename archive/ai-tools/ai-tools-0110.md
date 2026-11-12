---
id: ai-tools-0110
domain: ai-tools
claim: Claude Code로 에이전트를 여러 개 만들 때는 회사 일·영상 편집·출판처럼 기능별로 디렉토리를 따로 만들어야 각 에이전트에만 적용할
  지침(CLAUDE.md)이 섞이지 않는다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=yh05xGAUyRc
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-03'
  quote: 한 디렉토리에 여러 에이전트를 만들면 각 에이전트에만 적용할 지침을 독립시킬 수 없기 때문이다.
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
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
- 에이전트설계
- 디렉토리
- CLAUDE.md
---
에이전트는 실행한 폴더의 CLAUDE.md를 가장 먼저 읽기 때문에, 한 폴더에 여러 에이전트를 몰아 두면 에이전트별 지침을 따로 둘 수 없습니다. 바탕화면 등에 Claude Code용 상위 폴더를 하나 만들고 그 아래에 기능별 하위 폴더를 둡니다. 새 에이전트를 만들 때마다 새 하위 폴더에서 시작합니다. 에이전트가 많아지면 세션도 늘어나지만, 처음에는 한두 개로 가볍게 시작하면 됩니다.
