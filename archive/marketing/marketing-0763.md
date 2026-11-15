---
id: marketing-0763
domain: marketing
claim: 서버 부담 때문에 네이버 검색로봇을 잠시 막아야 할 때는 robots.txt로 차단하지 말고 웹마스터도구 수집 설정에서 트래픽 제한량을
  최소로 지정해야 하며, robots.txt로 막으면 그동안 수집된 문서가 네이버 검색에서 빠질 수 있습니다.
status: merged
evidence: policy
confidence: 0.85
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-16'
  quote: 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 것을 권장합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-16'
last_confirmed: '2026-11-16'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- 웹마스터도구
- robots.txt
- 트래픽제한
merged_into: marketing-0629
---
사이트 성능이나 내부 사정으로 검색로봇 접근을 잠깐 줄여야 할 때가 있습니다. 이때 robots.txt로 막으면 그 기간에 이미 수집된 문서가 검색 결과에서 제외될 수 있습니다. 네이버 서치어드바이저 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 방법을 쓰면 됩니다. 로봇 차단이 꼭 필요하더라도 IP 대역은 언제든 바뀔 수 있으므로 IP 기준으로 막지 말아야 합니다.
