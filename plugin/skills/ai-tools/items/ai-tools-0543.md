# 클로드 코드의 CLAUDE.md처럼 세션마다 자동으로 불러오는 지시 파일은 짧게 유지하고 세부 내용은 별도 파일로 옮겨 링크만 남겨야 한다. 지시 파일이 길수록 지시를 덜 지키고, 그 안에 틀린 내용이 있으면 모든 세션에 그대로 따라 들어가기 때문이다.

🏛 공식 발표 · Anthropic Engineering 블로그

세션을 시작할 때마다 자동으로 들어가는 지시·메모는 매번 토큰을 씁니다. Anthropic은 클로드 코드 문서에서도 지시 파일이 길어지면 지시를 따르는 정도가 떨어진다고 경고합니다. 또 여기에 틀린 메모가 들어 있으면 모든 세션이 그 내용을 사실로 믿고 시작합니다. 항상 지켜야 할 핵심 규칙만 맨 위 파일에 두세요. 업무별 세부 요령은 별도 문서로 빼고 '자세한 내용은 ○○.md 참고' 같은 링크만 남기면 됩니다.

- 근거 policy · 처음 2026-11-14 · 최근 확인 2026-11-14 · 재검토 2026-12-14 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-14 · https://www.anthropic.com/research/components-of-agent-memory
  > our documentation on Claude Code warns that longer instruction files reduce adherence.
