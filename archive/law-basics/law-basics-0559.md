---
id: law-basics-0559
domain: law-basics
claim: 쓰지 않는 API나 테스트 서버를 그대로 두면 관리되지 않은 자산이 되어 개인정보 유출 경로가 되므로, 개발이 끝났거나 더 이상 쓰지
  않는 서버·API·부가 서비스는 찾아서 닫거나 지워야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=12674
  author: 개인정보보호위원회
  seen: '2026-11-28'
  quote: 미사용 API·테스트 서버 방치 등 관리되지 않은 자산으로 인한 유출
  source: 개인정보보호위원회
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: '2027-05-27'
supersedes: null
superseded_by: null
experiment: null
law_ref:
  law: 개인정보 보호법
  article: 제29조
  effective: '2026-11-28'
contributor: null
tags:
- 개인정보
- 유출
- 테스트서버
- API
- 자산관리
verified_by: 공식 출처
---
개인정보위 분석에 따르면 미사용 API·테스트 서버 방치처럼 관리되지 않은 자산 때문에 생긴 유출이 많았습니다. 업무지원 시스템이나 부가 서비스 같은 비핵심 서비스가 해킹된 경우도 많았습니다. 외주로 홈페이지나 앱을 만든 사업자는 개발 과정에서 만든 테스트 서버, 예전 이벤트 페이지, 지금은 안 쓰는 연동 API가 아직 켜져 있는지 개발사에 확인하세요. 핵심 서비스만 지키고 주변 시스템을 방치하면 그 주변 시스템이 침입 통로가 됩니다.
