---
id: factory-ax-0154
domain: factory-ax
claim: 호스팅 업체나 솔루션·장비 공급기업이 홈페이지·쇼핑몰의 PHP를 관리하는 사업자는 직접 업데이트할 수 없더라도 PHP2Shell 취약점
  보안 업데이트를 적용했는지 해당 업체에 확인하고 요청해야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://www.smart-factory.kr/usr/np/nm/ma/noticeMatterDetail
  author: 중소기업기술정보진흥원(TIPA)
  seen: '2026-11-13'
  quote: 해당 업체에 보안 업데이트 적용 여부를 확인·요청해 주시기 바랍니다.
  source: 스마트공장 사업관리시스템(스마트제조혁신추진단)
first_seen: '2026-11-13'
last_confirmed: '2026-11-14'
review_by: '2027-02-11'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- PHP
- 홈페이지
- 호스팅
- 외주관리
verified_by: 공식 출처
---
로그인 없이 외부에서 서버 명령을 실행할 수 있는 PHP 취약점(PHP2Shell)의 공격코드가 이미 공개되어 있습니다. 2026-10-22 12시부터 민간 분야 사이버위기 경보도 '주의' 단계로 올라갔습니다. 홈페이지·쇼핑몰·게시판을 호스팅 업체나 제작·유지보수 업체에 맡겨 두었다면 내가 직접 할 일이 없다고 넘기기 쉽습니다. 하지만 업데이트가 실제로 적용됐는지는 업체에 직접 확인하고 요청해야 합니다. 해킹되면 웹셸 설치, 고객정보 유출, 홈페이지 변조, 내부망 침투로 이어질 수 있습니다.
