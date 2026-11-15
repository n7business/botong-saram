# AI Gateway의 guardrails(혐오·폭력·프롬프트 인젝션 검사)는 다른 기능과 달리 모든 요청에 검사용 AI 모델을 돌려 Workers AI 요금이 붙으므로, 늘 켜 두지 말고 필요할 때만 켜야 한다.

👤 출처 1곳 · 노마드 코더 Nomad Coders

Firewall에서 guardrails를 켜면 메시지가 모델에 닿기 전과 답이 고객에게 가기 전에 Meta의 Llama Guard가 실행되어 혐오·폭력·탈옥 시도 등을 표시하거나 차단합니다. 고급 설정에서는 폭력 범죄·혐오·자해·프롬프트 인젝션 같은 카테고리마다 입력·출력 각각에 무시/표시/차단을 고를 수 있습니다. 다만 AI Gateway에서 이 기능만 유료이고, 요청마다 검사 모델이 돌아가 비용이 늘어납니다. 고객이 자유롭게 글을 입력하는 공개 챗봇처럼 위험이 큰 곳에만 켜는 것이 현실적입니다.

- 근거 anecdote · 처음 2026-11-16 · 최근 확인 2026-11-16 · 재검토 —

## 출처
- 노마드 코더 Nomad Coders · 2026-11-16 · https://www.youtube.com/watch?v=f1quywzT-a8
  > So turn it on when you need it.
