---
id: ai-tools-0107
domain: ai-tools
claim: Claude Code 토큰이 예상보다 많이 나가면 공식 마켓플레이스의 session-report 플러그인으로 기간(기본 7일, 30d·24h로
  지정)별 리포트를 만들어 '가장 비싼 프롬프트'와 캐시 처리 비율부터 확인한다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=L94yAQR9VvA
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-03'
  quote: 지정하지 않으면 기본 옵션은 7일이기 때문에
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
- 플러그인
- 토큰절약
- session-report
- 프롬프트캐싱
---
/plugin에서 공식 마켓플레이스(claude-plugins-official)의 Browse plugins로 session-report를 찾아 설치하고, /reload-plugins를 실행해야 쓸 수 있습니다. '지난 30일 세션 리포트 만들어 줘'처럼 말로 요청해도 되고 슬래시 명령으로 직접 불러도 됩니다. 기간은 30d·24h 같은 옵션으로 정하며, 지정하지 않으면 7일입니다. HTML 리포트에서 프로젝트·스킬·서브에이전트·프롬프트별 토큰 사용량을 볼 수 있습니다. 가장 중요한 건 '가장 비싼 프롬프트' 섹션입니다. 캐시 비율이 낮다면 CLAUDE.md처럼 반복되는 부분에 붙는 1/10 할인을 제대로 받지 못하고 있다는 신호입니다.
