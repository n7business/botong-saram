# 챗봇이 손님 말투나 요청 수위에 따라 어떻게 달라지는지 보려면, 말투와 수위를 묶어서 바꾸지 말고 수위마다 모든 말투를 하나씩 짝지어 시험해야 한다. 한쪽으로 묶어 두면 어떤 요인 때문에 답이 달라졌는지 가려낼 수 없기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

예를 들어 심각한 요청은 모두 다급한 말투로, 가벼운 요청은 모두 짜증 섞인 말투로만 시험하면, 챗봇이 실수했을 때 그 원인이 요청 수위인지 말투인지 알 수 없습니다. 수위 3단계 × 말투 3종류처럼 모든 조합을 만들어 시험합니다. 시스템 프롬프트를 바꾼 효과를 보고 싶을 때도 다른 조건은 그대로 두고 그것 하나만 바꿔 비교해야 합니다.

- 근거 consensus · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-23 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > You should also vary the dimensions you care about independently.
