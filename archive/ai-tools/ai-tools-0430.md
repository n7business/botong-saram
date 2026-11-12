---
id: ai-tools-0430
domain: ai-tools
claim: AI로 만든 웹 서비스를 공개하기 전에는 배포 파일에 API 키·토큰·서버 주소가 그대로 남아 있지 않은지 점검해야 하는데, 코드 압축은
  숨기는 장치가 아니고 이제는 AI가 압축된 코드도 대신 읽어 주기 때문이다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://yozm.wishket.com/magazine/detail/4028/
  author: 효빈
  seen: '2026-11-10'
  quote: .env 파일을 Git에 올리지 않았더라도, 번들에 들어간 값은 배포와 동시에 공개됩니다.
  source: 요즘IT
first_seen: '2026-11-10'
last_confirmed: '2026-11-10'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- API키
- 배포점검
- 바이브코딩
verified_by: 실무자 실측(단일 출처)
---
코드 압축(minify)은 파일 크기를 줄이려는 것이지 내용을 숨기는 장치가 아닙니다. 예를 들어 Vite에서 VITE_로 시작하는 환경 변수는 빌드할 때 배포 파일 안에 문자열로 그대로 들어가므로, .env 파일을 git에 올리지 않았더라도 배포하는 순간 공개됩니다. 기능마다 따로 챙기기보다 개발을 다 마친 뒤 배포 직전에 배포 파일에서 키·토큰·서버 주소를 한꺼번에 검색해 보세요. 비밀 키는 브라우저 쪽 코드가 아니라 서버 쪽에 두어야 합니다.
