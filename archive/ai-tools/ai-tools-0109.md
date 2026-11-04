---
id: ai-tools-0109
domain: ai-tools
claim: Claude Code가 같은 실수를 세 번쯤 반복하면 AI를 탓하며 다시 시키지 말고 Hookify 플러그인(/hookify)으로 그
  실수를 막는 규칙을 등록해, 실수→이유 묻기→재시도로 수천 토큰이 새는 것을 막는다.
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=L94yAQR9VvA
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 같은 실수가 세 번쯤 반복됐다 싶으면 패턴 자동 추출 명령을 한 번 돌려보라고 하며
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
- hookify
- 하네스엔지니어링
- 토큰절약
---
잘못된 작업을 하고, 이유를 묻고, 고쳐서 다시 시키는 사이클은 매번 수천 토큰을 씁니다. AI가 실수하면 같은 실수가 다시 나오지 않게 환경을 고치는 것이 하네스 엔지니어링의 핵심입니다. /hookify 뒤에 Claude가 자주 하는 실수를 적고 몇 가지 질문에 답하면, .claude 폴더 아래에 언제 발동할지와 지켜야 할 지침이 담긴 마크다운 규칙 파일이 생깁니다. 같은 실수가 세 번쯤 반복됐다면 최근 짜증 났던 패턴을 자동으로 뽑는 명령을 돌려 규칙을 추가하세요. 등록된 규칙은 목록 보기 명령으로 확인할 수 있습니다.
