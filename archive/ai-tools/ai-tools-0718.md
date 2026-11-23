---
id: ai-tools-0718
domain: ai-tools
claim: 클로드 코드에서 --continue나 --resume으로 이어서 하려는데 빈 세션이 열린다면 대화가 사라졌다고 판단하지 말고 v2.1.330
  이상으로 업데이트한 뒤 다시 시도해야 합니다. 이전 버전에서는 마지막으로 저장된 메시지의 시간 정보에 문제가 있으면 빈 세션이 열리거나 실패했습니다.
status: verified
evidence: policy
confidence: 0.7
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-23'
  quote: '`--continue` and `--resume` opening an empty session or failing'
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- resume
- 업데이트
verified_by: 공식 출처
---
이전 버전의 클로드 코드는 마지막으로 저장된 메시지에 시간 정보(timestamp)가 빠졌거나 잘못돼 있으면, --continue나 --resume으로 이어 가려 할 때 빈 세션을 열거나 실패했습니다. 이 문제는 v2.1.330에서 고쳐졌습니다. 이전 대화가 없어진 것처럼 보이면 업데이트한 뒤 다시 시도하세요. 같은 작업을 처음부터 다시 시키기 전에 먼저 확인하는 것이 좋습니다.
