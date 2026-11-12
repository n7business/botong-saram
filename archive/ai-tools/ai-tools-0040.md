---
id: ai-tools-0040
domain: ai-tools
claim: 웹 수집 에이전트를 매일 돌리려면 Claude Code 루틴(또는 ChatGPT 예약 작업)에 등록하고, 결과는 폴더에 엑셀만 쌓지 말고
  요약해 Slack이나 메일로 받도록 바꾸며, 우리 회사 PR 기사처럼 리스크 조건에 걸리는 건만 알림이 오게 고정한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=iJfRqfDetsI
  author: 일잘러 장피엠
  seen: '2026-11-03'
  quote: 수집이 끝나면 메일이나 Slack으로 알려 줘
  source: 일잘러 장피엠
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
- 루틴
- 자동화
- 웹-수집
- slack
---
수집 요청이 한 번 성공했으면 '루틴으로 등록해 줘'라고 말해 매일 지정 시각에 자동으로 돌게 한다. Claude Code에는 루틴, ChatGPT에는 예약 작업(Scheduled Tasks) 기능이 있다. 기본 산출물은 엑셀이지만 폴더에 파일만 쌓이면 잘 안 보게 되므로, Slack·메일 앱을 커넥터로 붙이고 '수집이 끝나면 메일이나 Slack으로 알려 줘'라고 요청해 요약을 받는다. 범용 크롤러를 특정 사이트·특정 항목만 모으도록 고정하면 더 강력해지는데, 예를 들어 회사 PR 기사를 계속 모니터링하다가 법적 리스크로 보이는 기사만 정리해 메일로 보내게 조건을 걸 수 있다. 화자는 별도 맥미니를 서버로 두고 매일 LinkedIn·YouTube의 경쟁 크리에이터 콘텐츠를 모은다.
