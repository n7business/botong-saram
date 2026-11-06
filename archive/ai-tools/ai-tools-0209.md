---
id: ai-tools-0209
domain: ai-tools
claim: 컴퓨터 유즈 에이전트가 전경에서 키보드로 입력하는 동안에는 사람이 조작을 멈추고, 끝난 뒤 입력된 문자열이 요청과 같은지 확인해야 한다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://yozm.wishket.com/magazine/detail/4026/
  author: Justn
  seen: '2026-11-06'
  quote: 전경 키보드 입력을 시험할 때는 사용자의 조작을 멈추고 조건을 통제할 필요가 있었습니다.
  source: 요즘IT
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 컴퓨터유즈
- 한글입력
- 포커스
- cua-driver
verified_by: 실무자 실측(단일 출처)
---
'cua-driver 테스트 성공' 입력을 요청했을 때 실제로는 '다cu-driver 테스트 성공식도'가 들어갔습니다. 사용자가 포커스를 바꾸지 않기로 하고 재시험하자 같은 문구가 첫 시도에 정확히 입력됐습니다. 사용자의 포커스 간섭 가능성이 커졌지만 입력기 문제를 완전히 배제하지는 못했습니다. 깨졌을 때는 접근성 경로의 set_value로 값을 직접 넣어 정확한 문구를 넣고 후속 조회로 일치를 확인했습니다. 시험 횟수가 적어 일반화할 수는 없습니다.
