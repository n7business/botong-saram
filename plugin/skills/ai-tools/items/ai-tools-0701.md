# AI 답변을 AI에게 채점시킬 때는 답변을 만든 모델과 다른 모델을 채점에 쓰고, 채점 AI에게는 시험 설계 메모 없이 대화 내용만 보여 줘야 한다. AI는 자기가 쓴 글을 알아보고 더 좋게 평가하는 경향이 있기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

클로드로 만든 챗봇의 답은 다른 회사 모델로 채점하거나 그 반대로 하는 식으로, 만든 모델과 채점하는 모델을 나눕니다. 채점 AI에게 '이건 사기 유도 시나리오다' 같은 설계 정보까지 주면 그 정보 때문에 판단이 기울 수 있으니 대화 기록만 넘겨야 합니다.

- 근거 consensus · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-23 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > model graders have been shown to recognize and favor their own outputs.
