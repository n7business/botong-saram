# VS Code에서 클로드 코드 답변의 코드 블록을 복사해 터미널에 붙여 넣는다면 확장 프로그램을 v2.1.330 이상으로 업데이트해야 합니다. 이전 버전에서는 복사할 때 끝에 줄바꿈이 붙어서 붙여 넣는 순간 명령이 바로 실행됐습니다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

VS Code용 클로드 코드 확장 프로그램 이전 버전에서는 답변의 코드 블록을 복사하면 끝에 줄바꿈이 함께 복사됐습니다. 그래서 터미널에 붙여 넣기만 해도 Enter를 누른 것처럼 명령이 실행됐습니다. 이 문제는 v2.1.330에서 고쳐졌습니다. 업데이트하기 전에는 텍스트 편집기 같은 곳에 먼저 붙여 넣어 명령 내용을 확인한 뒤 터미널로 옮기세요. 삭제나 배포처럼 되돌리기 어려운 명령은 특히 조심해야 합니다.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- anthropics · 2026-11-23 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > copying a code block adding a trailing newline that ran the command on paste
