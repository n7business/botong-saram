---
id: factory-ax-0216
domain: factory-ax
claim: MES에 가동·정지 기록이 남지 않는 노후 설비라면, 설비 표시등을 카메라로 찍고 AI로 빨간불·초록불을 구분해 담당자에게 알림을 보내는
  방식으로 정지 시간(다운타임)을 파악하는 방법을 검토할 만하다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.hellot.net/news/article.html?no=116400
  author: 최재규 기자(헬로티)
  seen: '2026-11-18'
  quote: 다만 카메라가 모든 설비 이상을 진단하는 것은 아니다.
  source: 헬로티
first_seen: '2026-11-18'
last_confirmed: '2026-11-18'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 노후설비
- 다운타임
- CCTV
- 비전AI
- MES
---
오래된 설비는 켜지고 꺼질 때 기록이 시스템에 남지 않아 언제 멈췄는지 알기 어려운 경우가 많습니다. 실제 고객 현장에서는 설비 표시등을 카메라로 비추고, 외부 생성형 AI로 빨간색과 초록색을 구분해 빨간불이 켜지면 담당자에게 알림을 보내도록 구성했습니다. 이 방식은 설비 내부의 제어 신호를 직접 가져오지 않으므로 기존 설비를 뜯어고치지 않아도 됩니다. 다만 표시등 색이 바뀌는 것만 감지할 뿐 설비 이상을 진단해 주지는 않습니다. 원인 분석은 따로 해야 합니다.
