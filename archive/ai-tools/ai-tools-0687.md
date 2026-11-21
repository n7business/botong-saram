---
id: ai-tools-0687
domain: ai-tools
claim: PDF를 AI에 넣기 전에 마우스로 글자를 드래그해 선택되는지 확인해야 한다. 선택되지 않는 PDF는 사진을 찍어 만든 파일이라 OCR로
  글자를 따로 읽어야 하기 때문이다.
status: candidate
evidence: consensus
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=bRzpzqedDSk
  author: 최승기 (테디노트 TeddyNote, AutoRAG Community Meetup 2026)
  seen: '2026-11-21'
  quote: 사진을 찍어 올린 문서는 드래그해도 잡히지 않는다.
  source: 테디노트 TeddyNote
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- PDF
- OCR
- 텍스트레이어
- 문서파싱
---
디지털로 만든 PDF·엑셀에는 텍스트 정보가 들어 있어 드래그하면 글자가 잡히고, AI도 그 텍스트를 바로 읽습니다. 사진을 찍거나 스캔해 올린 문서는 드래그해도 글자가 잡히지 않습니다. 이런 문서는 OCR이나 이미지를 읽는 모델로 글자를 따로 읽어내야 하고, 이 과정에서 오류가 생기기 쉽습니다. 원본 파일이 따로 있다면 스캔본 대신 원본 디지털 파일을 넣는 편이 정확합니다.
