---
id: marketing-0629
domain: marketing
claim: 서버 부담 등으로 네이버 검색로봇을 잠시 막아야 할 때는 robots.txt로 막지 말고 웹마스터도구 수집 설정에서 트래픽 제한량을 최소로
  지정해야 하며, robots.txt로 막으면 그동안 사이트 문서가 네이버 검색에서 빠질 수 있다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-13'
  quote: robots.txt로 검색로봇을 차단하는 방법도 있지만 이 경우 해당 기간 동안에 수집된 사이트 내의 문서는 네이버 검색에서 제외될
    수 있습니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2027-01-12'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 트래픽제한
- robots.txt
- 웹마스터도구
verified_by: 공식 출처
---
사이트 성능이나 내부 사정으로 네이버 검색로봇을 잠시 막아야 한다면, 웹마스터도구의 수집 설정에서 트래픽 제한량을 최소로 지정하는 방법을 권장합니다. robots.txt로 검색로봇을 차단할 수도 있지만, 그러면 차단 기간 동안 이미 수집된 사이트 문서가 네이버 검색에서 빠질 수 있습니다. 잠깐 멈추려다 기존 노출까지 잃지 않도록 일시 차단에는 트래픽 제한을 쓰세요.
