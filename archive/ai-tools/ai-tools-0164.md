---
id: ai-tools-0164
domain: ai-tools
claim: Claude Code v2.1.318 이전 버전에서는 메시지를 보낸 직후 친 키가 권한 확인 창의 답으로 처리될 수 있으므로, 업데이트하고
  그전까지는 확인 창을 읽은 뒤에 키를 누른다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.318
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Fixed permission prompts being answered by keys typed just after sending
    a message
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
- 권한
- 안전
- 업데이트
verified_by: 공식 출처
---
v2.1.318 이전에는 메시지를 보낸 직후 입력한 키나 느리게 뜨는 확인 창이 나타나기 전에 입력한 키가 권한 확인의 답으로 처리될 수 있었다. 이 경우 내용을 읽지 않은 작업이 승인되거나 거절될 수 있다. v2.1.318 이상으로 업데이트한다. 업데이트 전에는 메시지를 보낸 뒤 이어서 타이핑하지 말고, 확인 창이 뜨면 내용을 읽고 답한다.
