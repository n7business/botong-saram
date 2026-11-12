---
id: ai-tools-0105
domain: ai-tools
claim: Claude Code 프로 플랜 사용자는 기본 모델이 Opus로 되어 있으면 토큰이 빨리 바닥나므로, /model로 Sonnet으로 바꾸거나
  작업 폴더의 .claude/settings.json에 "model"을 Sonnet으로 적어 다시 실행해도 Sonnet이 기본으로 유지되게 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=QacldO_VQww
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: Opus가 더 좋은 건 맞지만 Sonnet도 일상적인 작업은 아주 잘한다.
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
- 모델선택
- 토큰절약
- settings.json
---
프로 플랜은 사용량이 적어서 비싼 Opus를 기본으로 쓰면 한도가 금방 소진됩니다. /model을 입력하면 현재 모델이 보이고, 방향키로 Sonnet을 고를 수 있습니다. 매번 바꾸기 번거롭다면 작업 폴더에 .claude/settings.json 파일을 만들고 "model" 값을 Sonnet으로 지정하세요. 그러면 Claude Code를 다시 실행해도 Sonnet이 기본으로 유지됩니다. Opus가 더 뛰어나긴 하지만 일상적인 작업은 Sonnet도 충분히 잘합니다.
