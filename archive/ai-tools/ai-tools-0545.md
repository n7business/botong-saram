---
id: ai-tools-0545
domain: ai-tools
claim: AI가 위키나 문서 모음을 한 번 만들고 나면, 정리 작업을 한 번 더 돌려 없는 페이지를 가리키는 링크와 빠진 목차를 찾아 고치게 해야
  한다. 한 번에 만든 위키에는 아직 만들어지지 않은 페이지로 걸린 링크가 남기 때문이다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic
  seen: '2026-11-14'
  quote: A second dreaming pass closed many of these gaps.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2026-12-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 위키
- 점검
- 링크
- 에이전트
verified_by: 실무자 실측(단일 출처)
---
Anthropic 실험에서 AI는 위키를 만드는 도중 아직 없는 페이지로 링크를 걸어 두곤 했습니다. 두 번째 정리 작업을 돌리자 이런 빈틈이 상당수 메워졌습니다. 한 과제에서는 없는 페이지를 가리키던 링크 9개를 같은 문서의 기존 페이지로 바로잡았습니다. 목차를 포함해 새 페이지 3개도 추가했습니다. AI에게 문서 모음을 만들게 했다면 끝난 뒤 '깨진 링크와 빠진 목차를 찾아 고쳐라'라는 점검 작업을 따로 한 번 더 맡기세요.
