# 클로드 코드를 API 키나 게이트웨이로 쓰다가 auto mode에서 '이 세션은 무료 분류기 요청 대상이 아니다'라는 안내가 뜨면 auto mode의 안전 검사 요청이 내 토큰 사용량으로 청구된다는 뜻이므로, /status에서 Auto mode server 줄을 확인하고 중간에 있는 게이트웨이나 프록시부터 점검해야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

auto mode는 셸 명령이나 네트워크 요청을 실행하기 전에 분류기로 검사하는데, 서버 쪽 검사가 켜진 곳에서는 이 검사가 무료입니다. 이 안내가 뜬다면 서버 검사가 세션에 닿지 않아 클로드 코드가 검사 요청을 직접 보내고 있고, 그 요청이 토큰 사용량으로 청구된다는 뜻입니다. 흔한 원인은 클로드 코드와 API 사이에 있는 LLM 게이트웨이나 프록시입니다. 게이트웨이를 직접 운영하지 않는다면 관리자나 업체에 anthropic-beta 헤더와 safeguards 필드를 그대로 넘겨 달라고 요청하세요. Pro·Max·Ultra·Team 요금제에서는 이 안내가 뜨지 않습니다. 세션 상태는 /status의 Auto mode server 줄에서 확인할 수 있으며, Enabled면 서버 검사, Disabled면 자체 검사로 돌아간 상태입니다.

- 근거 policy · 처음 2026-11-14 · 최근 확인 2026-11-14 · 재검토 2026-12-10 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-14 · https://code.claude.com/docs/en/auto-mode-classifier-billing
  > On a Pro, Max, Ultra, or Team plan, you never see the notice.
