---
id: factory-ax-0189
domain: factory-ax
claim: CNC 프로그램을 기계에 넣은 뒤 사람이 처음부터 끝까지 붙어서 검증하는 대신, 기계로 보내기 전에 충돌·보정 오류를 소프트웨어로 자동
  검사하고 경고가 뜰 때만 사람이 확인하게 하면 세팅 시간과 불량률을 함께 줄일 수 있다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=8GWWXAyAMpY
  author: 기계맨 CNC MCT (@GIGYEMAN)
  seen: '2026-11-16'
  quote: 그 검증 자체를 이 프로그램에 넣었고요.
  source: 기계맨 CNC MCT (@GIGYEMAN)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- CNC
- NC코드검증
- 충돌방지
- 불량률
- 세팅시간
---
세팅이 오래 걸리는 이유는 프로그램을 기계에 넣은 뒤 보정이나 치수가 맞는지 사람이 끝까지 지켜봐야 하기 때문입니다. 한 업체는 작업자가 뽑은 NC 코드를 기계로 보내기 전에 충돌 여부와 불량 가능성을 자동으로 검사하고, 보정이 잘못됐거나 이상한 값이 있으면 알람을 띄우게 했습니다. 사람은 '확인해 주세요' 같은 체크리스트가 뜰 때만 확인합니다. 예전에는 작업자 역량에 따라 불량률이 달라져 재가공이 반복됐지만, 도입 뒤에는 불량률이 줄고 제품이 더 빨리 나온다고 합니다. 다만 현장 맞춤으로 만든 프로그램이라 신뢰도는 최소 95% 수준으로 보고 있으며, 나머지는 계속 업데이트해 맞춰야 한다고 했습니다.
