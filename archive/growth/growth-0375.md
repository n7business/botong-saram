---
id: growth-0375
domain: growth
claim: AI나 공공 데이터로 거래처·경쟁사의 공시나 실적을 찾을 때는 회사 이름만으로 찾지 말고 사업자등록번호나 법인등록번호로 회사를 특정해야
  합니다. 한 개발자에 따르면 DART 회사 목록에서는 13,530개 회사가 5,573개 이름을 나눠 쓰고, 폐업한 회사와 옛 이름도 그대로 남아
  있습니다.
status: verified
evidence: observed
confidence: 0.6
sources:
- url: https://github.com/YoungsoonLee/korea-data-mcp
  author: Ted
  seen: '2026-11-15'
  quote: 같은 이름의 회사가 흔합니다.
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: '2027-02-13'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- DART
- 거래처확인
- AI활용
- 공공데이터
- 사업자등록번호
verified_by: 실무자 실측(단일 출처)
---
DART 회사 목록에는 이름이 같은 회사가 많습니다. 예를 들어 (주)카카오는 둘이고 종목명까지 같은데, 그중 하나는 2014년에 폐업했습니다. 상장폐지된 회사도 종목코드가 남아 있어서 종목코드가 있다고 상장사라고 판단하면 약 1,250개 회사가 틀린다고 전합니다. 회사 이름이 바뀌어도 목록에 옛 이름이 남아 있는 경우가 있습니다. 그래서 현재 이름으로 검색하면 안 나오거나, 옛 이름으로 검색하면 옛 기록이 나옵니다. AI에게 회사 정보를 물을 때는 사업자등록번호나 법인등록번호를 함께 주고, 국세청 사업자 상태 조회로 지금 영업 중인지도 따로 확인해야 합니다.
