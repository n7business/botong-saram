---
id: ai-tools-0379
domain: ai-tools
claim: AI에게 코드를 맡길 때 사람은 시스템의 핵심 제약과 설계 판단을 쥐고 있다가, AI가 그 제약을 어기는 방식으로 문제를 풀면 '안 된다'고
  막아야 한다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/redesigning-source-control
  author: Anthropic Engineering
  seen: '2026-11-09'
  quote: Very often, we found that the role of the engineers was to tell Claude “no.”
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
- claude-code
- 코드리뷰
- 사람의역할
- 설계
---
Anthropic 엔지니어들은 Claude가 자신들보다 코드를 더 잘 쓴다고 평가하면서도, 엔지니어가 맡는 일의 상당 부분이 Claude에게 '안 된다'고 말하는 것이었다고 밝혔습니다. 에이전트는 애초에 허용하지 말았어야 할 패턴을 맞추려고 시스템의 핵심 제약을 어기기도 합니다. 예를 들어, 정해진 도구에 물어보면 될 정보를 기록 전체를 하나씩 읽어서 찾는 식입니다. AI에게 구현을 맡기더라도 '이 데이터는 어디서 가져와야 하는지', '무엇은 절대 바꾸면 안 되는지' 같은 원칙은 사람이 정해 두고, 결과가 그 원칙을 지키는지 확인해야 합니다.
