---
id: growth-0283
domain: growth
claim: KOSIS OpenAPI로 서비스를 만든 사업자는 API가 예고 없이 중단되거나 다른 방식으로 바뀌거나 아예 끝날 수 있다는 점에 대비해야
  하며, 발급받은 인증키는 남에게 넘기거나 담보로 쓰면 안 된다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://kosis.kr/serviceInfo/applicationClause.do
  author: 국가데이터처
  seen: '2026-11-12'
  quote: 현재 제공되는 공공정보 서비스를 완전히 중단할 수 있습니다.
  source: KOSIS 국가통계포털
- url: https://kosis.kr/serviceInfo/applicationClause.do
  author: 국가데이터처
  seen: '2026-11-12'
  quote: OpenAPI 접속 인증키(key)의 무단 양도, 증여 및 담보 목적물로 사용하는 행위
  source: KOSIS 국가통계포털
first_seen: '2026-11-12'
last_confirmed: '2026-11-12'
review_by: '2027-02-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- KOSIS
- OpenAPI
- 서비스중단
- 인증키
- 리스크관리
verified_by: 공식 출처
---
KOSIS 통계정보 활용약관에 따르면 긴급 점검 같은 부득이한 사유가 있으면 OpenAPI·다운로드 서비스가 예고 없이 일시 중단될 수 있습니다. 기능 개선이나 보안을 이유로 새 방식으로 교체되거나 완전히 중단될 수도 있으며, 국가데이터처는 서비스를 계속 제공한다고 보장하지 않습니다. 따라서 유료 고객에게 KOSIS 수치를 보여 주는 서비스라면 마지막으로 받은 데이터를 따로 저장해 두고, API가 멈췄을 때 고객에게 안내할 방법을 미리 정해 두어야 합니다. 활용자는 공지사항을 주기적으로 확인할 의무가 있습니다. 인증키를 무단으로 양도·증여하거나 담보로 쓰는 행위, 연결 방식을 위·변조하는 행위는 금지됩니다.
