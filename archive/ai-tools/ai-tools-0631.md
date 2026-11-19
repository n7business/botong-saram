---
id: ai-tools-0631
domain: ai-tools
claim: MCP 서버나 웹사이트에서 받은 PDF·이미지·워드·엑셀 파일을 클로드 코드가 읽지 못하고 .bin 파일로 저장한다면 v2.1.329
  이상으로 업데이트해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic (anthropics/claude-code)
  seen: '2026-11-20'
  quote: being saved as .bin, which kept Claude from reading the PDFs and images
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2026-12-20'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- mcp
- pdf
- 문서처리
- 업데이트
verified_by: 공식 출처
---
이전 버전에서는 MCP 서버나 웹사이트가 PDF, 이미지, .docx, .xlsx, .pptx 파일을 application/octet-stream 형식으로 보내면 클로드 코드가 이를 .bin 파일로 저장했습니다. 그래서 클로드가 PDF와 이미지를 읽지 못했습니다. v2.1.329에서 이 문제가 고쳐졌습니다. 서류나 첨부 파일을 연결 도구로 받아 처리하는 업무라면 버전부터 확인하세요.
