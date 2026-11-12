---
id: factory-ax-0142
domain: factory-ax
claim: CNC·PLC 같은 생산설비를 사무용 PC망에 연결한 제조 사업자는 설비 네트워크를 사무용 네트워크와 구획해 분리해야 하며, 그래야 사무용
  PC 쪽으로 들어온 공격이 생산설비까지 번지는 것을 막을 수 있다.
status: candidate
evidence: consensus
confidence: 0.6
sources:
- url: https://www.kidd.co.kr/news/248118
  author: 산업일보 임지원 기자(포티넷 레베카 첸 발표)
  seen: '2026-11-12'
  quote: 핵심 제어 기능을 격리하면서도 필요한 데이터 흐름과 유지보수 활동은 허용하는 것이 원칙
  source: 산업일보
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- OT보안
- 네트워크분리
- 사이버보안
- 스마트공장
---
예전에는 생산설비(OT)가 외부와 끊긴 망에서 돌았지만, 지금은 사무용 IT망과 주고받는 데이터가 많아져 공격자가 들어올 수 있는 길도 늘었습니다. 포티넷이 708명을 조사했더니 OT를 IT와 분리해 운영한다는 곳은 34%뿐이었고, OT 시스템이 멈춰 생산성에 영향을 받았다는 응답은 50%였습니다. 공장에서 사이버공격을 당하면 서버 복구로 끝나지 않고 설비 정지, 납기 차질, 작업자 안전 문제까지 이어질 수 있습니다. 사무용 PC망과 설비망을 나누되, 데이터 수집이나 원격 유지보수처럼 꼭 필요한 연결은 접근제어를 걸어 허용하는 것이 원칙입니다. 이 내용은 보안 업체가 행사에서 발표한 것이므로 장비를 사기 전에 내 설비 규모에 맞는지 따로 견적과 의견을 받아 보세요.
