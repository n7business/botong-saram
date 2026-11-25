# 챗봇 지시문(시스템 프롬프트)을 고친 덕분에 답이 좋아졌는지 알려면, 다른 조건은 그대로 두고 같은 모델에 같은 시험 질문을 넣어 고치기 전과 후를 비교해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

모델 A와 모델 B의 점수 차이만 봐서는 점수가 왜 달라졌는지 알 수 없습니다. 특정 변경이 효과가 있었는지 알려면 한 번에 한 가지만 바꿔야 합니다. 예를 들어 같은 모델과 같은 질문 목록을 쓰고 지시문만 바꾼 두 버전을 나란히 시험합니다. 지시문과 모델을 동시에 바꾸면 어느 쪽 때문에 좋아졌는지 가려낼 수 없습니다.

- 근거 consensus · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-25 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > need a design that varies one variable at a time
