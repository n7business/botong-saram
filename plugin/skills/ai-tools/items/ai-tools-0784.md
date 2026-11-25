# 윈도우에서 클로드 코드 설치 명령을 넣었는데 'The token '&&' is not a valid statement separator' 오류가 나오면 지금 창이 CMD가 아니라 PowerShell이므로 PowerShell용 설치 명령(irm https://claude.ai/install.ps1 | iex)을 써야 하고, ''irm'은 내부 또는 외부 명령이 아닙니다' 오류가 나오면 반대로 CMD용 명령을 써야 한다.

🏛 공식 발표 · Claude Code 공식 문서

윈도우 설치 명령은 PowerShell용과 CMD용이 따로 있습니다. 입력줄 앞에 'PS C:\'가 보이면 PowerShell이고, 'PS' 없이 'C:\'만 보이면 CMD입니다. CMD용 명령을 PowerShell에 넣으면 '&&' 관련 오류가 나고, PowerShell용 명령을 CMD에 넣으면 'irm'을 알 수 없다는 오류가 납니다. 이런 오류가 나와도 설치 파일이 망가진 것이 아니니, 지금 쓰는 창에 맞는 명령으로 다시 실행하면 됩니다.

- 근거 policy · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 2026-12-25 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-25 · https://code.claude.com/docs/en/overview
  > If you see `The token '&&' is not a valid statement separator`, you're in PowerShell, not CMD.
