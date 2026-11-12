# 윈도우에서 클로드 코드를 설치할 때는 프롬프트가 PS C:\로 시작하는지 먼저 보고 PowerShell용과 CMD용 설치 명령 중 맞는 것을 넣어야 하는데, 다른 쪽 명령을 넣으면 오류가 나기 때문이다.

🏛 공식 발표 · Claude Code 공식 문서

윈도우 설치 명령은 PowerShell용과 CMD용이 따로 있습니다. 프롬프트가 PS C:\로 시작하면 PowerShell이고, PS 없이 C:\로 시작하면 CMD입니다. 'The token '&&' is not a valid statement separator' 오류가 나오면 CMD용 명령을 PowerShell에 넣은 것입니다. ''irm' is not recognized' 오류가 나오면 PowerShell용 명령을 CMD에 넣은 것입니다. 그 밖의 오류는 공식 설치 문제 해결 문서에서 오류 문구로 찾아보면 됩니다.

- 근거 policy · 처음 2026-11-12 · 최근 확인 2026-11-12 · 재검토 2026-12-12 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-12 · https://code.claude.com/docs/en/overview
  > On Windows, your prompt shows `PS C:\` when you're in PowerShell
