---
id: ai-tools-0300
domain: ai-tools
claim: AI 채팅창에 붙여 넣어 노출된 키는 폐기하거나 새로 발급하고, 앞으로는 .env.local 같은 환경 변수 파일에 직접 넣어야 토큰
  유출 위험을 줄일 수 있다.
status: candidate
evidence: anecdote
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=wa5BtVLAcNs
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-07'
  quote: 채팅창에 노출된 키는 폐기하거나 새로 발급하라
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- API키
- 환경변수
- 보안
---
클로드 코드와 코덱스는 채팅창에 입력한 키도 위험하게 보며, 에이전트가 폐기나 재발급을 안내하기도 합니다. 채팅창 대신 .env.local 같은 환경 변수 파일에 키를 직접 수동으로 넣을 수 있습니다. 레퍼런스 ID처럼 공유돼도 괜찮은 값도 있지만, 토큰은 반드시 새어 나가지 않게 관리해야 합니다. Vercel 토큰처럼 한 번 복사하면 다시 볼 수 없는 값은 발급 후 한 번에 진행합니다.
