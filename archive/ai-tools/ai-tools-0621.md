---
id: ai-tools-0621
domain: ai-tools
claim: 셸 시작 파일(.zshrc 등)에 실행되면 곤란한 명령이 들어 있다면 클로드 코드에 CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1을
  설정해야 한다. v2.1.327부터는 첫 Bash 명령을 승인하기 전, 심지어 거부하더라도 셸 시작 파일이 먼저 실행될 수 있기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-19'
  quote: shell start-up files may now run before it's approved, even if it's refused;
    set `CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1` to turn this off
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
- bash
- 보안
- 설정
verified_by: 공식 출처
---
v2.1.327은 세션의 첫 Bash 명령을 빠르게 하려고 셸 시작 파일을 미리 실행합니다. 이 실행은 사용자가 명령을 승인하기 전에 일어나고, 명령을 거부해도 일어날 수 있습니다. .zshrc나 .bashrc에 서버 접속, 동기화, 외부 호출처럼 부작용이 있는 명령을 넣어 두었다면 의도하지 않은 때에 실행될 수 있습니다. 이런 경우 환경 변수 CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1을 설정해 이 동작을 끄세요.
