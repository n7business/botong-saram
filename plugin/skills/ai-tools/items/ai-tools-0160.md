# claude -p로 예약 작업을 돌린다면 claude auth status로 저장된 claude.ai 로그인의 만료일을 확인하고 표준 오류 경고까지 로그에 남겨야, 로그인 만료로 작업이 멈추기 전에 대비할 수 있다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

Claude Code v2.1.318부터 claude auth status에 저장된 claude.ai 로그인의 만료일(loginExpiresAt)이 표시된다. claude -p의 JSON 결과에는 credential_expires_at으로 나온다. 텍스트 출력에서는 만료 10일 전부터 표준 오류(stderr)로 한 줄 경고가 나오므로, 표준 출력만 저장하는 스크립트에서는 이 경고를 놓칠 수 있다. 만료일을 점검 항목에 넣고 stderr도 로그에 남긴다. 만료되면 claude -p의 오류 메시지가 안내하는 claude auth login 또는 claude setup-token으로 조치한다.

- 근거 policy · 처음 2026-11-06 · 최근 확인 2026-11-06 · 재검토 2026-12-06 · 검증 공식 출처

## 출처
- ashwin-ant · 2026-11-06 · https://github.com/anthropics/claude-code/releases/tag/v2.1.318
  > Added a one-line stderr warning to `claude -p` text output, starting 10 days before a stored claude.ai sign-in ends
