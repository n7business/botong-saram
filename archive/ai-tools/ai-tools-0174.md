---
id: ai-tools-0174
domain: ai-tools
claim: 잘 돌아가는 프로젝트에 성공 여부가 불확실한 큰 기능을 넣을 때는 AI에게 새 브랜치에서 작업하게 해야, 실패해도 브랜치만 버리면 되고
  원본은 그대로 남는다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=CcRM0IHYriM
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-06'
  quote: 새 브랜치 만들어서 거기서 작업해 줘
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- git
- 브랜치
- 바이브코딩
- claude-code
---
기능을 넣기 전에 Claude Code에 '새 브랜치 만들어서 거기서 작업해 줘'라고 지시합니다. 브랜치는 원본 코드에 영향을 주지 않는 독립된 작업 공간입니다. 파일 10~20개가 한꺼번에 고쳐지다가 몇 개만 잘못되면 커밋으로 되돌리기가 애매하고 토큰 비용도 듭니다. 브랜치에서 작업하면 실패했을 때 통째로 버리면 됩니다. 결과가 마음에 들면 메인에 합칩니다.
