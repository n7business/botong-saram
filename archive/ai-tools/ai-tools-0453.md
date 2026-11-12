---
id: ai-tools-0453
domain: ai-tools
claim: 윈도우에서 WSL 없이 클로드 코드를 쓴다면 Git for Windows를 먼저 설치해야, 클로드 코드가 PowerShell 대신 Bash
  도구로 명령을 실행할 수 있다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: Git for Windows is recommended on native Windows
  source: Claude Code 공식 문서
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 윈도우
- 설치
- Git
verified_by: 공식 출처
---
공식 문서는 윈도우에서 WSL 없이 쓸 때 Git for Windows 설치를 권장합니다. Git for Windows가 없으면 클로드 코드는 Bash 대신 PowerShell로 명령을 실행합니다. 인터넷 예제와 안내는 대부분 Bash 기준이라 PowerShell에서는 그대로 맞지 않을 수 있습니다. WSL을 쓴다면 Git for Windows는 따로 설치하지 않아도 됩니다.
