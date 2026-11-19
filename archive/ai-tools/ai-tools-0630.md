---
id: ai-tools-0630
domain: ai-tools
claim: 인터넷에서 받은 폴더를 클로드 코드로 열 때는 신뢰 확인창을 그냥 넘기지 말고, v2.1.329부터 표시되는 '이 폴더의 훅이 어디에
  선언돼 있는지' 경고를 읽어야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: Added a trust dialog warning that says where a folder's hooks are declared
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 보안
- 훅
- 신뢰확인
- v2.1.329
verified_by: 공식 출처
---
훅은 클로드 코드가 작업하는 중에 자동으로 실행되는 명령입니다. 남이 만든 저장소에 훅이 들어 있으면 그 폴더를 신뢰하는 순간 그 명령이 내 컴퓨터에서 실행될 수 있습니다. v2.1.329부터는 신뢰 확인창이 해당 폴더의 훅이 어느 설정 파일에 선언돼 있는지 알려 줍니다. 낯선 폴더에서 훅 경고가 보이면 신뢰를 누르기 전에 그 파일을 열어 어떤 명령이 실행되는지 확인하세요.
