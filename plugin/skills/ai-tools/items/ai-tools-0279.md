# 매 세션 자동으로 불러오는 AI 메모와 지시문은 짧은 색인으로 유지하고 세부 내용은 아래 파일로 내려 링크만 남겨야, 토큰 낭비와 지시 불이행을 줄일 수 있다.

🏛 공식 발표 · Anthropic Engineering 블로그

세션 시작 때 자동으로 불러오는 메모는 토큰을 쓰고, 틀린 메모가 있으면 모든 세션으로 옮겨 갑니다. 불러왔다고 해서 Claude가 반드시 따르는 것도 아니며, Claude Code 문서는 지시 파일이 길수록 준수도가 떨어진다고 경고합니다. Claude Code의 자동 메모리는 MEMORY.md의 처음 200줄 또는 25KB만 불러오고, 이 부분을 무엇을 어디서 찾을지 보여 주는 색인으로 씁니다. 내 메모리 파일도 맨 위에는 자주 쓰는 내용과 링크만 두고, 긴 설명은 별도 파일로 옮기는 편이 좋습니다.

- 근거 consensus · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-07 · https://www.anthropic.com/research/components-of-agent-memory
  > longer instruction files reduce adherence
