---
id: ai-tools-0549
domain: ai-tools
claim: 클로드 코드 팀·엔터프라이즈 요금제에서 직원이 fast mode를 쓰면 그 비용은 조직의 사용 크레딧에서 나가므로, 오너가 fast mode를
  켜 줄 때는 fastModePerSessionOptIn을 true로 설정해 세션마다 직원이 /fast로 직접 켜야만 쓰이게 해야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://code.claude.com/docs/en/fast-mode
  author: Anthropic
  seen: '2026-11-14'
  quote: fast mode is disabled by default for Team and Enterprise organizations.
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
- fast-mode
- 팀요금제
- 비용관리
verified_by: 공식 출처
---
팀·엔터프라이즈 조직에서 fast mode는 기본적으로 꺼져 있고, 오너가 조직 설정의 Claude Code 메뉴에서 켜 줘야 직원이 쓸 수 있습니다. 켜고 나면 직원의 fast mode 사용료는 구독 사용량이 아니라 조직의 사용 크레딧에서 빠집니다. 설정 파일에서 fastModePerSessionOptIn을 true로 두면 모든 세션이 fast mode가 꺼진 상태로 시작하고, 필요할 때만 직원이 /fast로 켜게 됩니다. 오너는 서버 관리 설정으로 이 값을 조직 전체에 배포할 수 있습니다. 직원은 /usage로 자기가 쓴 사용 크레딧을 확인할 수 있습니다.
