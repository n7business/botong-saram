---
id: marketing-0963
domain: marketing
claim: robots.txt 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www가 붙은 주소·안 붙은 주소·https 주소를 함께 쓴다면
  각 주소의 robots.txt를 따로 확인해야 합니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-robots
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-23'
  quote: 같은 호스트, 프로토콜 및 포트 번호 하위의 페이지에 대해서만 유효합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- robots.txt
- www
merged_into: marketing-0851
---
네이버에 따르면 http://www.example.com/robots.txt의 규칙은 http://example.com/이나 https://example.com/에는 적용되지 않습니다. 그래서 한 주소에만 설정하면 다른 주소는 의도와 다르게 수집될 수 있습니다. 가장 깔끔한 방법은 대표 주소 하나를 정하고 나머지를 그쪽으로 redirect하는 것입니다. 수정한 뒤에는 웹마스터도구 robots.txt 도구에서 수집 요청을 누르면 검색로봇에게 빨리 알릴 수 있습니다.
