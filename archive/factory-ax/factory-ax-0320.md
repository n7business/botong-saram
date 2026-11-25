---
id: factory-ax-0320
domain: factory-ax
claim: Codex·Claude Code 같은 AI 코딩 도구를 업무에 쓰는 사업자는 도구 설정이 바뀌어 AI 요청이 허가하지 않은 외부 중계
  서버를 거치거나 샌드박스 같은 보안 기능이 꺼져 있지 않은지 점검하고, 외부 네트워크 연결과 API 인증정보도 바로 확인해야 한다.
status: candidate
evidence: consensus
confidence: 0.7
sources:
- url: https://www.kidd.co.kr/news/248256
  author: 산업일보 임지원 기자(포티넷 카필 굽타 부사장 발언)
  seen: '2026-11-25'
  quote: 외부 네트워크 연결과 API 인증정보를 즉시 점검해야 한다
  source: 산업일보
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI보안
- AI코딩도구
- 설정변조
- API키
- 샌드박스
---
포티넷은 국내 조직을 노리고 정상 AI 코딩 도구(Codex, Claude Code 등)의 설정을 바꾸는 공격을 확인했다고 밝혔습니다. 공격자는 AI 서비스 요청이 허가하지 않은 외부 중계 서버를 거치도록 설정을 바꾸고, 실행 환경을 격리하는 샌드박스 같은 보안 기능을 끕니다. 회사가 설정이 바뀐 줄 모르고 AI를 계속 쓰면 내부 정보가 밖으로 새어 나갈 수 있습니다. 도구 설정 파일에 모르는 프록시나 중계 주소가 들어 있지 않은지, 샌드박스·권한 확인 기능이 꺼져 있지 않은지 정기적으로 확인하십시오. 의심스러우면 API 키를 새로 발급해 바꾸십시오.
