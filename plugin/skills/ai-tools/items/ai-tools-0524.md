# 클로드 코드의 답변이 길어 읽기 번거롭다면 /output-style에서 Concise를 고르면 되는데, 결과부터 말하고 군더더기를 빼면서도 오류 보고·보안 경고·삭제 확인은 그대로 다 보여 준다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

Concise 스타일에서는 답변 첫 문장이 무슨 일이 일어났는지, 또는 답이 무엇인지 바로 말합니다. 서론과 단계별 진행 설명, 끝 요약을 빼고, 간단한 질문에는 1~3문장으로 답하지만 작업 자체는 기본 스타일만큼 꼼꼼히 합니다. 오류 보고, 실패한 테스트 출력, 보안 경고, 파괴적 작업 확인처럼 안전하게 판단하는 데 필요한 내용은 줄이지 않습니다. 출력이 짧아지니 출력 토큰도 줄어듭니다. 반대로 Explanatory와 Learning 스타일은 설명을 덧붙여 출력 토큰이 늘어납니다. Concise는 v2.1.237 이상에서 쓸 수 있습니다.

- 근거 policy · 처음 2026-11-13 · 최근 확인 2026-11-13 · 재검토 2026-12-13 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-13 · https://code.claude.com/docs/en/output-styles
  > Responses lead with the result and leave out preamble, narration, and recaps
