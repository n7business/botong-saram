---
id: ai-tools-0551
domain: ai-tools
claim: claude.ai 구독으로 로그인해 클로드 코드를 쓰면서 터미널 환경 변수에 API 키도 넣어 두었다면 v2.1.325 이상으로 업데이트해야
  하는데, 이전 버전에서는 백그라운드 세션이 구독 대신 그 API 키로 요금을 청구하는 문제가 있었기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: Anthropic
  seen: '2026-11-14'
  quote: Fixed background sessions started on your claude.ai login using (and billing)
    an API key or token from the shell
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-14'
last_confirmed: '2026-11-14'
review_by: '2026-12-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 비용관리
- api-key
- 업데이트
verified_by: 공식 출처
---
v2.1.325 릴리스 노트에 따르면, 그 전에는 claude.ai 로그인으로 시작한 백그라운드 세션이 백그라운드 서비스를 띄운 셸에 있던 API 키나 토큰을 쓰고 그 키로 비용을 청구하는 문제가 있었습니다. 구독 요금제를 쓰면서 다른 용도로 ANTHROPIC_API_KEY 같은 환경 변수를 셸에 설정해 둔 경우, 모르는 사이에 API 요금이 따로 나왔을 수 있습니다. claude --version으로 버전을 확인하고 낮으면 업데이트하세요. API 콘솔에서 예상하지 못한 사용 내역이 있는지도 확인해 보는 것이 좋습니다.
