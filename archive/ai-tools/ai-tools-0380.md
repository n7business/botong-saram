---
id: ai-tools-0380
domain: ai-tools
claim: AI끼리 서로 검토시키는 적대적 리뷰 결과를 그대로 반영하지 말고, 일어날지 모를 걱정에 대응하느라 검증과 복잡도만 늘어나는 수정은 사람이
  걸러야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/redesigning-source-control
  author: Anthropic Engineering
  seen: '2026-11-09'
  quote: while this is incredibly effective in many ways, it can also be myopic
  source: Anthropic Engineering 블로그
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 교차검증
- 과잉설계
- 코드리뷰
- claude-code
---
Anthropic은 AI가 서로의 작업을 공격적으로 검토하는 적대적 리뷰를 많이 쓰며 효과도 크다고 평가합니다. 다만 이 리뷰는 시야가 좁아서, 가정에 불과한 우려에도 과하게 대응하는 경우가 있습니다. 실제로 한 리뷰가 다른 내부 서비스를 믿지 못하겠다고 지적하자 Claude가 불필요한 검증 코드와 복잡도를 잔뜩 추가했습니다. AI 리뷰가 지적한 사항은 실제로 일어날 수 있는 위험인지 사람이 판단한 뒤에 반영해야 프로그램이 쓸데없이 무거워지지 않습니다.
