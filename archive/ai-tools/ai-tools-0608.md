---
id: ai-tools-0608
domain: ai-tools
claim: 비개발자 직원이 클로드 코워크 같은 AI 에이전트를 쓰게 할 때는 확인창의 '허용' 버튼에 기대지 말고, 에이전트가 접근할 폴더와 권한을
  처음부터 좁혀 두어야 한다. 앤트로픽 집계로는 사용자가 권한 확인창의 약 93%를 승인했고, 확인창을 많이 볼수록 하나하나를 덜 살폈기 때문이다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.anthropic.com/research/how-we-contain-claude
  author: Anthropic
  seen: '2026-11-19'
  quote: Our telemetry showed users approved roughly 93% of permission prompts.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- 권한
- 클로드 코워크
- 클로드 코드
- 직원 관리
verified_by: 실무자 실측(단일 출처)
---
앤트로픽은 클로드 코드에서 동작마다 사용자 승인을 받았지만, 사용자는 확인창의 약 93%를 승인했습니다. 몇 주 만에 '승인 피로'가 나타나 감독 장치가 오히려 주의를 떨어뜨렸습니다. 그래서 앤트로픽은 bash 명령을 읽지 못하는 일반 사무직 사용자에게는 건별 승인 대신 늘 켜져 있는 고정 경계를 두는 쪽으로 정했습니다. 코워크는 사용자가 고른 작업 폴더 밖을 볼 수 없게 해 두었습니다. 직원에게 에이전트를 쓰게 한다면 '물어볼 때 잘 보고 눌러라'고 당부하기보다 연결할 폴더와 계정 권한부터 최소로 정하세요.
