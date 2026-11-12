# Opus 4.8의 빠른 모드(fast mode)는 2026-10-30 지원 중단, 2026-11-30 제거되며 제거 후엔 일반 Opus 4.8로 대체되지 않고 오류만 나므로 그 전에 Opus 5.5로 옮긴다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

Claude Code 2.1.316 릴리스 노트에서 Opus 4.8 빠른 모드가 2026년 10월 30일부로 지원 중단(deprecated)되고 11월 30일에 제거된다고 공지했다. 제거 이후 Opus 4.8에 빠른 모드로 보내는 요청은 오류를 반환하며, 표준 Opus 4.8로 자동 전환되지 않는다. 빠른 모드를 켜 둔 채 자동화 스크립트나 예약 작업을 돌리면 11월 30일부터 매 턴 실패할 수 있다. 속도 이점을 유지하려면 모델을 Opus 5.5로 바꾸고, /fast 설정과 CLAUDE_CODE 환경변수·settings.json의 model 지정을 11월 30일 전에 점검한다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 공식 출처

## 출처
- anthropics · 2026-11-03 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21316
  > Deprecated fast mode for Opus 4.8 as of October 30, 2026; it will be removed on November 30, 2026.
