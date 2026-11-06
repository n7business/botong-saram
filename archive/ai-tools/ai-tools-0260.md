---
id: ai-tools-0260
domain: ai-tools
claim: 코덱스 /review는 그냥 돌리지 말고 기존 기능과의 충돌이나 휴대폰 동작 같은 확인 기준을 직접 적어야, '문제 없음'으로 지나간
  결함까지 찾을 수 있다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=zmpXdQmLeYA
  author: 코드깎는노인
  seen: '2026-11-06'
  quote: 다만 그냥 봐 달라고 했을 때는 13초 만에 '문제 없음'이 나왔다.
  source: 코드깎는노인
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- codex
- 코드리뷰
- review
- 검증
verified_by: 실무자 실측(단일 출처)
---
영상에서 그냥 봐 달라고 했을 때는 13초 만에 '문제 없음'이 나왔습니다. 같은 기능을 Custom review instructions에 '필터나 완료 정렬과 같이 쓸 때 순서가 꼬이는지, 휴대폰에서도 되는지 확인해 줘'라고 적어 검토하자, 25초 뒤 문제 두 개를 찾았습니다. 완료 항목 정렬이 사라진 문제와 마우스 끌기를 휴대폰 손가락으로 쓸 수 없는 문제였습니다. 리뷰는 문제만 알려 주고 파일은 고치지 않으므로 수정은 따로 부탁해야 합니다. 리뷰가 확인하지 못했다고 한 부분은 직접 열어 본 뒤 커밋하세요.
