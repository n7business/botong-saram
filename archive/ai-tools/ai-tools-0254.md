---
id: ai-tools-0254
domain: ai-tools
claim: 클로드 코드에서 위험한 명령 차단과 테스트 실행처럼 반드시 지켜야 할 규칙은 CLAUDE.md에 부탁하지 말고 퍼미션과 훅으로 강제해야
  한다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=6cr4PeilKJk
  author: 짐코딩
  seen: '2026-11-06'
  quote: 클로드 MD가 부탁이라면 훅은 강제예요.
  source: 짐코딩 (@gymcoding)
- url: https://www.youtube.com/watch?v=8RxtwS94ahw
  author: 한범 (서울대 교수)
  seen: '2026-11-07'
  quote: 이 설정은 클로드가 기계적으로 따르는 규칙입니다.
  source: 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm)
first_seen: '2026-11-06'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드 코드
- 퍼미션
- 훅
- 하네스 엔지니어링
---
CLAUDE.md에 '위험한 명령은 실행하지 말라'거나 '테스트를 꼭 하라'고 적어도 AI가 항상 지킨다는 보장은 없다. 퍼미션을 쓰면 파일 읽기는 허용하고 파일 삭제는 실행 자체를 막는 식으로 제한할 수 있다. 훅은 자동으로 실행되므로 테스트 같은 검증을 강제할 때 쓴다. CLAUDE.md에는 맥락을 적고, 어기면 안 되는 일은 퍼미션과 훅으로 옮긴다.
