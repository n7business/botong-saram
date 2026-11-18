---
id: factory-ax-0220
domain: factory-ax
claim: 홈페이지·쇼핑몰·게시판·관리자 페이지(워드프레스, 그누보드 등)를 운영하는 사업자가 PHP 8.1 이하 구버전을 쓰고 있다면 같은 버전
  안에서 패치하는 것으로 끝내지 말고 지원 중인 PHP 버전으로 옮겨야 한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://www.smart-factory.kr/usr/np/nm/ma/noticeMatterDetail
  author: 중소기업기술정보진흥원 스마트제조혁신추진단
  seen: '2026-11-19'
  quote: 구버전(PHP 8.1 이하)은 지원 버전으로 전환
  source: 스마트공장 사업관리시스템(스마트제조혁신추진단)
first_seen: '2026-11-19'
last_confirmed: '2026-11-19'
review_by: '2027-02-17'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- PHP2Shell
- 홈페이지
- 쇼핑몰
- KISA
verified_by: 공식 출처
---
정부가 PHP2Shell 취약점에 대해 안내한 기업 보안 대응 수칙에는 'PHP 8.1 이하 구버전은 지원 버전으로 전환'하라는 항목이 따로 들어 있습니다. 이 취약점은 로그인하지 않은 외부인도 서버에 명령을 실행할 수 있게 하고, 공격 코드는 이미 공개되어 있습니다. 해킹을 당하면 웹셸이 설치되거나 고객정보가 유출되고, 홈페이지가 변조되거나 내부망까지 침투당할 수 있습니다. 먼저 내 홈페이지·쇼핑몰이 어떤 PHP 버전으로 돌아가는지 확인하세요. 8.1 이하라면 지원 버전으로 옮기는 일정을 잡아야 합니다. 버전을 올린 뒤에는 워드프레스·그누보드 같은 프로그램과 플러그인이 새 버전에서 제대로 작동하는지도 함께 점검해야 합니다.
