# 클로드 코드 Remote Control을 worktree 모드로 쓰고 있다면 v2.1.327 이상으로 업데이트해야 한다. 이전 버전에서는 서버를 멈추면 실행 중인 세션의 .env 같은 git 제외 파일이 지워지는 문제가 있었기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

Remote Control을 worktree 모드로 켜 두고 폰 등에서 작업을 이어 하는 경우가 해당됩니다. v2.1.327 이전에는 서버를 멈출 때 실행 중이던 세션 폴더에서 git이 추적하지 않는 파일(.gitignore에 넣은 파일)이 함께 지워질 수 있었습니다. 대표적인 예가 API 키나 비밀번호를 넣어 두는 .env 파일입니다. 이런 파일은 git에도 없어서 한번 지워지면 되살리기 어렵습니다. claude --version으로 버전을 확인해 업데이트하고, .env 같은 설정 파일은 따로 백업해 두세요.

- 근거 policy · 처음 2026-11-19 · 최근 확인 2026-11-19 · 재검토 2026-12-19 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-19 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > Fixed stopping the server in worktree mode deleting a running session's git-ignored files, such as `.env`
