---
id: marketing-1046
domain: marketing
claim: 메인 페이지나 본문 페이지의 meta 태그에 noindex가 들어 있으면 그 페이지는 네이버 검색 결과에서 빠지므로, 홈페이지가 검색되지
  않을 때는 먼저 noindex 설정이 있는지 확인해 지워야 합니다.
status: merged
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-25'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-25'
last_confirmed: '2026-11-25'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버SEO
- noindex
- nofollow
- 검색누락
merged_into: marketing-0936
---
네이버는 <meta name="robots" content="noindex">가 적힌 페이지를 검색 결과에 넣지 않습니다. 제작 중에 넣어 둔 noindex를 공개할 때 빼먹는 일이 많으니, 사이트가 검색되지 않으면 이것부터 확인하세요. 페이지 안의 링크가 수집되지 않는다면 nofollow 설정도 함께 확인합니다. robots.txt와 방화벽이 네이버 검색로봇(Yeti)을 막고 있지 않은지도 같이 점검해야 합니다.
