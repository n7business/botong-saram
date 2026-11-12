# AI가 만든 위키가 있어도 원본 검색 기능을 끄지 말고 둘을 함께 쓰게 해야, 위키만 쓸 때보다 정답률이 높고 질문당 토큰도 아낄 수 있다.

🏛 공식 발표 · Anthropic Engineering 블로그, 조코딩 JoCoding

약 35만 개 파일로 한 실험에서 검색과 위키를 함께 쓰자 점수가 54%에서 61%로 올랐습니다. 검색만 쓴 경우는 53%, 위키만 쓴 경우의 최고 점수는 48%였습니다. 검색과 위키를 함께 쓰면 질문 하나에 토큰도 약 2만 개를 아꼈습니다. 위키는 원본을 대신하는 것이 아니라 원본을 찾아가는 지도로 쓰는 것이 좋습니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 독립 2곳 weight 1.7

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > Using search and the wiki also saved about 20,000 tokens per question.
- 조코딩 JoCoding · 2026-11-10 · https://www.youtube.com/watch?v=Ni0gE4LeSlc
  > 정리된 지식과 원본 검색을 함께 쓰는 것이 좋다.
