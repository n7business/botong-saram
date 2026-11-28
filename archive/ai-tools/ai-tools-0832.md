---
id: ai-tools-0832
domain: ai-tools
claim: 클로드 코드 설치 명령을 실행한 뒤에는 새 터미널 창을 열고 'claude --version'으로 설치가 됐는지 확인해야 한다. 버전
  번호가 나오지 않고 claude 명령을 찾을 수 없다고 나오면 설치에 실패한 것이 아니라 PATH 설정 문제다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-28'
  quote: open a new terminal window and run `claude --version`
  source: Claude Code 공식 문서
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2026-12-28'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 설치
- PATH
verified_by: 공식 출처
---
설치 명령은 내려받는 동안 진행 상황을 보여 주지 않습니다. 설치가 끝나면 기존 창이 아니라 새 터미널 창을 열고 claude --version을 입력해 보세요. 버전 번호가 나오면 제대로 설치된 것입니다. 'claude'를 찾을 수 없다거나 인식할 수 없다고 나오면 설치 폴더가 아직 PATH에 등록되지 않은 것이므로, 공식 문서의 'Fix your PATH' 안내를 따라 고치면 됩니다.
