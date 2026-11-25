---
id: ai-tools-0788
domain: ai-tools
claim: 클로드 코드가 파일을 고칠 때마다 자동 정리를 돌리거나 커밋 전에 검사를 돌리게 하려면, AI에게 매번 말로 부탁하지 말고 훅(hooks)을
  설정해야 한다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-25'
  quote: Hooks let you run shell commands before or after Claude Code actions
  source: Claude Code 공식 문서
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: '2026-12-25'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- hooks
- 자동화
verified_by: 공식 출처
---
훅은 클로드 코드가 어떤 동작을 하기 전이나 후에 정해 둔 명령을 자동으로 실행하는 기능입니다. 공식 문서는 파일을 고칠 때마다 자동으로 서식을 맞추거나 커밋 전에 린트 검사를 돌리는 것을 예로 듭니다. CLAUDE.md에 적은 지시는 AI가 따를 수도 안 따를 수도 있습니다. 반면 훅으로 걸어 둔 명령은 정해진 시점마다 반드시 실행됩니다.
