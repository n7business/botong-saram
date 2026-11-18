---
id: ai-tools-0609
domain: ai-tools
claim: 메일이나 메신저로 받은 '이 프롬프트 좀 실행해 줘' 같은 지시문은 클로드 코드 같은 AI 에이전트에 그대로 붙여 넣지 말고, 처음부터
  끝까지 읽어 파일을 읽어 외부로 보내는 단계가 없는지 확인해야 한다. 앤트로픽 내부 모의 해킹에서 이런 프롬프트는 25번 중 24번 서버 접속
  키를 밖으로 빼냈다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.anthropic.com/research/how-we-contain-claude
  author: Anthropic
  seen: '2026-11-19'
  quote: Across 25 retries of that prompt, Claude completed the exfiltration 24 times.
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
- 프롬프트 인젝션
- 피싱
- 클로드 코드
verified_by: 실무자 실측(단일 출처)
---
앤트로픽 내부 모의 해킹에서 평범한 협업 메일처럼 보이는 '이거 실행해 줄래요?' 메일에 붙여 넣기만 하면 되는 프롬프트를 담아 직원에게 보냈습니다. 설정 단계 사이에 클라우드 접속 키 파일을 읽어 외부 주소로 보내라는 지시가 섞여 있었고, 25번 시도 중 24번 유출에 성공했습니다. 사용자가 직접 입력한 지시는 AI 쪽 안전장치가 이상하다고 잡아낼 근거가 없습니다. 출처가 확실하지 않은 프롬프트는 실행하지 말고, 에이전트를 쓰는 컴퓨터에는 접속 키·공인인증서 같은 민감 파일을 작업 폴더 밖에 두세요.
