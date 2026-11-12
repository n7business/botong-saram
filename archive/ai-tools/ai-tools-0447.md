---
id: ai-tools-0447
domain: ai-tools
claim: 스티커·캐릭터처럼 배경 없는 이미지가 필요하면 AI로 만든 뒤 배경을 따로 지우지 말고, 처음부터 투명 배경으로 생성해야 하는데, OpenAI
  이미지 API에서는 background를 transparent로 두고 png나 webp로 받으면 된다.
status: candidate
evidence: policy
confidence: 0.6
sources:
- url: https://www.gpters.org/news/post/seedream-55-summary-transparent-DrMcx2U64UQAOl4
  author: 강지인
  seen: '2026-11-10'
  quote: 투명 배경이 시드림만의 기능은 아니에요.
  source: 지피터스 GPTers
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 이미지생성
- 투명배경
- 누끼
- openai
---
투명 배경(RGBA)으로 바로 생성하면 따로 배경을 지우는 작업을 하지 않아도 됩니다. 새로 나온 시드림 5.5는 완전 투명과 반투명 이미지를 직접 만든다고 밝혔습니다. 다만 투명 배경은 시드림만의 기능이 아닙니다. OpenAI 이미지 생성 가이드도 background를 transparent로 두고 png나 webp 형식으로 받으라고 안내합니다. jpg처럼 투명도를 지원하지 않는 형식으로 받으면 배경이 채워지니 형식부터 확인하세요.
