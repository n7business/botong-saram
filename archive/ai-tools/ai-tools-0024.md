---
id: ai-tools-0024
domain: ai-tools
claim: Claude Code 2.1.317부터 웹·셸 도구가 계정 이메일을 외부로 보내려 하면 확인을 묻는데, 직접 의도한 경우가 아니면 거절해야
  이메일이 User-Agent나 요청 본문에 실려 외부 서비스에 남는 걸 막는다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21317
  author: anthropics
  seen: '2026-11-03'
  quote: Added a check that asks before a web or shell tool call sends your account
    email address to the network
  source: Claude Code 릴리스 노트 (CHANGELOG)
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.317
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Added a check that asks before a web or shell tool call sends your account
    email address to the network
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-03'
last_confirmed: '2026-11-06'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- privacy
- security
- personal-data
verified_by: 공식 출처
mentions: 2
---
2.1.317에서 웹 도구나 셸 명령이 사용자의 Claude 계정 이메일 주소를 네트워크로 전송하기 전에 묻는 확인 단계가 추가됐다. 일부 사이트는 자동화 클라이언트에 연락처를 요구하는데, 모델이 이에 응해 계정 이메일을 헤더나 URL에 넣으려 할 때 이 프롬프트가 뜬다. 본인이 명시적으로 이메일을 쓰라고 한 작업이 아니라면 거절하고 범용 클라이언트 이름을 쓰게 하는 것이 안전하다. 외부 서비스로 나간 이메일은 캐시·색인될 수 있어 되돌리기 어렵다. 이 보호를 받으려면 2.1.317 이상으로 업데이트해야 한다.
