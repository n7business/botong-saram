---
id: ai-tools-0725
domain: ai-tools
claim: AI 광고 영상에 내 홈페이지나 앱 화면을 보여 주려면 스크린샷을 레퍼런스로 첨부하고 노트북이나 휴대폰 화면에 띄우라고 지시하면 된다.
  그러면 AI 배우가 화면 속 버튼을 가리키는 장면까지 만들 수 있다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=p5Fj3dWSSmU
  author: 노마드 코더 Nomad Coders
  seen: '2026-11-23'
  quote: AI actors can interact with your UI.
  source: 노마드 코더 Nomad Coders
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI영상
- 스크린샷
- FFmpeg
- 그린스크린
- 광고
---
홈페이지 스크린샷을 첨부해 '이것이 노트북 화면'이라고 지정하고, 배우가 어디를 언제 가리킬지(예: 먼저 가운데 사진을 누르고 이어서 오른쪽 표지로 옮김)까지 프롬프트에 적습니다. 이용 단계를 차례로 보여 주고 싶다면 단색 녹색 배경 앞에서 찍게 합니다. 그다음 그 영상과 단계별 스크린샷을 클로드에 주고, FFmpeg로 녹색 부분을 알맞은 타이밍에 각 스크린샷으로 바꾸게 할 수도 있습니다. AI가 FFmpeg 명령을 잘 쓰므로 터미널에 익숙하지 않아도 시도할 수 있습니다.
