---
id: ai-tools-0026
domain: ai-tools
claim: 맥·리눅스에서 Claude Code를 무인으로 돌리는 환경(launchd·cron·클라우드 세션)은 2.1.316 이상으로 올려야 하며,
  그 이전 버전은 인증 거부 등으로 스스로 종료될 때 실행 중이던 셸 명령을 남겨 둬 좀비 프로세스가 쌓일 수 있다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  author: anthropics
  seen: '2026-11-03'
  quote: Fixed shell commands being left running on macOS and Linux when Claude Code
    exits by itself
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  author: anthropics
  seen: '2026-11-03'
  quote: Fixed bash scripts started from the Bash tool stopping after their first
    command when `SHELLOPTS` is exported
  source: Claude Code 릴리스 노트 (CHANGELOG)
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
- automation
- launchd
- macos
- process-cleanup
verified_by: 공식 출처
---
2.1.316에서 macOS·Linux의 Claude Code가 스스로 종료될 때(예: 자격 증명이 거부되거나 클라우드 세션이 보관 처리될 때) 셸 명령이 그대로 남아 계속 실행되던 문제가 수정됐다. 같은 버전에서 Bash 도구가 SHELLOPTS가 export된 환경에서 스크립트를 첫 명령에서 멈추던 버그도 고쳐졌다. 맥미니에 launchd로 수집기를 돌리는 식의 무인 운영이라면 토큰 만료 한 번에 프로세스가 누적돼 메모리·CPU를 잠식할 수 있었다. 무인 환경은 버전을 올리고, 주기적으로 남은 프로세스가 없는지 ps로 점검한다.
