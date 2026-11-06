---
id: ai-tools-0162
domain: ai-tools
claim: Claude Code v2.1.318부터는 IDE 터미널에서 실행해도 IDE 확장이 자동으로 설치·업데이트되지 않으므로, 외부 터미널의
  /ide나 편집기의 확장 화면에서 직접 설치·업데이트한다.
status: verified
evidence: policy
confidence: 0.92
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.318
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Changed Claude Code to no longer install or update the IDE extension when
    started in an IDE terminal
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- vscode
- ide
- 업데이트
verified_by: 공식 출처
---
예전처럼 VS Code 같은 IDE의 터미널에서 claude를 실행해도 v2.1.318부터는 IDE 확장이 설치되거나 업데이트되지 않는다. 확장이 없거나 오래됐다면 IDE 바깥 터미널에서 /ide를 실행하거나 편집기의 확장 화면을 이용한다. 터미널의 Claude Code를 업데이트해도 확장까지 함께 업데이트된다고 여기지 말고 따로 확인한다.
