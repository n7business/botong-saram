---
id: ai-tools-0450
domain: ai-tools
claim: AI에게 문서 정리 위키를 만들게 했다면 위키가 원본 문서보다 커지지 않았는지 확인해야 하는데, 원본만큼 자세해진 위키는 정리 효과 없이
  검색 비용만 늘린다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-11'
  quote: the wiki grew larger than the documents themselves
  source: Anthropic Engineering 블로그
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- wiki
- knowledge-base
verified_by: 실무자 실측(단일 출처)
---
Anthropic 실험의 한 과제에서 AI가 만든 위키가 원본 문서보다 커져 사실상 아무것도 요약하지 못한 결과가 나왔습니다. 위키는 여러 문서를 엮어 찾아갈 수 있는 지도 역할을 해야 쓸모가 있습니다. 위키를 만들게 했다면 전체 크기와 페이지 수를 원본과 비교해 보십시오. 원본 내용을 거의 그대로 옮겨 적고 있다면 중복 페이지를 합치고 세부 내용은 원본 링크로 대신하라고 다시 지시해야 합니다.
