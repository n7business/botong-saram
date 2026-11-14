---
id: marketing-0707
domain: marketing
claim: 홈페이지를 네이버 웹마스터도구에 등록할 때는 www.mysite.com처럼 호스트 단위로 등록해야 하며, 메인 페이지가 자바스크립트나
  meta refresh로 이동하거나 소유 확인 태그를 frame 안에 넣으면 소유 확인이 되지 않습니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: NAVER Corp. (네이버 서치어드바이저)
  seen: '2026-11-15'
  quote: 사이트 등록은 호스트 단위만 지원합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-15'
last_confirmed: '2026-11-15'
review_by: '2027-01-14'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- 웹마스터도구
- 서치어드바이저
- 소유확인
- 홈페이지
verified_by: 공식 출처
---
웹마스터도구 사이트 등록은 호스트 단위만 받습니다. www.mysite.com이나 blog.mysite.com은 되고, www.mysite.com/myid처럼 하위 경로는 안 됩니다. 소유 확인은 HTML meta 태그를 넣거나 HTML 파일을 올려서 합니다. 메인 페이지가 자바스크립트나 meta refresh로 다른 곳으로 이동하면 소유 확인이 안 되므로 HTTP redirect로 바꿔야 합니다. 확인용 태그를 frame 안에 넣었거나 내려받은 HTML 파일이 손상돼도 실패합니다. HTML을 고칠 권한이 없다면 제작업체에 요청하세요.
