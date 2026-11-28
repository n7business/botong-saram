---
id: ai-tools-0831
domain: ai-tools
claim: 윈도우 PC에서 클로드 코드를 쓴다면 Git for Windows를 먼저 설치해야 한다. 설치하지 않으면 클로드 코드가 Bash 대신
  PowerShell로 명령을 실행하게 되기 때문이다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-28'
  quote: Git for Windows is recommended on native Windows so Claude Code can use the
    Bash tool.
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
- 윈도우
- 설치
verified_by: 공식 출처
---
윈도우에서 WSL 없이 클로드 코드를 바로 설치할 때 공식 문서는 Git for Windows 설치를 권장합니다. Git for Windows가 있어야 클로드 코드가 Bash 도구를 쓸 수 있습니다. 없으면 PowerShell을 대신 씁니다. WSL로 설치했다면 Git for Windows는 필요 없습니다.
