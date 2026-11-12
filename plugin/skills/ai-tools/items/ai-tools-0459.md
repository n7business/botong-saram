# 클로드 코드를 claude -p로 무인 자동 실행하면서 자동 모드를 쓴다면 stderr 로그에 '이 세션은 무료 분류기 요청 대상이 아니다' 안내가 찍혔는지 확인해야 하는데, 이 경우 작업은 멈추지 않고 그대로 이어지면서 분류기 요청이 토큰 사용량으로 과금되기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

자동 모드에서는 명령 실행 전에 분류기가 안전한지 검사하고, 서버 측 검사가 켜져 있으면 이 검사는 무료입니다. 대화형 화면에서는 안내가 뜨면 Enter로 승인해야 진행되지만, claude -p 같은 비대화형 실행에서는 묻지 않고 같은 문구를 stderr에 출력한 뒤 자동 모드로 계속 돕니다. 그래서 예약 작업이나 수집 스크립트로 돌리면 분류기 비용이 붙는 것을 모르고 지나치기 쉽습니다. 실행 로그에 stderr를 남겨 두고 해당 문구가 있는지 주기적으로 확인하세요. Agent SDK 앱이라면 stream-json 출력의 system 경고 메시지로도 읽을 수 있습니다.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-11 · https://code.claude.com/docs/en/auto-mode-classifier-billing
  > In non-interactive mode with -p it prints the text to stderr
