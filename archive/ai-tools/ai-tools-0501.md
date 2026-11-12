---
id: ai-tools-0501
domain: ai-tools
claim: AI 에이전트가 고친 결과를 받으면 수정한 파일이 몇 개인지보다 그 수정이 이번에 요청한 범위 안에 있는지를 확인하고, 나중에 하려고
  준비해 둔 기능까지 만들어 넣었다면 되돌려야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://yozm.wishket.com/magazine/detail/4036/
  author: 김동혁
  seen: '2026-11-12'
  quote: AI가 많은 파일을 수정했는지보다, 그 수정이 이번에 필요한 것이었는지를 확인해야 했습니다.
  source: 요즘IT
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 바이브코딩
- 작업범위
- 코드검토
- 에이전트
---
에이전트는 프로젝트 전체를 읽으므로 나중에 하려고 일부만 만들어 둔 코드를 보면 이번 작업에 넣어 완성해 버리기도 합니다. 기능이 늘었다고 그대로 받아들이면 이번에 할 일과 나중에 할 일이 섞여 검토와 관리가 어려워집니다. 결과를 받으면 요청하지 않은 변경이 있는지 먼저 보고, 범위 밖 변경은 되돌리세요. AI가 읽을 수 있는 범위와 이번에 맡긴 일은 다르다는 점을 기억해야 합니다.
