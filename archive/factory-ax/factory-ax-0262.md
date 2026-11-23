---
id: factory-ax-0262
domain: factory-ax
claim: AI 학습에 쓸 설비 데이터를 쌓는 제조 사업자는 값만 모으지 말고, 설비마다 고유 식별자(ID)를 붙이고 각 데이터의 의미·단위·제약조건을
  정의하며 양식 버전을 관리해야 나중에 데이터를 추적하고 재현할 수 있다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/172429/view?mno=&pageIndex=1
  author: 산업통상부 국가기술표준원
  seen: '2026-11-21'
  quote: 데이터의 추적성과 재현성을 위해 ▲ AAS 식별자 (ID) , 데이터의 의미·단위·제약조건 정의
  source: 산업통상부 보도자료
first_seen: '2026-11-21'
last_confirmed: '2026-11-23'
review_by: '2027-02-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AAS
- 데이터품질
- 메타데이터
- 추적성
- 제조AI
verified_by: 공식 출처
---
국가기술표준원의 AAS 활용 KS안은 데이터의 추적성과 재현성을 확보하는 기준으로 AAS 식별자(ID), 데이터의 의미·단위·제약조건 정의, 양식 버전 관리, 파일 형식 같은 적합성 확인 항목을 제시합니다. 같은 온도값이라도 단위나 측정 기준이 기록돼 있지 않으면 다른 설비 데이터와 합쳐 AI에 학습시킬 수 없습니다. 지금 쓰는 엑셀이나 MES 기록에 설비 ID, 항목별 단위와 허용 범위, 양식을 바꾼 날짜와 버전이 남아 있는지부터 점검하세요. 설비 이름과 코드를 하나로 맞추는 작업(factory-ax-0203)과 함께 하면 효과가 큽니다.
