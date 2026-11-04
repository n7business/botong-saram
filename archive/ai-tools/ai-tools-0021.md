---
id: ai-tools-0021
domain: ai-tools
claim: 스크립트에서 claude -p의 종료 코드로 성공 여부를 판단하려면 Claude Code를 2.1.314 이상(디스크 꽉 참 감지는 2.1.317
  이상)으로 올려야 하며, 그 이전 버전은 시작 실패나 저장 실패 시에도 0을 반환한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21314
  author: anthropics
  seen: '2026-11-03'
  quote: Fixed `claude -p` exiting with code 0 and no output when startup failed;
    it now prints the error and exits 1
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317
  author: anthropics
  seen: '2026-11-03'
  quote: Fixed `claude -p` exiting 0 when a full disk or quota lost its transcript
    or ~/.claude.json writes; it now prints an error and, in text and json output,
    exits 1.
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
- headless
- automation
- exit-code
- claude-p
verified_by: 공식 출처
---
2.1.314 이전 버전의 claude -p는 시작 자체가 실패해도 아무 출력 없이 종료 코드 0을 반환했다. 2.1.314부터 시작 실패 시 오류를 출력하고 1로 종료한다. 2.1.317부터는 디스크가 가득 차거나 용량 제한으로 대화 기록(transcript)이나 ~/.claude.json 저장이 실패했을 때도 text·json 출력 모드에서 1로 종료한다. launchd·cron으로 무인 자동화를 돌리는 경우 이 버전 미만이면 실패를 성공으로 오인해 빈 결과가 그대로 흘러갈 수 있다. 자동화 스크립트는 종료 코드와 함께 출력이 비어 있는지도 같이 검사하는 것이 안전하다.
