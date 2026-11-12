# 계약서 여러 건을 AI에게 정리시켜 자료집을 만들 때는 여러 AI가 표 하나에 함께 요약해 넣게 하지 말고, 계약서마다 한 AI가 페이지를 따로 맡아 조건을 원문 그대로 옮기게 해야 중요한 조건이 빠지지 않는다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic이 시험해 보니, 여러 에이전트가 계약 조건 표 하나에 동시에 쓰게 했을 때는 서로 쓴 내용을 덮어써서 채점 대상 사실 57개 중 41개(72%)만 남았습니다. 계약서마다 에이전트 하나가 페이지를 따로 맡고 조건을 요약 없이 원문 그대로 옮기게 바꾸자 57개가 모두 남았습니다. 계약 조건·약관·고시처럼 문구 하나가 결론을 바꾸는 자료는 AI에게 '요약해 줘'보다 '해당 조항을 그대로 옮겨 줘'라고 맡겨야 합니다. 여러 AI를 한꺼번에 돌릴 때는 같은 파일이나 표를 동시에 고치지 않도록 각자 맡을 범위를 나눠 주십시오.

- 근거 observed · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-11 · https://www.anthropic.com/research/components-of-agent-memory
  > quoted the terms word for word rather than summarizing them into a shared table
