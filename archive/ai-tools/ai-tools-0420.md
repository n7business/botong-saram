---
id: ai-tools-0420
domain: ai-tools
claim: 클로드 코드 2.1.321 이전 버전에는 권한 확인 없이 명령이 실행되거나 MCP 로그인 토큰이 다른 서버로 새는 버그가 있었으므로,
  권한 창과 deny 규칙에 기대어 쓴다면 최신 버전으로 업데이트해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-10'
  quote: Fixed a case where a read-only Bash command ran outside the sandbox without
    a permission prompt
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
- 보안
- 권한
- MCP
- 업데이트
verified_by: 공식 출처
---
2.1.321에서 여러 보안 문제가 고쳐졌습니다. MCP OAuth 요청이 리디렉션될 때 refresh token 같은 비밀값을 다른 호스트로 보내던 문제, 읽기 전용 Bash 명령이 권한 창 없이 샌드박스 밖에서 실행되던 문제가 대표적입니다. cp·mv로 폴더 안에 파일을 쓸 때 deny 규칙과 보호 파일 확인이 적용되지 않던 문제도 함께 고쳐졌습니다. 권한 창을 꼼꼼히 봐도 창이 아예 뜨지 않으면 막을 방법이 없습니다. claude --version으로 버전을 확인하고 업데이트하세요.
