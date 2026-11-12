---
id: licensing-0107
domain: licensing
claim: 기업마당의 지원사업 공고·행사정보는 REST/JSON API로 제공되므로, 공고를 자사 서비스에 연계하려는 사업자는 공고정보·행사정보
  API를 신청해 쓸 수 있다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://portal.smes.go.kr/home/cs/opndata/UI_USR_L_210
  author: 중소벤처기업부 (중소벤처24)
  seen: '2026-11-06'
  quote: 국민, 기업, 지원기관 등 누구나 참고하고 활용할 수 있도록
  source: 중소벤처24
- url: https://portal.smes.go.kr/home/cs/opndata/UI_USR_L_210
  author: 중소벤처기업부 (중소벤처24)
  seen: '2026-11-06'
  quote: 해당 인증키는 신청 및 가능여부를 판단하여 제공하고 있습니다.
  source: 중소벤처24
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 중소벤처24
- OpenAPI
- 기업마당
- 지원사업
---
공고정보 API는 공고명, 기간, 지원기관, 신청상태, 첨부파일 등의 항목을 제공한다. 행사정보 API는 중소기업이 참여 가능한 교육, 세미나, 전시회 정보를 제공한다. 두 API는 국민, 기업, 지원기관 등 누구나 활용할 수 있도록 제공되며, 운영 중인 서비스에 연계해 적용할 수 있다. 다만 인증키는 신청 후 가능 여부를 판단해 제공하므로 신청만으로 발급된다고 전제하면 안 된다.
