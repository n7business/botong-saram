---
id: ai-tools-0574
domain: ai-tools
claim: 클로드 코드 예약 작업이나 /loop로 스킬을 무인 실행하고 있다면, v2.1.325부터 allowed-tools나 훅을 선언한 스킬은
  실행 전에 묻도록 바뀌었으므로 permissions.allow에 Skill(스킬이름)을 추가해야 작업이 멈추지 않는다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-15'
  quote: Changed scheduled tasks and `/loop` to ask before running a skill that declares
    `allowed-tools` or hooks; add `Skill(name)` to `permissions.allow` to run it unattended
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: '2026-12-15'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 예약작업
- loop
- 권한
- v2.1.325
verified_by: 공식 출처
---
클로드 코드 v2.1.325부터 예약 작업과 /loop가 allowed-tools나 훅을 선언한 스킬을 실행하기 전에 확인을 받도록 바뀌었습니다. 밤사이 돌던 정기 작업이 이 확인 단계에서 아무도 답하지 않아 멈춰 있을 수 있습니다. 무인으로 계속 돌려야 하는 스킬이면 settings.json의 permissions.allow에 Skill(스킬이름)을 넣으세요. 같은 버전에서 Desktop·IDE·SDK의 'Always allow'도 바뀌어, 저장된 규칙에 기대던 예약 작업이 사람 응답을 기다릴 수 있습니다. 업데이트한 다음 날에는 예약 작업 결과가 제대로 나왔는지 꼭 확인하세요.
