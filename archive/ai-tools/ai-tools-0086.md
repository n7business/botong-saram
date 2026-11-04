---
id: ai-tools-0086
domain: ai-tools
claim: 협력업체·거래처 서류 검수는 상대방이 스캔본만 올리게 하고 OCR로 읽어 엑셀화하되, 사업자등록증은 국세청 공공데이터 API로 진위를
  조회하고 보험 증권은 유효기간을 작업 일정과 교차 검증한다.
status: candidate
evidence: anecdote
confidence: 0.55
sources:
- url: https://www.youtube.com/watch?v=ID9b5reTD0o
  author: VCU AX 해커톤 2기 지클제 팀 · 양실장의 바이브코딩대학
  seen: '2026-11-03'
  quote: 요즘에 OCR 기능이 상당히 많이 뛰어나고
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- OCR
- 서류검수
- 국세청API
- 협력업체
---
업체당 약 10종 서류(사업자등록증, 산재보험 가입 내역, 근재보험 증권 등)가 3일 안에 몰리면 10개 업체만 돼도 100건이 넘고, 관리자 한 명이 이를 처리하느라 본업에 쓸 에너지가 남지 않는다. 고령의 업체 대표도 할 수 있게 제출은 스캔본 업로드만 요구하고, 우리 쪽은 검수만 한다. 회사 정보와 조직도는 OCR로 읽어 엑셀 항목으로 나누고, 사업자등록증은 국세청 API로 진위를 조회하며, 보험 증권은 OCR로 읽은 기간이 작업 일정과 맞는지 자동 대조한다. 요즘 OCR은 성능이 좋아 약간의 교정 장치만 더하면 실무에 쓸 수 있으므로, 보완이 필요한 건에만 알림이 뜨게 한다. 아낀 시간은 실제 현장 관리에 쓴다.
