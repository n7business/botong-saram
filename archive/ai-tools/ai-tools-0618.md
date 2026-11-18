---
id: ai-tools-0618
domain: ai-tools
claim: 클로드 코드가 작업마다 허락을 구하게 하려면 permissions.defaultMode를 설정에 직접 적어 두어야 한다. v2.1.326부터는
  모드를 정하지 않은 세션이 조직 정책을 아직 불러오지 못했을 때 수동(Manual)이 아니라 auto mode로 시작하기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-19'
  quote: Changed terminal and VS Code sessions with no mode set to start in auto mode,
    not Manual mode, when your organization's policy hasn't loaded
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- auto-mode
- 권한
- 설정
verified_by: 공식 출처
---
v2.1.326부터 모드가 지정되지 않은 터미널·VS Code 세션은 조직 정책을 불러오지 못한 상태에서 auto mode로 시작합니다. auto mode에서는 안전 검사를 통과한 작업이 묻지 않고 바로 실행됩니다. 고객 자료가 있는 컴퓨터에서 모든 작업을 직접 승인하고 싶다면 사용자 설정이나 관리 설정의 permissions.defaultMode에 원하는 모드를 명시하세요. 조직 관리자는 관리 설정의 disableAutoMode로 auto mode를 끌 수도 있습니다.
