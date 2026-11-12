---
id: ai-tools-0423
domain: ai-tools
claim: claude remote-control에 --settings로 설정 파일을 지정해 쓰다가 그 파일을 고쳤다면 claude remote-control을
  다시 시작해야 하는데, 재시작 전까지는 새 세션이 시작되지 않기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-10'
  quote: no new session starts until you restart `claude remote-control`
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- remote-control
- 원격
- 설정
verified_by: 공식 출처
---
2.1.321에서 claude remote-control에 --settings <파일> 옵션이 추가되었습니다. 이 옵션을 쓰면 원격으로 여는 모든 세션에 같은 설정 파일이 적용됩니다. 그런데 실행 중에 설정 파일이 바뀌면 claude remote-control을 다시 시작할 때까지 새 세션이 열리지 않습니다. 휴대폰으로 사무실 컴퓨터의 클로드를 부리다가 갑자기 새 세션이 안 열린다면, 최근에 설정 파일을 고치지 않았는지 먼저 확인하세요.
