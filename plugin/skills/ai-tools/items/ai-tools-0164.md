# Claude Code v2.1.318 이전 버전에서는 메시지를 보낸 직후 친 키가 권한 확인 창의 답으로 처리될 수 있으므로, 업데이트하고 그전까지는 확인 창을 읽은 뒤에 키를 누른다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

v2.1.318 이전에는 메시지를 보낸 직후 입력한 키나 느리게 뜨는 확인 창이 나타나기 전에 입력한 키가 권한 확인의 답으로 처리될 수 있었다. 이 경우 내용을 읽지 않은 작업이 승인되거나 거절될 수 있다. v2.1.318 이상으로 업데이트한다. 업데이트 전에는 메시지를 보낸 뒤 이어서 타이핑하지 말고, 확인 창이 뜨면 내용을 읽고 답한다.

- 근거 policy · 처음 2026-11-06 · 최근 확인 2026-11-06 · 재검토 2026-12-06 · 검증 공식 출처

## 출처
- ashwin-ant · 2026-11-06 · https://github.com/anthropics/claude-code/releases/tag/v2.1.318
  > Fixed permission prompts being answered by keys typed just after sending a message
