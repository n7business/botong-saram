# AI 채점기를 믿기 전에 모범 답안을 직접 넣어 합격이 나오는지 먼저 확인해야 하고, 채점에 쓰는 AI 모델이 바뀌면 같은 답안의 점수가 그대로인지 다시 확인해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

AI 채점기는 고장이 나도 아무 경고 없이 점수를 계속 매길 수 있습니다. 바탕 모델이 바뀌면 전보다 엄하게 또는 후하게 채점하기도 합니다. 시험 질문마다 모범 답안을 준비해 두고 채점기에 넣어 합격이 나오는지 확인합니다. 점수가 갑자기 이상하게 나오면 챗봇보다 채점 설정을 먼저 의심해야 합니다. 채점 AI가 '확신이 낮다'고 표시한 건은 사람이 직접 읽어 봅니다.

- 근거 consensus · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-25 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > does a reference solution exist for every item, and does it pass your grader?
