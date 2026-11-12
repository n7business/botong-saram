---
id: ai-tools-0441
domain: ai-tools
claim: 한 컴퓨터에서 클로드 코드 세션을 여러 개 동시에 돌린다면 프로그램 이름으로 한꺼번에 종료하는 명령과 git add -A처럼 변경 파일을
  통째로 커밋하는 명령을 훅으로 막아야, 다른 세션의 서버가 꺼지거나 남이 고치던 파일이 내 커밋에 섞이는 일을 막을 수 있다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.gpters.org/llm-service/post/case-resolving-conflict-occurs-5wJnzP5SBtG7tKh
  author: .
  seen: '2026-11-10'
  quote: 각 세션이 컴퓨터를 혼자 사용한다고 판단하기 때문에 생기는 문제입니다.
  source: 지피터스 GPTers
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
- 훅
- 멀티세션
- git
verified_by: 실무자 실측(단일 출처)
---
세션은 저마다 컴퓨터를 혼자 쓴다고 여깁니다. 그래서 한 세션이 자기 서버를 다시 켜려고 같은 이름의 프로그램을 모두 끄면 다른 세션의 서버도 함께 꺼집니다. 같은 폴더에서 한 세션이 변경 파일을 전부 커밋하면 다른 세션이 고치던 파일까지 그 커밋에 들어갑니다. 클로드 코드의 훅은 셸 명령이 실행되기 직전에 그 명령을 검사해 막을 수 있으니, 이런 명령을 걸러 내도록 설정해 두세요. 한 사용자의 2주 기록에서는 동시 세션이 최대 13개였고, 막혔어야 할 명령이 507개였으며 그중 25건이 다른 세션이 작업하던 폴더에서 git add -A를 실행한 경우였습니다. 이 훅을 모은 claude-bulkhead는 개인이 공개한 오픈소스이므로, 설치하기 전에 출처와 구성 요소를 확인해야 합니다.
