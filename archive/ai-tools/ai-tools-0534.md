---
id: ai-tools-0534
domain: ai-tools
claim: AI로 만든 캐릭터를 여러 영상에 똑같은 모습으로 등장시키려면 그림 한 장만 쓰지 말고 정면·옆모습·얼굴 클로즈업을 한 장에 담은 캐릭터
  시트를 만들어 영상 생성 때 참고 이미지로 붙여야 한다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=eTM3zIVFkp4
  author: 코드깎는노인
  seen: '2026-11-13'
  quote: 같은 캐릭터를 여러 각도에서 보여 주는 캐릭터 시트를 만듭니다.
  source: 코드깎는노인
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI영상
- 캐릭터일관성
- 캐릭터시트
- Higgsfield
---
그림 한 장에는 옆모습이나 얼굴 클로즈업이 없으므로 AI가 장면마다 캐릭터를 조금씩 다르게 그릴 수 있습니다. 먼저 만든 캐릭터 그림을 첨부하고 첨부 이미지를 정밀하게 고치는 모델(화자는 Higgsfield의 GPT Image 2.6 Sunburst를 사용)로 바꾼 뒤, 16:9 비율로 정면·옆모습·얼굴 클로즈업 세 칸을 그리게 합니다. 배낭처럼 옆이나 뒤에서만 보이는 소품은 보이게 그리라고 따로 지정합니다. 영상을 만들 때는 이 시트를 레퍼런스로 첨부하고, 프롬프트의 @Image1이 첨부 이미지와 연결되어 초록색으로 바뀌었는지 확인해야 합니다. 화자 계정에서는 시트 한 장에 1.5크레딧이 들었습니다.
