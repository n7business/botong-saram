---
id: ai-tools-0659
domain: ai-tools
claim: 클로드 코드를 사람 없이 자동으로 돌리면서 작업 폴더나 상위 폴더를 rm으로 지우는 단계가 있다면 v2.1.330부터는 그 단계가 실행되지
  않는다는 점을 확인해야 한다. 이런 rm 명령은 이제 승인을 요구하고, 승인할 사람이 없으면 거부되기 때문이다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics (Anthropic)
  seen: '2026-11-21'
  quote: where nobody can answer, they're refused
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: '2026-12-21'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 자동화
- 권한
- 삭제
verified_by: 공식 출처
---
v2.1.330부터 루트·홈·최상위 폴더·현재 작업 폴더를 겨냥한 rm 명령은 더 많은 경우에 승인을 묻는다. 예약 작업이나 claude -p처럼 답할 사람이 없는 실행에서는 이런 명령이 거부된다. 그래서 '작업 폴더를 비우고 다시 받기' 같은 단계가 들어간 자동화는 조용히 중간에 멈출 수 있다. 업데이트 뒤 첫 자동 실행 기록을 확인하고, 지우는 대상을 하위 폴더로 좁히거나 그 단계를 셸 스크립트로 빼는 게 좋다. 이 변경은 실수로 중요한 폴더가 지워지는 일을 막아 주므로 끄기보다는 그대로 두는 편이 낫다.
