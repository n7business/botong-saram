# API로 클로드 같은 AI를 붙여 자체 챗봇을 만들었다면 claude.ai에서 써 본 느낌대로 동작할 거라고 기대하지 말고, 하지 말아야 할 답을 시스템 프롬프트에 직접 적은 뒤 그 설정 그대로 다시 시험해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

같은 모델이라도 시스템 프롬프트가 붙는 claude.ai와 모델을 그대로 부르는 API는 다르게 답합니다. 앤트로픽 시험에서 Claude Fable 5.1은 두 환경 사이 적절 응답률 차이가 최대 34%p였고, 문제 행동을 막는 문장을 시스템 프롬프트에 넣었더니 API 60%에서 claude.ai 94%로 올랐습니다. 내 챗봇에서도 '없는 할인이나 환불을 약속하지 않는다'처럼 금지할 행동을 시스템 프롬프트에 분명히 적으세요. 시험은 실제 고객에게 열 구성 그대로(시스템 프롬프트, 연결 도구까지) 해야 하고, 프롬프트나 모델을 바꿀 때마다 다시 돌려야 합니다.

- 근거 observed · 처음 2026-11-20 · 최근 확인 2026-11-20 · 재검토 2026-12-20 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic · 2026-11-20 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > was as high as 34 percentage points.
