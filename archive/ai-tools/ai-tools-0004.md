---
id: ai-tools-0004
domain: ai-tools
claim: Claude Code가 갑자기 앞 내용을 잊고 반복하거나 둔해지면 모델 탓보다 먼저 CLI 버전을 v2.1.116 이상으로 올린다.
status: verified
evidence: observed
confidence: 0.9
sources:
- url: https://www.anthropic.com/research/april-23-postmortem
  author: Anthropic Engineering
  seen: '2026-11-03'
  quote: All three issues have now been resolved as of April 20 (v2.1.116).
  source: Anthropic Engineering 블로그
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 버전
- 장애
- 트러블슈팅
verified_by: 실무자 실측(단일 출처)
---
2026년 3~4월 Claude Code 품질 저하 보고 3건은 모두 모델이 아닌 제품(CLI) 쪽 변경이 원인이었고, API는 영향이 없었다. 특히 3월 26일 캐시 최적화 버그는 한 시간 넘게 쉰 세션에서 매 턴 이전 추론을 지워 '잊고 반복하고 이상한 도구를 고르는' 증상과 사용량 급감을 일으켰다. 수정은 4월 10일 v2.1.101, 전체 해결은 4월 20일 v2.1.116이다. 비슷한 증상이 나면 `claude --version`으로 버전을 확인하고 업데이트한 뒤 새 세션으로 재시도한다. 오래 쉰 세션을 이어 쓰기보다 새 세션을 열어 비교하는 것도 진단에 도움이 된다.
