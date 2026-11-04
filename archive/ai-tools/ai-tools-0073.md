---
id: ai-tools-0073
domain: ai-tools
claim: AI 예약 작업은 등록만 하고 예정일을 기다리지 말고 등록 직후 한 번 미리 실행해 보고 형식과 보내면 안 되는 것을 보내지 않았는지
  확인하며, 다음 실행 시각과 시간대(UTC/한국 시간)도 함께 점검한다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=zO68MQmfvcA
  author: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
  seen: '2026-11-03'
  quote: 예약을 만드는 허락 카드는 끝까지 읽어 보세요.
  source: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
- url: https://www.youtube.com/watch?v=k_n8fmTt8Ck
  author: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
  seen: '2026-11-03'
  quote: 기다리지 말고 한 번 미리 돌려서 보고 형식과, 보내면 안 되는 걸 보내지 않았는지 확인한다.
  source: '샘 호트만 : AI 엔지니어의 시선 (@ai.sam_hottman)'
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 예약작업
- 크론
- 검증
- claude-code
- hermes
---
Claude Code 데스크톱의 예약 작업은 허락 카드를 끝까지 읽고 만든 뒤, 왼쪽 '예약됨'에서 요일과 다음 실행 시각을 확인하고 오른쪽 위 '실행'으로 미리 돌려 본다. 서버형 에이전트(Hermes 등)의 크론도 같은 원리로, 목록에서 다음 실행 시각과 시간대를 확인한다. 화자의 서버는 UTC로 잡혀 있어 한국 시간으로 바꿔야 했다. 예약 실행은 매번 새 세션이라 지난 대화가 없고 작업 폴더 밖에서 시작할 수 있으므로, 작업 폴더를 지정하고 처음 보는 사람도 알 수 있게 완결된 지시문을 쓴다. 조용히 끝난 날에도 실행 기록을 확인한다.
