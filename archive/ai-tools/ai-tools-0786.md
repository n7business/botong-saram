---
id: ai-tools-0786
domain: ai-tools
claim: IntelliJ·PyCharm 같은 JetBrains 프로그램에서 클로드 코드를 쓰려면 마켓플레이스에서 플러그인만 깔아서는 안 되고,
  클로드 코드 CLI를 따로 설치한 뒤 프로그램을 다시 시작해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-25'
  quote: The plugin requires the Claude Code CLI, installed separately
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
- jetbrains
- 설치
verified_by: 공식 출처
---
VS Code 확장과 달리 JetBrains용 클로드 코드 플러그인은 CLI가 깔려 있어야 돌아갑니다. 먼저 터미널에서 클로드 코드 CLI를 설치하고 claude --version으로 버전이 나오는지 확인합니다. 그다음 JetBrains Marketplace에서 Claude Code 플러그인을 설치하고 IDE를 다시 시작합니다.
