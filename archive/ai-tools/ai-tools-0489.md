---
id: ai-tools-0489
domain: ai-tools
claim: 클로드 코드를 API 키로만 쓰고 있다면 웹·모바일에서 시작한 작업을 터미널로 가져오는 claude --teleport와 터미널 세션을
  데스크톱 앱으로 넘기는 /desktop을 쓸 수 없으므로, 기기를 오가며 이어 일하려면 claude.ai 구독으로 로그인해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-12'
  quote: Teleport requires a claude.ai subscription.
  source: Claude Code 공식 문서
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2026-12-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- teleport
- 요금제
- 원격
verified_by: 공식 출처
---
웹이나 클로드 모바일 앱에서 시작한 긴 작업은 claude --teleport로 터미널에 가져와 이어 할 수 있습니다. 터미널에서 하던 세션은 /desktop으로 데스크톱 앱에 넘겨 변경 내용을 화면으로 확인할 수 있습니다. 두 기능 모두 claude.ai 구독이 있어야 합니다. /desktop은 macOS와 x64 윈도우에서만 됩니다. API 키로 쓰고 있다면 이 기능이 동작하지 않는 것이 고장이 아니라는 점을 알아 두세요.
