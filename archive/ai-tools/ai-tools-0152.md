---
id: ai-tools-0152
domain: ai-tools
claim: 판정 업무에 쓸 AI 모델을 고를 때는 짧은 검증셋으로 끝내지 말고 모델이 운영에서 실제로 읽는 입력으로 한 번 더 시험해야 하며, 한
  실험에서는 이렇게 재자 정답률이 약 10~18%포인트 낮아졌다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.gpters.org/dev/post/panjeong-jeonyong-model-jev-geodae-hoesa-dulyi-sohyeong-modeli-naon-dwiedo-f6awppi0Iirr7Ef
  author: 아그나르(글쓴이 하영)
  seen: '2026-11-05'
  quote: 짧은 검증셋으로 끝내지 말고, 운영에서 실제로 모델이 읽는 입력으로 한 번 더 돌린다.
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
- 모델선택
- 평가
- 판정자동화
- 검증셋
verified_by: 실무자 실측(단일 출처)
---
정답이 있는 판정 사례를 50건 이상 모으고 이름 같은 개인정보는 뺀 뒤, 운영 중인 규칙 그대로 모델마다 3회씩 돌린다. 지피터스의 영업 리드 판정 실험에서 헤드라인·회사·위치만 준 검증셋과 프로필 원문을 준 운영 입력 56건을 비교하니 Jev는 91.9%에서 82.1%로, Luna는 90.9%에서 73.2%로, Haiku는 85.9%에서 71.4%로 떨어졌다. 모델 간 순위도 입력에 따라 달라졌다. 다만 운영 입력 56건은 봇의 1차 판정을 지나 사람이 본 건이라 어려운 쪽일 수 있고 라벨 성격도 달라서, 하락 전부를 입력 차이 때문으로 볼 수는 없다.
