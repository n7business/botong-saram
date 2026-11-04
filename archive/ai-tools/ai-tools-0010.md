---
id: ai-tools-0010
domain: ai-tools
claim: Claude Code가 같은 규칙이나 명령을 두 번 틀리면 채팅에서 매번 고쳐주지 말고 CLAUDE.md에 그 규칙을 적는다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/features-overview
  author: Anthropic (Claude Code Docs)
  seen: '2026-11-03'
  quote: A repeated mistake or a recurring review comment is a CLAUDE.md edit, not
    a one-off correction in chat.
  source: Claude Code 공식 문서
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- 워크플로
- 설정
---
채팅에서 한 번 바로잡은 내용은 다음 세션에 남지 않는다. 공식 문서는 '두 번 틀리면 CLAUDE.md에 추가'를 기준으로 제시한다. 반복되는 실수나 코드 리뷰에서 계속 나오는 지적은 CLAUDE.md 편집 대상이다. 같은 프롬프트를 반복해서 치고 있다면 그건 스킬로 저장하고, 브라우저에서 데이터를 계속 복사해 넣고 있다면 MCP 서버로 연결한다. 이렇게 트리거별로 설정을 쌓아가면 처음부터 전부 구성할 필요가 없다.
