---
id: factory-ax-0175
domain: factory-ax
claim: 로봇 AI 모델을 돌리는 GPU를 다른 세대나 다른 제조사 제품으로 바꾸려는 사업자는 모델만 옮기면 끝난다고 보지 말고, 실행 엔진을
  다시 구축한 뒤 추론 지연·작업 정확도·로봇 제어 주기를 다시 검증할 일정과 비용을 잡아야 한다.
status: candidate
evidence: policy
confidence: 0.65
sources:
- url: https://www.hellot.net/news/article.html?no=116298
  author: 최재규 기자(헬로티)
  seen: '2026-11-14'
  quote: 사측은 GPU 아키텍처가 달라지면 텐서RT 실행 엔진을 다시 구축해야 한다고 명시한다.
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
- GPU교체
- TensorRT
- 재검증
- 원격추론
---
엔비디아 GPU에서 추론 성능을 높이는 텐서RT 실행 엔진은 GPU 아키텍처가 바뀌면 다시 구축해야 하며, 엔비디아 제품끼리 바꿀 때도 마찬가지라고 회사가 명시하고 있습니다. 다른 반도체 업체의 연산 장치로 옮길 때는 그 하드웨어에 맞는 실행 프로그램과 연산 방식까지 검토해야 합니다. 모델이 정상적으로 돌아가더라도 추론 지연, 작업 정확도, 로봇 제어 주기는 다시 확인해야 합니다. 로봇 본체에 연산 장치를 달지 않고 별도 서버에서 추론해 결과를 보내는 원격 추론 방식도 있으니, 연산 장치를 어디에 둘지에 따라 달라지는 개발·운영 비용도 함께 비교할 수 있습니다.
