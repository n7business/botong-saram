---
id: ai-tools-0683
domain: ai-tools
claim: AI로 만든 프로그램이 언제부터 잘못됐는지 모르겠다면 새 대화에서 'Git 히스토리를 하나씩 확인해서 언제부터 틀렸는지 찾고, 문제 커밋의
  변경만 되돌리고 이후 기능은 유지해 줘'라고 시키면 된다. 이렇게 하면 에이전트가 이전 대화를 기억하지 못해도 커밋 기록만으로 원인을 찾아 그
  커밋만 취소(revert)한다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 새 대화라 어제 내용을 몰라도 Git 기록 덕분에 해결할 수 있었습니다.
  source: 코드깎는노인
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- git
- revert
- 디버깅
- 바이브코딩
---
에이전트는 지금 대화에 남은 내용만 기억하고, 새 대화를 열면 예전 내용을 모두 잊습니다. 커밋이 남아 있으면 에이전트가 예전 커밋을 하나씩 불러와 실제로 실행해 보고, 마지막으로 잘 되던 커밋과 처음 틀린 커밋 사이의 변경에서 원인을 찾습니다. 화자 실습에서는 '계산 코드 정리'라는 평범한 커밋에 숨어 있던 버그를 찾아 그 커밋만 취소했고, 이후에 넣은 기능은 그대로 남았습니다. 실수는 이렇게 평범한 수정 속에 섞여 들어오므로, 합계만 맞아 보이는 결과에 안심하지 말아야 합니다. 에이전트가 권한을 물으면 무엇을 실행하려는지 읽고 승인하세요.
