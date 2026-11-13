---
id: ai-tools-0523
domain: ai-tools
claim: 클로드 코드에서 '삭제 전에 꼭 물어보기'처럼 반드시 지켜야 하는 규칙은 출력 스타일이나 지시문에만 적지 말고 훅이나 권한 설정으로 걸어야
  하는데, 출력 스타일은 클로드가 따르는 지시일 뿐 강제되지 않기 때문이다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/output-styles
  author: Anthropic
  seen: '2026-11-13'
  quote: It's an instruction Claude follows, so nothing enforces it.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-13'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 출력스타일
- 훅
- 안전
verified_by: 공식 출처
---
출력 스타일은 세션의 모든 답변에 적용되지만, 클로드가 따르는 지시일 뿐 아무것도 강제하지 않습니다. 예를 들어 Proactive 스타일에는 데이터를 지우거나 운영 시스템을 바꾸기 전에 확인하라는 지시가 들어 있지만, 이것은 권한 확인 창과 별개이고 권한 모드도 바꾸지 않습니다. 공식 문서는 편집 후 자동 정리나 특정 명령 차단처럼 예외 없이 일어나야 하는 일에는 훅을 쓰라고 안내합니다. 훅은 클로드가 지시를 따르는지와 상관없이 클로드 코드가 직접 실행합니다. 프로젝트 지식은 CLAUDE.md에, 답변 말투는 출력 스타일에, 꼭 지켜야 할 일은 훅에 나눠 두세요.
