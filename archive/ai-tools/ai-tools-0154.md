---
id: ai-tools-0154
domain: ai-tools
claim: AI 판정 모델을 비교할 때는 정답률 하나로 고르지 말고 비싼 실수(오발송)와 놓침을 따로 세어야 내 업무에 맞는 모델을 고를 수 있다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.gpters.org/dev/post/panjeong-jeonyong-model-jev-geodae-hoesa-dulyi-sohyeong-modeli-naon-dwiedo-f6awppi0Iirr7Ef
  author: 아그나르(글쓴이 하영)
  seen: '2026-11-05'
  quote: 정답률만 보지 말고 업무에서 비싼 실수(오발송)와 놓침을 따로 센다
  source: 지피터스 GPTers
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2026-12-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 평가지표
- 오발송
- 재현율
- 모델선택
verified_by: 실무자 실측(단일 출처)
---
같은 검증셋에서 오발송은 84건 중 Haiku 0건, Jev 3건, Opus 4건, Luna 6건이었고, 보낼 사람 15건 중 잡아낸 수는 Luna 13건, Jev·Opus 11건, Haiku 10건이었다. Haiku는 '검토'를 오답으로 치는 세 갈래 채점에서 85.9%였지만, 보냄 여부 둘로만 보면 94.9%로 1위였다. 그러니 '검토' 같은 보류 답을 어떻게 셀지도 먼저 정해야 한다. 잘못 보내는 것이 비싼 일인지 놓치는 것이 비싼 일인지에 따라 같은 결과로도 다른 모델을 고르게 된다. 보낼 사람이 15건뿐이라 재현율은 1건 차이가 6.7%포인트이므로 비율을 일반 성능으로 읽지 않는다.
