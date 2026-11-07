---
id: ai-tools-0288
domain: ai-tools
claim: 클로드 코드를 설치한 뒤 `claude`를 찾을 수 없다고 나오면 다시 설치하기 전에 설치 폴더가 PATH에 들어 있는지부터 확인한다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-07'
  quote: If your shell says `claude` isn't found or isn't recognized, the install
    directory isn't on your PATH yet
  source: Claude Code 공식 문서
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 설치
- 문제해결
- path
verified_by: 공식 출처
---
설치 명령은 내려받는 동안 진행 상황을 보여 주지 않습니다. 설치가 끝나면 새 터미널 창을 열고 `claude --version`을 실행해 버전 번호가 나오는지 확인합니다. `claude`를 찾을 수 없거나 인식되지 않는다고 나오면 설치 폴더가 아직 PATH에 없는 것이므로 공식 문서의 Fix your PATH 안내를 따릅니다. 다른 설치 오류는 Troubleshoot installation 문서에서 오류 내용에 맞는 해결법을 찾습니다.
