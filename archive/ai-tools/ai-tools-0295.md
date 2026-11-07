---
id: ai-tools-0295
domain: ai-tools
claim: AI가 사용자 대신 잘못된 가정을 하고 불필요한 코드까지 고치는 일을 줄이려면, 지시문에 모호하면 선택지를 드러내고 문제를 고치는 줄만
  바꾸라는 규칙을 적어 둔다.
status: candidate
evidence: consensus
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=3JCgiVYlLFo
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-07'
  quote: 요청이 모호하면 혼자 조용히 고르지 말고 선택지를 드러내라는 것이다.
  source: 노마드 코더 Nomad Coders
- url: https://www.youtube.com/watch?v=8RxtwS94ahw
  author: 한범 (서울대 교수)
  seen: '2026-11-07'
  quote: 정확히 지시한 일만 하고, 추가로 하고 싶은 일은 '제안' 한 줄로만 달게 했습니다.
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
- 코딩에이전트
- CLAUDE.md
- 지시문
- 카파시
---
Andrej Karpathy Skills는 이런 규칙을 담은 CLAUDE.md 파일로, 플러그인으로 설치하거나 내려받아 프로젝트에 넣을 수 있습니다. '코딩 전에 생각하기' 규칙은 가정하지 말고, 요청이 모호하면 혼자 고르지 말고 선택지를 드러내라는 내용입니다. '단순함 우선' 규칙은 문제를 고치는 줄만 바꾸고, 기존 스타일에 맞추고, 나머지는 건드리지 말라는 내용입니다. 다만 지시문은 강제력이 없어 세션이 길어지고 지저분해질수록 잘 지켜지지 않으므로, 린터나 테스트 같은 확인 수단과 함께 써야 합니다.
