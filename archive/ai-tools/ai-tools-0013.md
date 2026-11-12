---
id: ai-tools-0013
domain: ai-tools
claim: Claude Code에서 무관한 작업으로 넘어갈 때는 /clear로 대화를 비우고, 같은 작업은 끊지 말고 이어가야 토큰과 캐시를 아낀다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/3993/
  author: 비벙 (요즘IT)
  seen: '2026-11-03'
  quote: 턴이 적으면 처리하는 입력도 줄어들
  source: 요즘IT
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 토큰절약
- 캐시
- clear
verified_by: 실무자 실측(단일 출처)
---
Claude Code는 매 턴 지금까지의 대화 전체를 다시 보내므로, 짧게 '다시 해봐'라고만 적어도 이미 읽은 파일과 테스트 결과가 전부 재전송된다. 대화가 2만→12만 토큰으로 커지는 작업을 40턴에 끝내면 누적 입력이 약 280만 토큰, 25턴이면 약 175만 토큰으로 줄어든다. 따라서 같은 수정을 불필요하게 반복하지 말고, 전혀 다른 일로 넘어갈 때는 /clear로 이전 맥락을 끊는다. 반대로 같은 작업을 이어가는 동안은 반복 내용이 캐시에서 재사용되므로 세션을 자주 끊을 필요가 없다. 캐시 수명은 구독 1시간, API 키·클라우드 제공자 5분이며 구독이라도 추가 크레딧 사용 시 5분으로 줄어든다.
