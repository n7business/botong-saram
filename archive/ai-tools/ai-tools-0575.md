---
id: ai-tools-0575
domain: ai-tools
claim: 클로드 코드 샌드박스 덕분에 Bash 명령이 묻지 않고 실행되던 환경이라면 v2.1.325부터는 일반 권한 확인을 거치도록 바뀌었으므로,
  예전처럼 쓰려면 sandbox.autoAllowBashIfSandboxed를 true로 설정해야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-15'
  quote: 'Changed sandboxed Bash commands to follow the normal permission flow by
    default; set `sandbox.autoAllowBashIfSandboxed: true` to keep running them without
    prompts'
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
- 샌드박스
- 권한
- v2.1.325
verified_by: 공식 출처
---
v2.1.325부터 샌드박스 안에서 실행되는 Bash 명령도 기본적으로 일반 권한 확인 절차를 따릅니다. 업데이트 뒤 갑자기 명령마다 확인 창이 뜨거나 무인 작업이 멈췄다면 이 변경 때문일 가능성이 큽니다. 예전처럼 묻지 않고 실행하려면 설정에 sandbox.autoAllowBashIfSandboxed: true를 넣으세요. 관리 설정으로 샌드박스를 켜는 조직은 우선순위가 가장 높은 관리 설정 쪽에 이 값을 넣어야 합니다. 묻지 않게 하는 쪽이 편하지만 확인 단계가 하나 사라지는 것이므로, 샌드박스 범위를 먼저 확인한 다음 켜세요.
