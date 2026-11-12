---
id: ai-tools-0319
domain: ai-tools
claim: 모든 프로젝트에 적용할 지시는 사용자 폴더의 .claude에 CLAUDE.md로 두고 한 프로젝트용 지시는 그 프로젝트 루트에 두어야,
  지시가 적용될 범위를 나눌 수 있다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=8RxtwS94ahw
  author: 한범 (서울대 교수)
  seen: '2026-11-07'
  quote: 프로젝트 폴더의 가장 바깥쪽(루트)에 둔 CLAUDE.md는 그 프로젝트에만 적용됩니다.
  source: 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- CLAUDE.md
- 전역설정
- 설치
---
프로젝트 폴더의 가장 바깥쪽(루트)에 둔 CLAUDE.md는 그 프로젝트에만 적용된다. 모든 프로젝트에 적용하려면 사용자 기본 폴더(윈도우는 %USERPROFILE%) 안의 숨은 폴더 .claude에 넣으며, 이를 전역 세팅이라고 한다. 폴더를 하나하나 클릭해 들어갈 필요 없이 클로드 코드에 명령으로 시키면 된다. 설치가 끝나면 /exit로 나갔다가 claude를 다시 실행해야 적용된다.
