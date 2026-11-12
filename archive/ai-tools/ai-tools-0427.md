---
id: ai-tools-0427
domain: ai-tools
claim: AI 에이전트가 MCP로 회사 데이터를 고칠 수 있게 열어 줄 때는 요청한 사람에게 수정 권한이 있는지와 입력값이 맞는지를 서버에서 확인하게
  해야, 에이전트가 요청했다는 이유만으로 아무 데이터나 바뀌는 일을 막을 수 있다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://yozm.wishket.com/magazine/detail/4033/
  author: zwoo
  seen: '2026-11-10'
  quote: 요청한 사용자의 권한을 확인하고, 허용된 수정만 기존 상품 처리 로직으로 실행할 생각이다.
  source: 요즘IT
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- MCP
- 권한
- 입력검증
- 보안
---
조회만 되던 업무 시스템에 에이전트가 쓸 수정 기능(MCP·API)을 붙이면 편해지지만, 그만큼 잘못된 값이 바로 반영될 위험도 커집니다. 어떤 경로로 들어온 요청이든 요청한 사람의 권한을 확인하고, 허용된 수정만 기존 입력 검증을 거쳐 처리하게 만드세요. 외주 개발자에게 맡긴다면 이 두 가지 확인이 들어가 있는지 꼭 물어보세요. 읽기 전용 조회 경로는 따로 그대로 두는 편이 안전합니다.
