# 매 세션 자동으로 읽히는 클로드 코드 MEMORY.md는 내용을 담지 말고 어디에 무엇이 있는지 알려 주는 목차로 짧게 유지해야 하는데, 앞쪽 200줄 또는 25KB까지만 불러오기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

클로드 코드의 자동 메모리는 MEMORY.md 전체가 아니라 앞쪽 200줄 또는 25KB까지만 세션 시작 때 불러옵니다. 매번 자동으로 들어가는 메모리는 토큰을 쓰고, 틀린 메모가 들어 있으면 모든 세션에 그 오류가 따라갑니다. Anthropic은 지시 파일이 길수록 잘 지키지 않는다고도 경고합니다. 따라서 MEMORY.md에는 한 줄짜리 목차만 두고 세부 내용은 개별 메모 파일로 내려 링크만 남기는 것이 좋습니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > It loads only the first 200 lines or 25 KB of MEMORY.md.
