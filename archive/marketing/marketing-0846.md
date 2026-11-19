---
id: marketing-0846
domain: marketing
claim: 홈페이지 메인 페이지가 자바스크립트나 meta refresh로 다른 주소로 넘어가거나 소유 확인용 태그를 frame 태그 안에 넣으면
  네이버 웹마스터도구의 사이트 소유 확인이 되지 않으므로, HTTP redirect를 쓰고 확인용 태그는 frame 바깥에 넣어야 합니다.
status: verified
evidence: policy
confidence: 0.9
sources:
- url: https://searchadvisor.naver.com/guide/seo-basic-intro
  author: 네이버 서치어드바이저
  seen: '2026-11-20'
  quote: frame 태그 내부에 소유 확인용 HTML 태그를 넣었다면 지원이 불가능합니다.
  source: 네이버 서치어드바이저 가이드 (SEO 공식)
first_seen: '2026-11-20'
last_confirmed: '2026-11-20'
review_by: '2027-01-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 네이버
- SEO
- 웹마스터도구
- 소유확인
- 홈페이지
verified_by: 공식 출처
---
네이버 서치어드바이저 웹마스터도구에 사이트를 등록하려면 소유 확인을 해야 합니다. 방법은 HTML meta 태그를 넣거나 HTML 파일을 올리는 것입니다. 메인 페이지가 자바스크립트나 meta refresh로 다른 주소로 넘어가면 소유 확인이 지원되지 않으니 HTTP redirect로 바꿔야 합니다. 확인용 태그를 frame 태그 안에 넣어도 실패하므로 frame 바깥에 넣으세요. 사이트 등록은 www.mysite.com처럼 호스트 단위로만 되고 www.mysite.com/myid 같은 하위 경로는 등록할 수 없습니다. HTML을 고칠 권한이 없으면 제작업체에 요청하세요.
