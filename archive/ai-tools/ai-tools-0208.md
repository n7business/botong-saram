---
id: ai-tools-0208
domain: ai-tools
claim: 컴퓨터 유즈 에이전트에 화면 조작을 맡길 때는 '했습니다'라는 응답을 믿지 말고 실제 결과를 다시 조회해 확인하며, 막히면 메뉴나 접근성
  같은 다른 경로로 시도한다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://yozm.wishket.com/magazine/detail/4026/
  author: Justn
  seen: '2026-11-06'
  quote: AI가 작업을 실행했다는 응답과 실제로 작업이 끝났다는 증거 사이에는 차이가 있었습니다.
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
- cua-driver
- 검증
- 우회
verified_by: 실무자 실측(단일 출처)
---
cua-driver 0.21.0을 맥북에서 단회 시험한 결과, 도구 응답과 실제 결과가 다르거나 도구가 막히는 경우가 있었습니다. 이 버전에서는 screenshot이 거부됐지만 get_desktop_state로 화면 PNG를 만들 수 있었습니다. 전경 Cmd+W로는 문서가 닫히지 않았지만 invoke_menu로 파일 → 닫기를 호출하니 저장 확인 시트가 나타났습니다. 이 시트에서는 미저장 문서를 폐기하는 '삭제'와 '저장' 버튼을 구분해야 했습니다. Cmd+W 실패의 원인은 확정되지 않았고, 파일 저장·메시지 전송·실제 폼 제출은 시험 범위에서 빠졌으므로 사람이 한 번 더 확인해야 합니다.
