---
id: ai-tools-0028
domain: ai-tools
claim: 광고 영상에 브랜드명·가격 같은 화면 글자가 들어가면 Kling 3.0은 쓰지 말고, 어떤 모델이든 생성 후 철자와 요청하지 않은 인쇄가
  생겼는지 확인한다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=cS1cBP5YtqU
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-03'
  quote: Text is still a problem for some models.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI영상
- 광고제작
- 텍스트렌더링
- Kling
- 검수
verified_by: 실무자 실측(단일 출처)
---
AI 영상 모델 일부는 아직 화면 속 글자를 제대로 쓰지 못한다. 같은 프롬프트 비교에서 Kling 3.0은 광고 3편 중 2편에서 엔드카드 글자가 깨졌고, Seedance 2.5는 'Hello, Nomad'를 'Hello No Map'으로 쓰고 캔에 요청하지 않은 인쇄를 넣었으며, Seedance 2.0은 요청하지 않은 '$1.99'를 캔에 찍었다. 상호·가격·슬로건이 화면에 보여야 하는 광고라면 Kling 3.0을 피하고 글자·제품 라벨을 잘 지킨 Kling 4.0이나 Flux 3 쪽을 먼저 시도한다. 생성 뒤에는 글자 철자, 추가된 문구, 라벨 변형 여부를 프레임 단위로 확인하고 나서 게시한다.
