# 고객 응대 챗봇은 질문 한 개씩만 던져 시험하지 말고 여러 번 주고받는 대화로 시험해야 하며, 대화 도중 한 번이라도 부적절하게 답했다면 그 대화 전체를 불합격으로 세야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

곤란한 요구는 첫 메시지에서 드러나지 않고 대화가 이어지면서 조금씩 수위가 올라가는 경우가 많습니다. 그래서 첫 질문에는 잘 대응한 챗봇도 다섯 번째 메시지쯤에서 무너질 수 있습니다. 손님이 앞에서 한 말 때문에 뒤에 나온 평범한 질문을 더 조심해서 다뤄야 하는 경우도 있습니다. 시험은 여러 번 주고받는 대화로 하고, 끝까지 적절하게 대응한 대화만 합격으로 셉니다.

- 근거 consensus · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-25 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > a model that handles the first message well may respond inappropriately by the fifth.
