---
id: ai-tools-0016
domain: ai-tools
claim: 추론 강도를 매우 높음으로 올려도 같은 문제에서 두 번 막히면 세 번째를 기다리지 말고 상위 모델로 바꾸고, 파일 찾기·로그 읽기 같은
  조회는 작은 모델이나 서브에이전트에 맡긴다.
status: candidate
evidence: consensus
confidence: 0.65
sources:
- url: https://yozm.wishket.com/magazine/detail/3993/
  author: 비벙 (요즘IT)
  seen: '2026-11-03'
  quote: 세 번째 실패를 기다리지 마세요.
  source: 요즘IT
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
- 모델선택
- 서브에이전트
- haiku
---
xhigh에서도 같은 지점에서 두 번 실패하면 더 돌리지 말고 가장 성능 높은 모델로 전환한다. 전환 시에는 /compact를 먼저 돌려 캐시 재작성 비용을 줄인다. 반대로 파일 탐색, 로그·테스트 출력 읽기처럼 실수가 바로 드러나는 조회성 작업은 작은 모델(haiku)에 맡긴다. 다만 작은 모델이 검색 결과를 잘못 읽어 메인 모델을 엉뚱한 파일로 보내면 되돌아오는 비용이 크니 조회 범위에 한정한다. 서브에이전트는 별도 지정이 없으면 메인 모델을 물려받으므로, 정의에 model: haiku를 적거나 CLAUDE_CODE_SUBAGENT_MODEL 환경변수로 일괄 지정한다.
