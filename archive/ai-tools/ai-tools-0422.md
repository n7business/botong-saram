---
id: ai-tools-0422
domain: ai-tools
claim: 클로드 코드 자동 모드나 권한 우회 모드에서는 클로드가 만든 mod가 묻지 않고 켜지고 mod의 도구 호출도 권한 창을 띄우지 않으므로,
  꼭 막아야 할 작업은 ask 규칙이 아니라 deny 규칙으로 걸어 두어야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-10'
  quote: deny rules and organization policy still apply
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 권한
- mod
- 자동모드
- deny규칙
verified_by: 공식 출처
---
2.1.321부터 클로드가 작성한 mod는 auto 모드와 bypass 모드에서 확인 없이 켜집니다. mod 안에서 일어나는 도구 호출($.tool.call, $.mcp.call)은 내가 만든 ask 규칙이 있어도 권한 창을 띄우지 않습니다. 다만 deny 규칙과 조직 정책은 그대로 적용됩니다. 삭제·업로드처럼 되돌리기 어려운 작업을 막고 싶다면 '물어보기'로 두지 말고 '거부' 규칙으로 등록하세요.
