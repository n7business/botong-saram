---
id: ai-tools-0368
domain: ai-tools
claim: GPT 이미지 2.6으로 GIF를 만들 때는 프레임 수만 늘리지 말고 서로 다른 그림 수와 한 장 크기를 함께 확인해야, 숫자만 많고
  작거나 같은 그림이 반복되는 결과를 피할 수 있다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=VtPhdzLEKP4
  author: 코드깎는노인
  seen: '2026-11-07'
  quote: 장수가 늘어난만큼 한 장이 작아진 셈이죠.
  source: 코드깎는노인
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- GPT 이미지
- GIF
- 이미지 생성
- 프레임
- 해상도
verified_by: 실무자 실측(단일 출처)
---
화자가 받은 GIF 4개는 모두 장수 x 한 장 크기가 약 150만 화소로 거의 같아, 장수가 늘면 한 장이 작아졌습니다. 70프레임을 요청했을 때 서로 다른 그림이 16장뿐인 파일도 있었고, 70장이 모두 다른 경우에는 채팅에 뜬 GIF가 208x102픽셀로 작았습니다. '더 부드럽게'라고 요청하면 그림이 더 부드러워지기보다 재생만 빨라질 수 있습니다. 짧게 반복되는 동작은 16장 안에서 장수와 간격을 숫자로 정해 요청하고, 긴 이야기 애니메이션은 장면별로 나눠 받는 편이 선명도를 지키는 데 유리합니다. OpenAI API 문서 기준으로 GIF는 한 번에 2~16장을 만들 수 있고 전체 픽셀 예산 안에 들어야 합니다.
