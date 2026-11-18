---
id: ai-tools-0610
domain: ai-tools
claim: 고객 원본 자료가 든 폴더를 클로드 코워크에 연결할 때는 읽기 전용이나 '읽기·쓰기·삭제 금지' 모드로 연결하고, 장부·DB도 읽기 전용
  권한부터 주어야 한다. 에이전트가 잘못 움직여도 손상될 수 있는 범위가 그만큼 줄기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/how-we-contain-claude
  author: Anthropic
  seen: '2026-11-19'
  quote: Claude Cowork offers read-only, read-write, and read-write-no-delete.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드 코워크
- 권한
- 고객 정보
- 보안
verified_by: 공식 출처
---
클로드 코워크는 폴더 연결 방식을 읽기 전용, 읽기·쓰기, 읽기·쓰기·삭제 금지 세 가지로 나눠 둡니다. 앤트로픽은 이 모드를 나눠 둔 것이 위험을 세밀하게 조절하는 데 도움이 됐다고 설명합니다. 또 읽기 전용 DB 권한만 가진 에이전트는 실제 운영 데이터에 쓰는 에이전트보다 훨씬 넓게 써도 된다고 봅니다. 원본 서류 폴더는 읽기 전용으로 연결하고, 결과물은 별도 폴더에 쓰게 하는 식으로 나누세요.
