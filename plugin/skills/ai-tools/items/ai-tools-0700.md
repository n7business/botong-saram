# AI에게 두 답변 중 더 나은 것을 고르게 할 때는 순서를 바꿔 한 번 더 물어야 하고, 길이가 긴 답변에 점수가 쏠리지 않는지 확인해야 한다. 채점 AI는 먼저 보여 준 답과 긴 답을 더 좋게 보는 경향이 있기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

두 모델이나 두 프롬프트의 답을 나란히 놓고 AI에게 고르게 하면, 내용과 상관없이 먼저 나온 쪽이나 더 긴 쪽이 이기는 경우가 생깁니다. 같은 비교를 A·B 순서를 뒤집어 다시 돌리고, 두 번 모두 같은 쪽이 이겼을 때만 결과를 믿습니다. 점수가 답변 길이와 함께 오르내리는지도 살펴봐야 합니다.

- 근거 consensus · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-23 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > Graders also favor longer responses and the first option they are shown in a pairwise comparison
