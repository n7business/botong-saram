---
id: factory-ax-0350
domain: factory-ax
claim: 로봇 학습용 데이터셋을 만드는 제조 사업자는 영상·음향 같은 센서 정보와 로봇의 상태·행동 데이터를 시간 순서가 맞도록 맞추고, 수집
  환경·데이터 종류·저장 위치 같은 메타데이터와 작업 환경·내용·과정을 함께 기록해 두어야 다른 로봇과 업체에서도 그 데이터를 다시 쓸 수 있다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/172462/view?mno=&pageIndex=1
  author: 산업통상부 국가기술표준원 기계융합산업표준과
  seen: '2026-11-28'
  quote: 영상·음향 등 센서 정보와 로봇의 상태·행동 데이터를 시간 순서와 일치하도록 최소 사항을 규정한다.
  source: 산업통상부 보도자료
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2027-02-26'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 로봇
- 학습데이터
- 메타데이터
- 시간동기화
- 데이터셋
- KS
verified_by: 공식 출처
---
로봇마다 데이터 구조와 속성이 달라서 지금은 기업끼리 학습 데이터를 공유하거나 다시 쓰기 어렵습니다. 국표원의 KS 제정안은 작업 중에 모은 센서 정보와 로봇의 상태·행동 데이터를 시간 순서에 맞게 정렬하는 최소 사항을 정합니다. 작업 수행 환경, 작업 내용, 작업 과정을 기록하는 데이터 구조도 함께 정의합니다. 메타데이터는 데이터를 어떤 환경에서 모았는지, 어떤 종류인지, 어디에 저장했는지를 설명하는 데이터이며, 표준안은 저장 방식과 메타데이터 형식도 체계적으로 정합니다. 처음부터 이 항목을 빠뜨리지 않고 남겨 두어야 나중에 데이터를 팔거나 다른 로봇에 학습시킬 때 처음부터 다시 정리하지 않아도 됩니다.
