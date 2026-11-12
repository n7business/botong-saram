---
id: ai-tools-0155
domain: ai-tools
claim: AI 판정 모델의 확신도로 사람이 볼 건을 가르려면 시험용 데이터에서 잡은 문턱을 그대로 쓰지 말고 운영 입력으로 다시 재서 정해야 한다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.gpters.org/dev/post/panjeong-jeonyong-model-jev-geodae-hoesa-dulyi-sohyeong-modeli-naon-dwiedo-f6awppi0Iirr7Ef
  author: 아그나르(글쓴이 하영)
  seen: '2026-11-05'
  quote: 확신도 문턱은 운영 입력으로 다시 잡아야 합니다.
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
- 확신도
- 사람검토
- 판정자동화
- 문턱값
verified_by: 실무자 실측(단일 출처)
---
검증셋에서는 Jev 확신도 0.8 미만 15건의 정답이 8건(53.3%)뿐이었고, 나머지 84건은 83건(98.8%)을 맞혀 이 문턱으로 사람 몫을 잘 가를 수 있어 보였다. 그러나 운영 입력에서는 0.8 이상 22건의 정답률이 90.9%, 0.8 미만 34건은 76.5%로 차이가 크게 줄었다. 검증셋에서 0건이던 판정 흔들림도 운영 입력에서는 3건 나왔다. 검증셋 수치는 표본을 사후에 나눠 본 결과이므로, 운영 입력으로 문턱을 잡은 뒤 실제 결과로 다시 확인한다.
