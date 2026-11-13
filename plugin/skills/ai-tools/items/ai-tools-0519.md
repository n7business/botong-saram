# 클로드 구독 요금제에서 클로드 코드 fast mode를 켜면 요금제 사용량이 남아 있어도 추가 결제인 사용 크레딧에서 바로 빠지므로, 켜기 전에 크레딧 결제 설정을 확인하고 급한 대화형 작업에만 /fast를 쓴 뒤 끝나면 꺼야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

fast mode는 같은 모델을 최대 2.5배 빠르게 돌리는 대신 토큰당 요금이 더 비쌉니다. Pro·Max·Team·Enterprise 같은 구독 요금제에서는 구독 사용량 한도에 포함되지 않고, 요금제 바깥의 사용 크레딧으로만 쓸 수 있습니다. 공식 문서는 '요금제 사용량이 남아 있어도 fast mode 사용량은 사용 크레딧에서 바로 빠진다'고 밝힙니다. 실시간 디버깅처럼 응답 속도가 중요한 작업에만 /fast로 켜고, 비용이 더 중요할 때는 꺼 두세요. 쓴 금액은 claude.ai의 Settings > Usage에서 확인할 수 있지만, fast mode 사용분이 따로 나뉘어 표시되지는 않습니다.

- 근거 policy · 처음 2026-11-13 · 최근 확인 2026-11-13 · 재검토 2026-12-09 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-13 · https://code.claude.com/docs/en/fast-mode
  > Fast mode usage draws directly from usage credits, even if you have remaining usage on your plan.
