---
id: ai-tools-0390
domain: ai-tools
claim: 클로드 코드를 쓰면서 코딩을 직접 익히고 싶다면 출력 스타일을 Learning으로 두어야, AI가 일상적인 구현은 하고 설계 판단이 필요한
  몇 줄은 내가 직접 작성하게 맡겨 준다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://code.claude.com/docs/en/output-styles
  author: Anthropic
  seen: '2026-11-09'
  quote: it leaves a few lines for you.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2026-12-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- output-style
- 학습
verified_by: 공식 출처
---
Learning 스타일에서 Claude는 일상적인 구현은 직접 처리합니다. 오류 처리나 업무 규칙처럼 정답이 여러 개인 부분에 이르면 파일에 TODO(human) 표시를 남기고 멈춥니다. 무엇을 써야 하고 무엇을 따져야 하는지 안내를 받은 뒤 직접 코드를 쓰고 끝났다고 알리면 작업이 이어집니다. 매번 직접 쓰기보다 이유만 알고 싶다면 선택한 이유를 Insight 블록으로 설명해 주는 Explanatory 스타일을 쓰십시오.
