---
id: ai-tools-0031
domain: ai-tools
claim: AI 영상 모델을 고를 때는 한 플랫폼에서 여러 모델에 같은 프롬프트·같은 설정을 돌리되, 프롬프트의 각 부분이 검사 항목 하나(글자·제품
  일관성·립싱크·물리)를 맡도록 짜고 감점표로 채점한다.
status: merged
evidence: anecdote
confidence: 0.5
sources:
- url: https://www.youtube.com/watch?v=cS1cBP5YtqU
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-03'
  quote: 프롬프트의 각 부분이 하나씩 테스트 항목을 맡도록 짰다.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI영상
- 모델비교
- 프롬프트설계
- 테스트방법
- 광고제작
merged_into: ai-tools-0137
---
모델마다 광고를 따로 만들어 보면 크레딧만 날리고 실패 원인이 모델인지 프롬프트인지 알 수 없다. 대신 Higgsfield처럼 여러 모델을 한곳에서 돌릴 수 있는 플랫폼에서 프롬프트와 설정을 고정하고 모델만 바꿔 비교한다. 프롬프트는 노트북 뒷면 문구는 글자 테스트, 캔 주위를 도는 첫 3초는 제품 일관성 테스트, 짧은 대사는 립싱크 테스트처럼 요소마다 검사 항목을 하나씩 배정한다. 채점은 10점에서 시작해 갑자기 생기는 물체 같은 물리 오류는 -2점, 틀린 글자·이상한 얼굴은 -1점으로 깎으면 모델 간 비교가 쉽다. 어려운 광고일수록 먼저 가장 필요한 요소(진짜 같은 얼굴, 물리, 글자, 비용)를 정한 뒤 그 항목 점수로 고른다.
