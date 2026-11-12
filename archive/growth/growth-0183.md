---
id: growth-0183
domain: growth
claim: 코딩 에이전트가 하면 안 되는 작업은 프롬프트로 조심시키는 데 그치지 말고 권한 규칙에 적어 두어야 하며, Claude Code의 deny·ask·allow
  규칙은 모델이 아니라 도구가 강제한다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://eopla.net/magazines/48749
  author: 조쉬의 뉴스레터
  seen: '2026-11-07'
  quote: 규칙은 막기·묻기·허용(deny·ask·allow) 순으로 적용되고, 모델이 아니라 Claude Code가 강제해요.
  source: EO 플래닛
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI에이전트
- 권한관리
- 샌드박스
- ClaudeCode
---
Claude Code 공식 문서에 따르면 권한 규칙은 막기·묻기·허용(deny·ask·allow) 순으로 적용되고, 모델이 아니라 Claude Code가 강제합니다. 그래서 프롬프트로 조심시키는 것과는 다른 층의 장치입니다. /permissions에서 규칙을 보고 고칠 수 있으므로 막을 명령을 여기에 적어 둡니다. Codex도 샌드박스와 승인 정책으로 같은 범위를 정할 수 있습니다. 레볼루트는 이런 규칙에 더해 사고가 났을 때 들여다볼 로그도 남깁니다.
