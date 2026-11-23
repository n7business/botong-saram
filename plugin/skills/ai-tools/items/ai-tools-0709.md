# 클로드 코드 설치 명령이 끝나면 새 터미널 창을 열어 claude --version을 실행해 버전 번호가 나오는지 확인해야 한다. 'claude를 찾을 수 없다'는 메시지가 나오면 설치 폴더가 PATH에 등록되지 않은 것이다.

🏛 공식 발표 · Claude Code 공식 문서

설치 명령은 내려받는 동안 진행 표시가 없어서 멈춘 것처럼 보일 수 있습니다. 설치가 끝나면 이미 열려 있던 창이 아니라 새 터미널 창을 열고 claude --version을 입력하세요. 버전 번호가 나오면 정상입니다. 'claude' isn't found 같은 메시지가 나오면 공식 문서의 Fix your PATH 안내를 따라 PATH를 고쳐야 합니다. 윈도우에서 '&&'가 올바른 구분자가 아니라는 오류가 나오면 지금 창이 PowerShell이라는 뜻이고, 'irm'을 인식하지 못한다는 오류가 나오면 CMD라는 뜻입니다. 이때는 그 창에 맞는 설치 명령을 다시 실행하세요.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-23 · https://code.claude.com/docs/en/quickstart
  > open a new terminal window and run `claude --version`
