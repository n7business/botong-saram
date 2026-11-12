---
id: ai-tools-0462
domain: ai-tools
claim: Microsoft Foundry에서 클로드 코드로 긴 문서를 다룰 때는 배포 이름을 claude-opus-4-8처럼 모델 ID로 짓거나
  modelOverrides로 연결해야 하는데, 클로드 코드가 이름으로 모델을 알아보지 못하면 1M이 아니라 200K 컨텍스트로 가정하기 때문이다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://code.claude.com/docs/en/azure-ai-foundry
  author: Anthropic
  seen: '2026-11-11'
  quote: For a deployment name it can't match to a model, Claude Code assumes a 200K
    window
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
- 컨텍스트
verified_by: 공식 출처
---
Foundry에서는 Fable, Sonnet 5 이상, Opus 4.7 이상 모델이 기본으로 1M 토큰 컨텍스트를 쓰지만, 클로드 코드는 모델 변수에 적힌 배포 이름을 보고 모델을 판단합니다. team-opus-prod처럼 임의로 지은 이름은 모델을 알 수 없어 200K 창으로 처리됩니다. 배포 이름을 모델 ID와 같게 짓거나 settings.json의 modelOverrides에 모델 ID와 배포 이름을 짝지어 적어 두세요. 일부러 200K로 쓰려면 CLAUDE_CODE_DISABLE_1M_CONTEXT=1을 설정하면 됩니다.
