---
id: marketing-0199
domain: marketing
claim: URL을 영구히 바꿀 때는 서버에서 301 redirect를, 일시적 장애나 잠깐의 페이지 변경에는 302 redirect를 써야 기존
  검색 정보를 잃을 위험을 줄일 수 있다.
status: merged
evidence: policy
confidence: 0.95
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-redirect
  author: NAVER Corp.
  seen: '2026-11-05'
  quote: 사이트나 페이지를 변경할 경우 301 Permanently Moved 형식의 redirect를 사용해 주세요.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2027-01-04'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 리다이렉트
- '301'
- '302'
verified_by: 공식 출처
merged_into: marketing-0026
---
URL을 바꾸면 검색로봇이 새 정보로 잘못 판단해 기존 검색 정보와 이용자 선호도 정보를 활용하지 못할 수 있으므로 301로 알립니다. 일시적 장애 때 응답이 없거나 변경을 인지하지 못하면 페이지가 삭제되거나 다른 정보로 바뀐 것으로 판단될 수 있으므로 302를 씁니다. 자바스크립트 redirect는 검색로봇이 이해하기 어렵고 스팸 문서 처리 과정에서 저평가될 수도 있으니 자제합니다. 연속 redirect는 최소화하고 5회를 넘기지 않으며, 거쳐 가는 모든 주소와 최종 주소는 수집 가능한 정상 페이지여야 합니다.
