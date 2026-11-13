---
id: ai-tools-0515
domain: ai-tools
claim: AI가 만든 문서 정리 위키는 검색을 대신하게 하지 말고 원본 문서 검색과 함께 쓰게 해야 하는데, 위키만 쓰면 오히려 점수가 낮았고
  위키와 검색을 함께 쓸 때 점수가 가장 높으면서 질문당 토큰도 줄었기 때문이다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: the wiki helped Claude the most when we also gave it access to a search tool
  source: Anthropic Engineering 블로그
- url: https://www.youtube.com/watch?v=Ni0gE4LeSlc
  author: 조코딩 JoCoding
  seen: '2026-11-10'
  quote: 정리된 지식과 원본 검색을 함께 쓰는 것이 좋다.
  source: 조코딩 JoCoding
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- wiki
- 검색
- 토큰비용
verified_by: 독립 2곳 weight 1.7
mentions: 2
---
Anthropic이 약 35만 개 내부 문서로 실험한 결과, 클로드가 위키만 보고 답했을 때는 최고 점수가 48%였습니다. 검색 도구만 쓴 경우는 53%였고, 검색과 위키를 함께 쓴 경우는 위키가 커지면서 54%에서 61%까지 올랐습니다. 위키와 검색을 함께 쓰면 질문 하나에 약 2만 토큰도 아낄 수 있었습니다. 사내 자료를 AI용 위키로 정리했다면 원본 폴더 검색 권한은 그대로 두고, 위키를 자료를 찾아가는 지도로 쓰게 하는 것이 좋습니다.
