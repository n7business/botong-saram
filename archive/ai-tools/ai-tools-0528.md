---
id: ai-tools-0528
domain: ai-tools
claim: 클로드 코드는 업무마다 프로젝트 폴더를 따로 두고 각 폴더의 CLAUDE.md에 '결과는 01, 02처럼 번호를 붙인 문서로 저장하라'는
  규칙을 적어 두어야 하는데, 그래야 결과물이 폴더에 차례대로 쌓이고 Git 커밋으로 남아 나중에 다시 찾아 쓰기 쉽기 때문이다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=UbY8U1_kUeo
  author: 한범 (서울대 교수, @ProfHanBuhm)
  seen: '2026-11-13'
  quote: 글로벌 세팅은 물론 따로 있고요.
  source: 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- CLAUDE.md
- 기록관리
- 프로젝트 폴더
---
클로드 코드를 아무 폴더에서나 실행하지 말고, 동호회 관리나 PC 정리처럼 업무마다 저장소(폴더)를 따로 만들어 그 폴더에서 실행하세요. 그 폴더의 CLAUDE.md에는 그 업무에만 적용할 지시를 적어 두고, 모든 업무에 공통인 규칙은 전역 설정에 따로 둡니다. 특히 '작업 결과는 01, 02처럼 번호를 붙인 문서로 저장하라'고 적어 두면 무슨 일을 시키든 결과가 차례대로 쌓여 도서관처럼 정리되고, Git으로 커밋해 기록으로 남길 수 있습니다. 클로드도 어느 폴더에서 시작했는지 알기 때문에 그 폴더의 파일을 더 잘 찾습니다.
