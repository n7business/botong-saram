# 클로드 코드의 MEMORY.md는 세부 내용을 담는 곳이 아니라 '무엇을 알고 어디에 있는지'를 보여 주는 짧은 목차로 유지해야 한다. 매 세션에는 앞쪽 200줄 또는 25KB까지만 불러오고, 지침 파일이 길수록 AI가 지침을 덜 따르기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

클로드 코드의 자동 메모리는 세션마다 MEMORY.md의 앞쪽 200줄 또는 25KB까지만 불러옵니다. 그 뒤에 적은 내용은 자동으로 읽히지 않습니다. Anthropic 문서도 지침 파일이 길어질수록 AI가 지침을 덜 지킨다고 경고합니다. 또 맨 위에 적어 둔 메모리는 매 세션에 들어가므로, 거기 틀린 메모가 있으면 모든 작업에 그 오류가 따라갑니다. 그래서 MEMORY.md에는 한 줄짜리 항목과 세부 파일 링크만 두고, 자세한 내용은 따로 파일로 내려 두는 것이 좋습니다.

- 근거 policy · 처음 2026-11-24 · 최근 확인 2026-11-24 · 재검토 2026-12-24 · 검증 공식 출처

## 출처
- Anthropic Engineering · 2026-11-24 · https://www.anthropic.com/research/components-of-agent-memory
  > It loads only the first 200 lines or 25 KB of MEMORY.md.
