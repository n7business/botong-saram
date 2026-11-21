---
id: ai-tools-0661
domain: ai-tools
claim: 클로드 코드 창을 여러 개 띄워 쓰다가 바꾼 사용자 설정이 사라진 적이 있다면 v2.1.330 이상으로 업데이트하고 설정을 다시 확인해야
  한다. 이전 버전에서는 여러 프로세스가 동시에 설정을 저장하면 변경 내용이 없어지는 문제가 있었기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics (Anthropic)
  seen: '2026-11-21'
  quote: Fixed changes to user settings being lost when several Claude Code processes
    saved them at the same time
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
- 설정
- 병렬세션
- 업데이트
verified_by: 공식 출처
---
v2.1.330에서 여러 클로드 코드 프로세스가 동시에 사용자 설정을 저장할 때 변경 내용이 사라지던 문제가 고쳐졌다. 권한 규칙이나 기본 모드처럼 안전과 관련된 설정이 이 문제로 조용히 원래대로 돌아갔을 수 있다. 업데이트한 뒤 ~/.claude/settings.json을 열어 넣어 둔 권한·훅 설정이 그대로 있는지 확인해야 한다. 디스크가 가득 찼을 때 ~/.claude.json 백업이 불완전하게 남아 멀쩡한 백업을 밀어내던 문제도 같은 버전에서 고쳐졌다.
