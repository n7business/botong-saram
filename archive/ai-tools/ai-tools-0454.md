---
id: ai-tools-0454
domain: ai-tools
claim: 컴퓨터에 ANTHROPIC_API_KEY 환경변수가 설정되어 있으면 클로드 코드가 첫 실행 때 그 키를 쓸지 묻는데, 구독 요금제로 쓰려면
  승인하지 말고 로그인해야 한다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://code.claude.com/docs/en/overview
  author: Anthropic
  seen: '2026-11-11'
  quote: Claude Code skips the login prompt.
  source: Claude Code 공식 문서
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2026-12-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 클로드코드
- 요금
- API키
- 로그인
verified_by: 공식 출처
---
ANTHROPIC_API_KEY 환경변수가 있는 상태에서 클로드 코드가 이 키를 쓸지 물을 때 승인하면, 로그인 창 없이 바로 그 API 키로 실행됩니다. 이 경우 사용료는 구독 요금제가 아니라 API 키 계정으로 청구될 수 있습니다. 다른 프로그램 때문에 이 키를 설정해 둔 경우 특히 헷갈리기 쉽습니다. 구독으로 쓰려던 것이라면 승인하지 말고 로그인하세요. 이미 쓰고 있다면 /status로 로그인 방식을 확인합니다.
