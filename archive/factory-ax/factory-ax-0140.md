---
id: factory-ax-0140
domain: factory-ax
claim: 드론 모터는 나사 하나를 먼저 꽉 조이지 말고 구멍을 맞춘 뒤 대각선 순서로 조금씩 단단히 고정해야 하며, 모터가 기울거나 느슨하면 진동이
  FC 센서에 전달돼 자세를 잘못 판단할 수 있다.
status: candidate
evidence: consensus
confidence: 0.6
sources:
- url: https://www.hellot.net/news/article.html?no=116164
  author: 헬로티 최재규 기자(이승욱 디메이커스 엔지니어 인용)
  seen: '2026-11-11'
  quote: 모터 체결이 단단히 돼야 FC 쪽에 진동이 덜하다
  source: 헬로티
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 드론
- 조립
- 진동
- 모터체결
---
모터를 체결할 때는 먼저 체결 구멍을 모두 맞춥니다. 그다음 나사를 대각선 순서로 조금씩 조여 고정합니다. 모터가 조금이라도 기울거나 헐거우면 불필요한 진동이 생기고, 이 진동이 프레임을 타고 FC 센서로 전달되면 기체 자세를 잘못 추정하는 원인이 됩니다. FC 아래에는 진동 댐퍼를 넣고, GPS와 FC의 방향은 기체 전방에 맞춥니다.
