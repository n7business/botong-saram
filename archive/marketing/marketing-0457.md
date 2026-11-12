---
id: marketing-0457
domain: marketing
claim: 홈페이지가 네이버 검색에 안 나오면 robots.txt·방화벽이 네이버 검색로봇(Yeti)을 막고 있는지, 페이지에 noindex 태그가
  붙어 있는지부터 확인해야 한다.
status: verified
evidence: policy
confidence: 0.92
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저 (NAVER Corp.)
  seen: '2026-11-09'
  quote: noindex가 표기된 페이지는 검색 반영에서 제외됩니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-09'
last_confirmed: '2026-11-09'
review_by: '2027-01-08'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- robots.txt
- noindex
- 검색누락
verified_by: 공식 출처
mentions: 1
---
meta 태그에 noindex가 표기된 페이지는 검색 반영에서 빠지고, nofollow가 붙은 페이지는 그 안의 링크를 수집하지 않습니다. 네이버 검색로봇의 이름(User-Agent)은 Yeti이므로 robots.txt와 웹서버·방화벽에서 이 로봇의 접근을 허용해야 합니다. 로봇을 꼭 막아야 한다면 IP 대역은 언제든 바뀔 수 있으니 IP로 막지 말고 robots.txt를 쓰세요. 관리자·개인정보 페이지만 Disallow로 막고 사이트 전체를 막는 설정(Disallow: /)은 피해야 합니다.
