# 시스템 프롬프트나 CLAUDE.md에 '답변 N단어 이내' 같은 출력 길이 제한을 넣으면 코딩 품질이 측정 가능하게 떨어진다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic이 Claude Code 시스템 프롬프트에 '도구 호출 사이 텍스트 25단어 이내, 최종 응답 100단어 이내' 지시를 넣었더니 평가 점수가 Opus 4.6·4.7 모두 3% 하락했고, 4일 만에 되돌렸다. 여러 주 내부 테스트에서는 잡히지 않았고, 한 줄씩 빼보는 ablation으로 더 넓은 평가를 돌린 뒤에야 드러났다. 자기 CLAUDE.md나 커스텀 시스템 프롬프트에 길이 제한을 넣고 있다면 빼고 결과를 비교해 본다. 간결함이 필요하면 출력을 후처리하거나 요약을 따로 요청하는 편이 안전하다. 프롬프트를 바꿀 때는 한 줄씩 추가·제거하며 같은 작업 묶음으로 전후 결과를 비교한다.

- 근거 observed · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-03 · https://www.anthropic.com/research/april-23-postmortem
  > One of these evaluations showed a 3% drop for both Opus 4.6 and 4.7.
