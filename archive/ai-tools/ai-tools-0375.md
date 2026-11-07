---
id: ai-tools-0375
domain: ai-tools
claim: AI가 만든 웹페이지의 버튼이 안 되면 콘솔의 빨간 에러 문장을 요약하지 말고 통째로 복사해 증상과 함께 주어야, 원인을 더 빨리 찾게
  할 수 있다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=xjHR00fV-XQ
  author: 코드깎는노인
  seen: '2026-11-07'
  quote: 요약하지 말고 보이는 그대로 통째로 복사해
  source: 코드깎는노인
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드 코드
- 디버깅
- 에러
- 개발자 도구
---
크롬 개발자 도구(맥 Command+Option+J, 윈도우 Ctrl+Shift+J)의 콘솔에서 빨간 에러 문장을 찾습니다. 이를 보이는 그대로 복사해 '할 일을 입력해도 추가가 안 돼' 같은 증상과 함께 붙여 넣으면, 몇 번째 줄인지 같은 단서까지 함께 전달됩니다. 화자의 사례에서는 13초 만에 원인을 찾았는데, 미리 커밋해 둔 시점과 비교할 수 있었던 덕도 있습니다. 에러 문장을 못 찾으면 보이는 증상과 원래 어떻게 돼야 하는지만 말해도 됩니다. 고친 뒤에는 새로고침으로 확인하고 커밋합니다.
