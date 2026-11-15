---
id: factory-ax-0203
domain: factory-ax
claim: 설비 데이터를 AI로 분석하려는 제조 사업자는 제어 시스템의 태그명, 정비 기록의 설비 코드, 도면 표기가 서로 다르면 데이터가 연결되지
  않으므로, 같은 설비를 가리키는 이름과 코드를 먼저 하나로 맞춰야 한다.
status: candidate
evidence: consensus
confidence: 0.55
sources:
- url: https://www.hellot.net/news/article.html?no=116312
  author: 헬로티 김진희 기자
  seen: '2026-11-16'
  quote: 태그명과 정비 시스템의 자산 코드, 엔지니어링 도면상의 표기가 서로 달라
  source: 헬로티
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 데이터맥락화
- 설비코드
- 온톨로지
- 데이터정리
---
같은 설비라도 제어 시스템에서는 태그명으로, 정비 기록에서는 자산 코드로, 도면에서는 또 다른 표기로 부르는 경우가 많습니다. 이름이 이렇게 다르면 AI가 알람 이력과 정비 기록, 작업 일지를 같은 설비 이야기로 묶지 못합니다. 칼럼은 이런 문제를 풀려면 '데이터의 맥락화', 즉 설비 태그·공정 이벤트·기술 문서를 실제 물리 설비와 맞추는 작업이 먼저라고 말합니다. 소규모 공장이라면 설비 번호표 하나를 정해 모든 기록에 똑같이 쓰는 것부터 시작할 수 있습니다.
