# 클로드 코드 세션 여러 개를 worktree로 나눠 동시에 돌리고 있다면 v2.1.330 이상으로 업데이트해야 한다. 이전 버전에서는 한 세션에서 worktree를 닫을 때 다른 세션이 아직 작업 중인 worktree까지 지워질 수 있었기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

이전 버전에서는 ExitWorktree나 worktree 종료 확인창이 다른 클로드 코드 세션이 쓰고 있는 worktree까지 삭제하는 문제가 있었고, v2.1.330에서 고쳐졌다. 세션을 여러 개 열어 기능별로 나눠 작업한다면 아직 커밋하지 않은 작업이 통째로 사라질 수 있었다는 뜻이다. claude --version으로 버전을 확인하고 업데이트해야 한다. 업데이트한 뒤에도 세션마다 작업 중간중간 커밋해 두는 습관을 들이는 게 안전하다.

- 근거 policy · 처음 2026-11-21 · 최근 확인 2026-11-21 · 재검토 2026-12-21 · 검증 공식 출처

## 출처
- anthropics (Anthropic) · 2026-11-21 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > Fixed `ExitWorktree` and the worktree exit dialog deleting a worktree that another running Claude Code session was working in
