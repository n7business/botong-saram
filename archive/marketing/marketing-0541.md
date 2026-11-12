---
id: marketing-0541
domain: marketing
claim: 도메인을 옮길 때는 옛 주소와 새 주소를 페이지별로 1:1로 연결해 HTTP 301을 걸고, 새 사이트의 모든 페이지에 canonical
  주소를 지정한 다음, 웹마스터도구에 새 사이트를 등록하고 사이트맵을 내야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-migration
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-11'
  quote: 콘텐츠의 redirect는 URL 기준으로 1:1로 대응되어야 합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: '2027-01-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 사이트이전
- '301'
- canonical
verified_by: 공식 출처
---
옛 사이트의 콘텐츠를 이미지·첨부파일까지 모두 새 사이트로 옮긴 뒤 새 도메인을 연결합니다. 새 도메인을 네이버 로봇이 알아보기까지는 최소 2~3일이 걸릴 수 있습니다. 옛 주소로 들어오면 그 페이지에 해당하는 새 주소로 하나씩 보내도록 HTTP 301을 겁니다. 모두 메인으로만 보내면 안 됩니다. 새 사이트의 모든 페이지에 canonical 주소를 넣어 두어야 검색 결과에 옛 도메인이 대표 주소로 남지 않습니다. 새 사이트는 웹마스터도구에 등록하고 사이트맵을 낸 뒤 수집·색인 현황을 확인하고, 옛 사이트로 들어오는 방문자가 없어진 다음에 옛 서버를 끕니다.
