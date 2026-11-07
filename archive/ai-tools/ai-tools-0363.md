---
id: ai-tools-0363
domain: ai-tools
claim: 클로드 코드 규칙을 나눌 때 테스트·CSS·API처럼 파일 종류별 규칙은 .claude/rules의 주제별 파일에 적용 경로를 지정해
  넣고 기능·폴더별 지침은 하위 CLAUDE.md에 넣어야, 관계없는 작업에 그 규칙이 로드되지 않는다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=G1JxVbTmCEc
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 결론부터 말하면 둘 다 쓰는게 최적입니다.
  source: 짐코딩 (@gymcoding)
- url: https://www.youtube.com/watch?v=FBv8hK_DtJ8
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 각 파일 맨 위에 조건을 설정할 수 있습니다.
  source: 짐코딩 (@gymcoding)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- CLAUDE.md
- rules
- 메모리
mentions: 2
---
조건부 규칙은 특정 종류의 파일을 작업할 때 로드되고, 하위 CLAUDE.md는 그 폴더에 접근할 때 로드됩니다. '테스트 파일 작성 시 반드시 이 라이브러리를 써라'는 파일 종류 기준이므로 조건부 규칙에 넣습니다. '결제 모듈은 이 외부 라이브러리를 쓰고 이 순서로 처리해라'는 폴더 맥락이므로 하위 CLAUDE.md에 넣습니다. 영상의 결론은 둘 중 하나를 고르기보다 함께 쓰는 것이 최적이라는 것입니다.
