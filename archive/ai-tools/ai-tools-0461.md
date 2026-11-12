---
id: ai-tools-0461
domain: ai-tools
claim: Microsoft Foundry(Azure)로 클로드 코드를 여러 사람에게 배포하기 전에는 배포마다 모델 버전을 고정하고 ANTHROPIC_DEFAULT_OPUS_MODEL
  같은 변수를 지정해야 하는데, 그러지 않으면 기본값이 계정에 없는 모델을 가리켜 요청이 실패하거나 opus가 구버전(Opus 4.6)으로 잡히기
  때문이다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://code.claude.com/docs/en/azure-ai-foundry
  author: Anthropic
  seen: '2026-11-11'
  quote: Microsoft Foundry has no startup model check, so requests fail when the default
    is unavailable.
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- azure
- foundry
- 모델고정
- 배포
verified_by: 공식 출처
---
Foundry에서 sonnet·opus 같은 별칭은 클로드 코드에 들어 있는 기본값을 따르고, 이 기본값은 최신 모델보다 늦을 수 있습니다. Foundry는 시작할 때 모델이 있는지 검사하지 않으므로 기본 모델이 계정에 없으면 실제 요청 단계에서야 실패합니다. Azure에서 배포를 만들 때 '최신으로 자동 업데이트' 대신 특정 버전을 고르고, ANTHROPIC_DEFAULT_OPUS_MODEL·SONNET·HAIKU 변수에 배포 이름을 넣으세요. HAIKU를 지정하지 않으면 세션 제목 생성 같은 배경 작업도 주 모델로 돌아가 비용이 더 들 수 있습니다. 설정 후 /status에서 API provider가 Microsoft Foundry로 나오는지 확인하세요.
