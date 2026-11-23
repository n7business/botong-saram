---
id: ai-tools-0723
domain: ai-tools
claim: AI 영상에서 손동작처럼 자주 망가지는 장면이 있다면 전체 영상을 계속 다시 만들지 말고, 그 몇 초만 괜찮게 나올 때까지 따로 만든
  뒤 그 클립을 전체 영상의 레퍼런스로 붙여 그대로 따라 하게 해야 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=p5Fj3dWSSmU
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-23'
  quote: AI models still struggle a lot with hands.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI영상
- 손
- 레퍼런스
- 비용절감
---
AI 영상 모델은 아직 손을 많이 어려워합니다. 포장지를 찢거나 리본을 당기는 장면은 초안 대부분이 이상하게 나왔습니다. 그래서 어려운 구간(예: 첫 5초)만 반복 생성해 괜찮은 클립을 하나 얻습니다. 그다음 그 클립을 레퍼런스로 첨부하고 프롬프트에 '오프닝은 이 클립을 그대로 따라 하라'고 적습니다. 이렇게 하면 나머지 부분을 고칠 때도 어려운 부분은 이미 해결된 상태라, 손이 망가진 전체 영상에 크레딧을 낭비하지 않습니다.
