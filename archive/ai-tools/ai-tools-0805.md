---
id: ai-tools-0805
domain: ai-tools
claim: 온라인 경품 추첨을 하면 마감 뒤 유효 명단을 고정해 그 해시를 먼저 공개하고, HMAC 같은 방식으로 응모번호마다 점수를 계산한 검증
  파일을 남겨야 한다. 그러면 누구나 결과를 다시 계산해 볼 수 있다.
status: candidate
evidence: anecdote
confidence: 0.5
sources:
- url: https://www.gpters.org/ai-tools/post/구독-정리하면서-남긴-판단-기준-3개-추첨-검증집중-환경위치-설명-mwumba6e
  author: 윤영준
  seen: '2026-11-25'
  quote: 마감 뒤 유효 명단을 고정하고 명단 해시를 공개합니다.
  source: 지피터스 GPTers
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 경품추첨
- 이벤트
- 공정성
- 검증
---
경품 추첨 발표 뒤에는 '조작 아니냐'는 말이 자주 나옵니다. 마감 뒤 유효 명단을 고정하고 명단 해시를 먼저 공개하세요. 추첨용 시드를 정해 응모번호마다 HMAC-SHA256 값을 계산하고, 그 값을 점수로 순위를 매깁니다. 검증 파일에는 명단·규칙 해시, 시드 약속, 응모별 점수, 최종 순위를 담습니다. 이 파일이 있으면 참여자가 브라우저에서 결과를 다시 계산해 순위가 같은지 대조할 수 있습니다.
