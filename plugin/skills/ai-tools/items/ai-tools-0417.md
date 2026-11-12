# AI가 남기는 업무 메모에는 규칙만 적지 말고 그 규칙이 맞는지 어떻게 알았는지, 확인된 것인지 아직 추측인지, 빠지기 쉬운 함정까지 함께 적게 해야 다음 작업에서 틀린 추측을 사실로 믿지 않는다.

🏛 공식 발표 · Anthropic Engineering 블로그

실험에서 메모리를 가장 잘 쓴 모델은 규칙과 함께 그 규칙이 참이라는 근거, 앞선 질문의 답, 발견한 함정에 대한 경고를 남겼습니다. 성능이 낮은 모델의 메모는 검증하지 않은 추측을 여러 파일에 흩어 둔 수준이었습니다. Opus 4.7은 메모를 참고 문서 하나로 모으고 확인한 사실과 아직 확인하지 않은 사실을 나눠 표시하기 시작했습니다. AI에게 업무 노트를 맡길 때도 '확인됨/미확인'과 근거를 함께 적게 하면 다음 세션에서 메모를 믿어도 될지 판단할 수 있습니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > began marking which facts it had checked and which were still unconfirmed
