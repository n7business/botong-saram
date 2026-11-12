---
id: ai-tools-0001
domain: ai-tools
claim: Claude Code에서 추론 effort를 기본값보다 낮추면 응답은 빨라지지만 결과 품질이 떨어지므로, 단순 작업에만 선택적으로 낮춘다.
status: merged
evidence: observed
confidence: 0.8
sources:
- url: https://www.anthropic.com/research/april-23-postmortem
  author: Anthropic Engineering
  seen: '2026-11-03'
  quote: In general, the longer the model thinks, the better the output.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- effort
- 추론
- 설정
verified_by: 실무자 실측(단일 출처)
merged_into: ai-tools-0015
---
Anthropic은 2026년 3월 Claude Code 기본 effort를 high에서 medium으로 내렸다가, 사용자들이 '덜 똑똑해졌다'고 보고하자 4월 7일 되돌렸다. 현재 기본값은 Opus 4.7은 xhigh, 그 외 모델은 high다. 모델이 더 오래 생각할수록 결과가 좋아지는 것이 일반 원칙이므로, 코드 수정·문서 분석 같은 중요한 작업에서는 effort를 낮추지 않는다. 파일 이름 바꾸기 같은 단순 반복 작업에서만 /effort로 낮춰 지연과 사용량을 줄인다. 기본값을 바꿨다면 응답이 둔해졌을 때 effort 설정부터 확인한다.
