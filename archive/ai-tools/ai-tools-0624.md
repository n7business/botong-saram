---
id: ai-tools-0624
domain: ai-tools
claim: AI에게 결과물을 채점하게 할 때는 '10점 만점에 몇 점'처럼 종합 점수를 받지 말고, '고객 이름을 정확히 썼나', '없는 할인을
  약속했나'처럼 예/아니오로 답할 수 있는 좁은 항목 여러 개로 나눠 묻고, 애매한 경우는 무엇이 해당하지 않는지까지 미리 적어 두어야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/building-strong-safety-evaluations
  author: Anthropic
  seen: '2026-11-20'
  quote: Make criteria atomic and binary.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- LLM채점
- 체크리스트
- 품질검수
---
종합 점수 하나로 물으면 채점 AI가 그때그때 다르게 판단하고, 점수가 낮을 때 어디가 문제인지도 알기 어렵습니다. 기준을 작고 분명한 예/아니오 질문으로 쪼개면 판정이 덜 흔들리고, 어느 항목이 결과를 끌어내렸는지 바로 보입니다. 경계에 걸리는 경우(예: 주의 문구를 붙였으면 괜찮은가)는 채점 AI의 재량에 맡기지 말고 기준에 직접 적어 두세요. 경고나 면책 문구를 덧붙였다고 잘못된 내용이 괜찮아지는 것은 아니므로, 겉 포장이 아니라 내용을 보고 판정하라고도 적어 두어야 합니다.
