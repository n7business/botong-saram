# 최신 Claude 모델에는 메모리에 무엇을 적을지 고정 규칙을 주지 말고 메모리의 용도만 알려 줘야, 메모리로 얻는 성능 향상을 잃지 않는다.

🏛 공식 발표 · Anthropic Engineering 블로그

CL-Bench 데이터베이스 과제에서 Anthropic은 메모리 폴더가 있다는 사실만 알려 주었고, Opus 4.7과 Opus 5는 그것만으로 메모리를 잘 활용해 성능이 눈에 띄게 올랐습니다. 반면 '실패만 기록하라'는 규칙을 주자 두 모델 모두 메모리로 얻던 향상분의 상당 부분을 잃었습니다. Anthropic은 최신 모델에 '사람이 요청하거나 분명히 기억할 가치가 있을 때 메모를 남기라' 정도의 간단한 안내만 주고 판단은 모델에 맡긴다고 밝혔습니다. 다만 이 결과는 해당 벤치마크와 규칙을 시험한 것이므로, 구형 모델에는 그대로 적용되지 않을 수 있습니다.

- 근거 observed · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-07 · https://www.anthropic.com/research/components-of-agent-memory
  > tell Claude what memory is for, but not how to use it
