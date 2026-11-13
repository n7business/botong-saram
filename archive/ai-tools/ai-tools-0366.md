---
id: ai-tools-0366
domain: ai-tools
claim: CLAUDE.md가 불어나 클로드가 느려지고 규칙을 잘 안 따르면 파일을 단순히 쪼개지 말고 규칙이 필요한 시점에만 불러오도록 설계해야
  한다.
status: merged
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=FBv8hK_DtJ8
  author: 짐코딩 (@gymcoding)
  seen: '2026-11-07'
  quote: 클로드닷d 파일이 무려 47,000 단어까지 불어놨대요.
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
- 컨텍스트
- 성능
merged_into: ai-tools-0363
---
영상은 프론트와 백엔드가 합쳐진 모노레포에서 CLAUDE.md가 47,000단어까지 불어난 사례를 소개합니다. 이때 클로드가 느려지고 규칙을 잘 따르지 않았습니다. 개발자가 규칙을 필요할 때만 불러오도록 나누자 처음에 읽는 루트 메모리 파일이 80% 줄었습니다. 핵심은 관계없는 규칙이 클로드의 주의를 뺏지 않게 하는 것입니다. 80%는 읽는 파일이 줄어든 수치이며, 정확도 향상을 측정한 수치는 아닙니다.
