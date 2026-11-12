# 구형이나 저렴한 AI 모델에 메모리를 맡길 때는 답하기 전에 메모 파일을 먼저 읽고 추측을 직접 확인하라고 명시해야, 메모리가 있어도 쓰지 않아 생기는 성능 손실을 줄일 수 있다.

🏛 공식 발표 · Anthropic Engineering 블로그

Sonnet 4.6은 메모리 폴더를 자주 읽지 않았고, 답이 틀린 이유에 대한 추측도 직접 확인하지 않았습니다. 답하기 전에 메모 파일을 읽고 추측을 확인하라고 지시하자 벤치마크 점수가 거의 두 배가 되었습니다. 최신 모델인 Sonnet 5는 지시 없이도 10번 중 9번 메모리를 먼저 읽었습니다. 비용 때문에 낮은 등급 모델을 쓴다면 메모리를 읽고 확인하는 절차를 지시문에 넣는 것이 좋습니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > nearly doubled its benchmark score
