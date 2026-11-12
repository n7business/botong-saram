# 파일을 수십 개 읽는 조사 작업이나 컨텍스트가 차오를 때는 메인 대화에서 직접 시키지 말고 서브에이전트로 보내 요약만 받는다.

🏛 공식 발표 · Claude Code 공식 문서

서브에이전트는 별도 컨텍스트 창에서 돌고 메인 대화에는 요약만 돌아온다. 그래서 많은 파일을 읽거나 광범위 검색을 하는 작업을 서브에이전트로 보내면 메인 컨텍스트가 소모되지 않는다. 결과물만 필요하고 중간 과정을 다시 볼 일이 없는 작업에 특히 적합하다. 반대로 메인 대화에 계속 남아야 하는 참고 지식은 스킬로 로드하는 게 맞다. 서브에이전트 몇 개로 감당이 안 되는 규모(코드베이스 전체 감사 등)는 동적 워크플로를 쓴다.

- 근거 policy · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03

## 출처
- Anthropic (Claude Code Docs) · 2026-11-03 · https://code.claude.com/docs/en/features-overview
  > Use a subagent when you need context isolation or when your context window is getting full.
