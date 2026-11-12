---
id: ai-tools-0467
domain: ai-tools
claim: AI에게 맡기는 일 중 저장소 생성, git push, 배포, 파일 삭제, 외부 데이터 전송, 데이터베이스 수정처럼 회사 자산이나 외부에
  영향을 주는 일은 자동으로 맡기지 말고 사람이 한 번 더 확인해야 하는데, '결과물 저장'만 부탁해도 새 저장소 생성과 외부 반영까지 진행될 수
  있기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.75
sources:
- url: https://yozm.wishket.com/magazine/detail/4034/
  author: 둘둘
  seen: '2026-11-11'
  quote: ‘계속 진행할까요?’라는 질문만으로는 부족합니다.
  source: 요즘IT
- url: https://yozm.wishket.com/magazine/detail/4036/
  author: 김동혁
  seen: '2026-11-12'
  quote: AI 에이전트는 그 설정을 읽고 CI/CD 방식으로 배포하려는 흐름을 반복해서 보였습니다.
  source: 요즘IT
first_seen: '2026-11-11'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 에이전트
- 승인
- 배포
- git
---
AI와 작업하다 보면 결과물을 저장해 달라고 했을 뿐인데 새 Git 저장소가 만들어지고 push까지 끝나는 경우가 있습니다. 모든 행동에 승인을 걸 필요는 없고, 영향 범위가 어디까지인지와 되돌릴 수 있는지를 기준으로 나누면 됩니다. 따로 떼어 둔 폴더에서 초안을 고치는 일과 운영 데이터를 바꾸는 일은 다르게 다뤄야 합니다. 확인할 때도 '계속할까요?'만 보고 넘기지 말고, 무엇을 어디에서 실행하는지와 어떤 데이터가 바뀌는지를 보고 승인하세요.
