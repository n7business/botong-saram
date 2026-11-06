---
id: ai-tools-0203
domain: ai-tools
claim: AI 에이전트가 만든 코드는 테스트 통과나 봇의 승인만 보고 합치지 말고, 코드를 쓰지 않은 별도 에이전트가 사용자처럼 직접 실행해 본
  판정을 받아야 한다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://yozm.wishket.com/magazine/detail/4027/
  author: 이정민
  seen: '2026-11-06'
  quote: 코드를 쓰지 않은 에이전트의 판정만 인정합니다.
  source: 요즘IT
- url: https://www.youtube.com/watch?v=6cr4PeilKJk
  author: 짐코딩
  seen: '2026-11-06'
  quote: 생성 AI에게 비판적으로 보라고 시키는 것보다 검증 전문 AI를 따로 두는 게 훨씬 쉽다.
  source: 짐코딩 (@gymcoding)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI에이전트
- 코드검증
- 바이브코딩
- pstack
---
커서 엔지니어 로런 탠이 공개한 pstack의 배포 절차는 변경(PR)마다 검증 에이전트를 붙여 PASS, PASS+NOTES, FAIL 중 하나를 남기게 합니다. 작성자는 자기가 만들려던 것만 확인하기 쉬우므로 코드를 쓰지 않은 에이전트의 판정만 인정합니다. 테스트 통과 표시와 봇 승인은 실제 사용 흐름을 돌려 본 결과가 아니어서 판정으로 치지 않습니다. 다만 이 사례는 PR 수가 2,500개와 2,000개로 엇갈리고 비용, 장애율, 되돌린 PR 비율도 공개되지 않았습니다. 사람 리뷰를 없애도 된다는 근거로 삼지 말고 검증 구조만 참고해야 합니다.
