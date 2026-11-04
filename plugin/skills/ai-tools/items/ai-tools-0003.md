# AI 코드 리뷰를 시킬 때 변경 파일만 주지 말고 연관 저장소·의존 코드까지 맥락으로 주고 최신 모델을 쓰면 놓치던 버그를 잡는다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic이 사람 리뷰·단위 테스트·E2E 테스트·내부 사용을 모두 통과한 버그(사고 후 발견)에 대해 Code Review를 사후 테스트했다. 관련 저장소를 모두 맥락으로 제공했을 때 Opus 4.7은 버그를 찾았고 Opus 4.6은 못 찾았다. 외주 개발 결과물이나 자기 코드를 AI로 검수할 때는 diff 하나만 붙이지 말고, 호출하는 라이브러리·API 계약·연관 레포를 함께 열어 준다. 모델은 가능한 최신 세대를 쓴다. 단일 사례 기반이므로 AI 리뷰는 사람 검토를 대체하지 않고 보조로 쓴다.

- 근거 observed · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-03 · https://www.anthropic.com/research/april-23-postmortem
  > When provided the code repositories necessary to gather complete context, Opus 4.7 found the bug, while Opus 4.6 didn't.
