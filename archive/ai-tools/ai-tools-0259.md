---
id: ai-tools-0259
domain: ai-tools
claim: AI 코딩 도구에는 기능을 하나씩 맡기고 잘된 상태마다 git 커밋해 두어야, 결과가 잘못되거나 되감기가 일부만 복구될 때도 바로 앞
  세이브 포인트로 돌아갈 수 있다.
status: verified
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=zmpXdQmLeYA
  author: 코드깎는노인
  seen: '2026-11-06'
  quote: 그 한 마디가 가장 확실한 되돌리기 버튼이 됩니다.
  source: 코드깎는노인
- url: https://www.youtube.com/watch?v=xjHR00fV-XQ
  author: 코드깎는노인
  seen: '2026-11-07'
  quote: bash 명령으로 바꾼 것이나 내가 직접 고친 것은 못 돌립니다.
  source: 코드깎는노인
first_seen: '2026-11-06'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- codex
- git
- 커밋
- 되돌리기
verified_by: 실무자 실측(단일 출처)
mentions: 2
---
영상 기준 버전의 코덱스에는 파일 되돌리기 명령이 따로 없어 git 저장이 되돌리기 수단이 됩니다. 명령어를 몰라도 '지금 상태를 git으로 저장해 줘' 또는 '커밋해 줘'라고 부탁하면 됩니다. 기능 하나를 부탁하고 확인한 뒤 커밋하고 다음 기능으로 넘어가세요. 여러 개를 한꺼번에 부탁하면 되돌릴 때 잘된 것까지 같이 사라집니다. 결과가 마음에 안 들면 /diff로 바뀐 곳을 보고 '마지막 커밋 상태로 되돌려 줘'라고 하면 됩니다. git은 내 컴퓨터 안의 저장이고, 인터넷에 올리는 GitHub와는 다릅니다.
