# 클로드 코드 예약 작업은 컴퓨터가 꺼져 있어도 돌아가야 하면 클라우드 예약으로, 내 컴퓨터의 파일과 도구가 필요하면 데스크톱 예약으로 만든다.

🏛 공식 발표 · Claude Code 공식 문서

클라우드 예약 작업은 클라우드에서 실행되므로 컴퓨터를 꺼도 계속 돌아가고, API 호출이나 GitHub 이벤트로 시작할 수도 있습니다. 웹, 데스크톱 앱 또는 CLI의 `/schedule`로 만듭니다. 데스크톱 예약 작업은 내 컴퓨터에서 실행되어 로컬 파일과 도구에 바로 접근합니다. CLI 세션 안에서 잠깐 상태를 반복 확인할 때는 `/loop`를 씁니다.

- 근거 policy · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/overview
  > run in the cloud, so they keep running even when your computer is off
- Anthropic · 2026-11-07 · https://code.claude.com/docs/en/overview
  > run on your machine, with direct access to your local files and tools
