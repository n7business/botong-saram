---
id: factory-ax-0134
domain: factory-ax
claim: 홈페이지·쇼핑몰·게시판·관리자 페이지(워드프레스, 그누보드 등)를 PHP로 운영하는 사업자는 로그인 없이 외부에서 서버 명령을 실행할
  수 있는 PHP 취약점(PHP2Shell)의 공격코드가 이미 공개되었으므로, 지금 PHP 버전을 확인해 최신 버전으로 업데이트하고 PHP 8.1
  이하라면 지원 버전으로 바꿔야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://www.smart-factory.kr/usr/np/nm/ma/noticeMatterDetail
  author: 중소기업기술정보진흥원(TIPA)
  seen: '2026-11-11'
  quote: 구버전(PHP 8.1 이하)은 지원 버전으로 전환
  source: 스마트공장 사업관리시스템(스마트제조혁신추진단)
first_seen: '2026-11-11'
last_confirmed: '2026-11-14'
review_by: '2027-02-09'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- PHP
- 홈페이지
- 취약점
- KISA
- 호스팅
verified_by: 공식 출처
---
과기정통부·KISA 요청으로 스마트공장 사업관리시스템에 안내된 PHP 취약점은 로그인 없이 서버에 명령을 실행할 수 있고, 공격코드가 이미 공개되어 있습니다. 해킹되면 웹셸 설치, 고객정보 유출, 홈페이지 변조, 내부망 침투로 이어질 수 있으며, 2026-10-22 12시부로 민간 분야 사이버위기 경보가 '주의'로 올라갔습니다. 먼저 운영 중인 PHP 사용 현황을 확인하고, 최신 버전으로 업데이트한 뒤 재시작해야 합니다. PHP 8.1 이하 구버전은 지원 버전으로 바꾸고, 바로 업데이트하기 어려우면 임시 조치를 하세요. 업데이트한 뒤에는 로그를 점검하고 중요한 인증정보를 교체하세요. 출처가 불분명한 PoC(공격 검증 코드)는 실행하지 말아야 합니다. 호스팅 업체나 솔루션·장비 공급기업이 PHP를 관리한다면 그 업체에 보안 업데이트를 적용했는지 확인하고 적용을 요청해야 합니다.
