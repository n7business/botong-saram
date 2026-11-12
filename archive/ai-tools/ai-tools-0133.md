---
id: ai-tools-0133
domain: ai-tools
claim: Claude Code에 바로 '만들어 줘'라고 시키지 말고 플랜 모드(Shift+Tab 두 번)에서 탐색→계획을 먼저 받아 충분히 고친
  뒤 구현시켜야, 구현 후 수정하느라 토큰이 더 드는 것을 막는다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=QacldO_VQww
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 구현하기 전에 이러한 계획을 충분히 수정하셔야 돼요.
  source: 짐코딩 (@gymcoding)
- url: https://yozm.wishket.com/magazine/detail/3988/
  author: 네네군
  seen: '2026-11-03'
  quote: 바로 개발을 진행하지 말고, 우선은 Plan Mode로 전환하여 상세한 계획 수립
  source: 요즘IT
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
- 플랜모드
- 토큰절약
mentions: 2
---
검증된 순서는 탐색(자료 모으기) → 계획 → 구현입니다. 탐색과 계획 단계에서는 Shift+Tab을 두 번 정도 눌러 플랜 모드를 켭니다. 요청이 간단하면 플랜 모드에서도 계획 없이 바로 실행될 수 있으니, 프롬프트 끝을 '계획해 줘'로 마무리합니다. 나온 계획은 꼼꼼히 읽고 마음에 들 때까지 수정을 요청하세요. 계획 없이 만든 뒤에 고치면 토큰이 더 많이 듭니다.
