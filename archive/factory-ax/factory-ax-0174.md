---
id: factory-ax-0174
domain: factory-ax
claim: 엔비디아 그루트(GR00T) 같은 공개 로봇 AI 모델로 자동화를 개발하려는 사업자는 상업적 이용이 가능한 라이선스라도 실행 하드웨어
  조건은 따로 있으므로, 그루트 1.7 기준 GPU 메모리 16GB 이상과 CUDA 12.6 이상 지원 장비를 예산에 넣어야 한다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://www.hellot.net/news/article.html?no=116298
  author: 최재규 기자(헬로티)
  seen: '2026-11-14'
  quote: 모델의 이용 권한과 이를 실행하는 하드웨어의 호환성은 별개의 문제다.
  source: 헬로티
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 로봇AI
- 오픈모델
- GPU
- 하드웨어요구사항
- 엔비디아
---
그루트 1.7은 상업적 이용과 자체 데이터로 추가 학습하는 것을 허용하는 아파치 2.0 라이선스로 배포됩니다. 그런데 모델을 쓸 권리와 그 모델을 돌릴 하드웨어 호환성은 별개입니다. 공식 실행 절차를 따르려면 추론에 GPU 메모리가 최소 16GB 필요하고, 엔비디아 CUDA 12.6 이상을 지원해야 합니다. 시뮬레이터인 아이작 심도 공식 요구사항에 엔비디아 RTX 시리즈가 들어 있고, 아이작 랩의 GPU 학습 단계에도 CUDA를 지원하는 엔비디아 장치가 필요합니다. 모델이 무료라고 개발비가 적게 들 거라 보지 말고, 장비 구매비 또는 클라우드 비용부터 따져 봐야 합니다.
