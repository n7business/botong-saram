# 챗봇을 시험할 때는 실제로 손님에게 내보낼 때와 같은 지시문·도구 연결·채널 설정으로 돌려야 한다. 같은 모델이라도 도구를 쓸 수 있는지, 기본 지시문을 쓰는지에 따라 곤란한 요청을 들어주는 정도가 달라지기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

API에서 맨 모델로만 시험하고 통과했다고 안심하면 안 됩니다. 실제 손님이 쓰는 홈페이지 채팅창, 카카오톡 채널, 연결된 예약·조회 도구 같은 설정을 그대로 갖춰서 시험해야 합니다. 외국인 손님을 받는다면 손님이 쓰는 언어로도 따로 시험합니다. Anthropic은 단발 질문 시험을 7개 언어와 여러 제품 화면에서 돌리고 있습니다.

- 근거 consensus · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-25 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > match the eval setup to the deployment you want to test.
