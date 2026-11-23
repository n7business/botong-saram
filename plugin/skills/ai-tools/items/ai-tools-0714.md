# VS Code에서 클로드 코드의 /rewind를 쓴다면 v2.1.330 이상으로 업데이트해야 합니다. 이전 버전에서는 Enter를 길게 누르거나 삭제 버튼을 두 번 빠르게 누르면 확인 창 없이 파일이 되돌려지거나 메모리·MCP 서버가 지워졌습니다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

VS Code용 클로드 코드 이전 버전에는 확인 단계가 건너뛰어지는 문제가 있었습니다. /rewind에서 Enter를 누르고 있으면 확인 없이 파일이 복원됐습니다. 메모리·MCP 서버·플러그인 마켓플레이스의 Remove나 Delete 버튼을 두 번 빠르게 눌러도 확인 없이 삭제됐습니다. 이 문제는 v2.1.330에서 고쳐졌습니다. 업데이트 전에는 이런 버튼을 한 번씩 천천히 누르고, 되돌리기 전에 먼저 Git 커밋을 해 두는 것이 안전합니다.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- anthropics · 2026-11-23 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > holding Enter on `/rewind` restoring files ... without confirmation
