# Pro·Max·Team 같은 구독 요금제에서 클로드 코드 빠른 모드를 켜면 요금제 사용량이 남아 있어도 추가 사용 크레딧에서 바로 돈이 나가므로, 켜기 전에 크레딧 결제 설정을 확인해야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

구독 요금제에서 빠른 모드는 요금제 기본 사용량에 포함되지 않습니다. 추가 사용 크레딧(usage credits)을 켜 두어야만 쓸 수 있고, 사용량은 그 크레딧에서 차감됩니다. 요금제 사용량이 남아 있어도 빠른 모드 사용분은 크레딧에서 바로 빠져나갑니다. 개인 요금제는 claude.ai의 Settings > Usage에서 이번 달 크레딧 사용액을 확인할 수 있지만, 빠른 모드 금액이 따로 표시되지는 않습니다. Team 요금제는 소유자가 먼저 빠른 모드를 허용해야 하고, 사용분은 조직 크레딧에서 나갑니다.

- 근거 policy · 처음 2026-11-09 · 최근 확인 2026-11-09 · 재검토 2026-12-09 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-09 · https://code.claude.com/docs/en/fast-mode
  > Fast mode usage draws directly from usage credits, even if you have remaining usage on your plan.
