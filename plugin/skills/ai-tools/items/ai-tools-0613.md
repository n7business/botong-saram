# 큰 개발 작업을 AI에게 단계별로 맡길 때는 각 단계를 시작하기 전에 '무엇이 되면 완료인지'를 검사 가능한 항목으로 먼저 정해 두고, 검토할 때 그 항목대로 하나씩 확인하게 해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

앤트로픽 실험에서는 코드를 쓰기 전에 만드는 AI가 무엇을 만들고 어떻게 확인할지 제안했습니다. 검토하는 AI는 그 제안이 맞는지 보고, 둘이 합의할 때까지 고친 뒤에야 작업을 시작했습니다. 이 '완료 기준 합의'는 큰 그림만 적은 기획서와 실제로 시험할 수 있는 구현 사이를 이어 줍니다. 한 단계에 검사 항목이 27개나 될 만큼 잘게 나눴고, 덕분에 검토 결과가 추가 조사 없이 바로 고칠 수 있을 만큼 구체적이었습니다.

- 근거 observed · 처음 2026-11-19 · 최근 확인 2026-11-19 · 재검토 2026-12-19 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic · 2026-11-19 · https://www.anthropic.com/research/harness-design-long-running-apps
  > agreeing on what "done" looked like for that chunk of work before any code was written.
