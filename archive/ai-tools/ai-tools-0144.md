---
id: ai-tools-0144
domain: ai-tools
claim: 에이전트 모델 비용을 줄이려면 Liner Router 같은 라우팅 API를 검토할 수 있으며, 쿠버네티스 장애 10건 측정에서 비용은
  GPT-6.1 Sol의 28%, 운영 점수는 0.940 대 0.960이었다.
status: verified
evidence: observed
confidence: 0.55
sources:
- url: https://yozm.wishket.com/magazine/detail/4015/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: '비용: GPT-6.1 Sol의 28%였습니다.'
  source: 요즘IT
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2026-12-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 모델 라우팅
- 에이전트 비용
- Liner Router
- 브랜디드 콘텐츠
verified_by: 실무자 실측(단일 출처)
---
라우팅 API는 요청에 맞는 모델을 자동으로 골라 보내 주는 API입니다. 라이너 조건의 비용은 GPT-6.1 Sol의 28%였고, 단가 차이로 약 45%가 줄었으며 나머지는 토큰이 적었던 효과입니다. 토큰 효과는 에이전트 설정에 따라 달라질 수 있으므로 28%를 그대로 기대하면 안 됩니다. 경량 모델인 GPT-6 Luna보다는 3.3배 비쌌습니다. 어떤 모델이 요청을 처리했는지 알 수 없다는 점도 감안해야 합니다. 이 측정은 라이너와 함께 만든 브랜디드 콘텐츠이고 쿠버네티스 장애 대응에 한정된 결과이므로, 내 작업으로 직접 비교해 본 뒤 결정합니다.
