# AI 도구 품질 이상은 막연한 불만 대신 /feedback 명령이나 재현 가능한 구체 예시로 보고해야 실제 수정으로 이어진다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic은 두 차례 사고 모두 초기 보고가 '정상적인 피드백 변동'과 구분되지 않아 조사 착수가 늦었다고 밝혔다. 결국 원인 확인을 가능하게 한 것은 /feedback 명령으로 보낸 신고와 온라인에 올라온 구체적·재현 가능한 예시였다. 개인정보 보호 정책상 엔지니어는 신고되지 않은 대화를 열어볼 수 없으므로, 신고하지 않은 문제는 조사 대상이 되지 않는다. 이상을 느끼면 세션 안에서 /feedback으로 즉시 보내고, 가능하면 입력·출력·버전·시각을 함께 적는다. 공식 설명은 X의 ClaudeDevs 계정과 GitHub 스레드에서 확인한다.

- 근거 consensus · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-03 · https://www.anthropic.com/research/april-23-postmortem
  > the people who used the /feedback command to share their issues with us
