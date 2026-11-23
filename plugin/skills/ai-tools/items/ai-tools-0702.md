# 챗봇 답변을 '예'라는 단어가 있는지 같은 글자 찾기로 자동 채점할 때는, 정중하게 거절한 답까지 '수락'으로 잘못 세지 않는지 표본을 직접 읽어 확인해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

답변에서 '예/아니오'나 특정 단어만 뽑아 맞고 틀림을 정하는 방식은 빠르고 객관적이지만 맥락을 놓칩니다. 예를 들어 '네, 기꺼이 돕겠지만 이 요청은 어렵습니다'라는 답이 '예'로 집계될 수 있습니다. 정답이 분명한 항목에만 글자 찾기를 쓰고, 해석이 필요한 항목은 AI 채점이나 사람 검토로 넘기며, 각 문항의 모범 답안이 그 채점 방식을 통과하는지도 먼저 확인합니다.

- 근거 consensus · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-23 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > pattern matching, such as extracting a “Yes” or “No” from the response, can miss nuance.
