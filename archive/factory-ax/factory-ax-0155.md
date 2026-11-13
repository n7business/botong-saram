---
id: factory-ax-0155
domain: factory-ax
claim: PHP2Shell 취약점 때문에 PHP를 업데이트한 사업자는 업데이트만 하고 끝내지 말고, 업데이트 후 로그를 점검하고 관리자 비밀번호
  같은 중요 인증정보를 바꿔야 한다.
status: verified
evidence: policy
confidence: 0.8
sources:
- url: https://www.smart-factory.kr/usr/np/nm/ma/noticeMatterDetail
  author: 중소기업기술정보진흥원(TIPA)
  seen: '2026-11-13'
  quote: 5. 업데이트 후 로그 점검 6. 중요 인증정보 교체
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
- 침해사고
- 인증정보
verified_by: 공식 출처
---
과기정통부·KISA가 안내한 기업 보안 대응 수칙에는 업데이트 다음 단계로 '업데이트 후 로그 점검'과 '중요 인증정보 교체'가 들어 있습니다. 공격코드가 이미 공개된 상태라 업데이트 전에 이미 침입당했을 수 있기 때문입니다. 즉시 업데이트가 어렵다면 임시 조치라도 먼저 해야 합니다. 침해 흔적이 보이면 정해진 침해사고 대응 절차를 따르세요. 출처가 불분명한 공격 시험코드(PoC)를 내 서버에서 직접 돌려 보는 것은 피해야 합니다.
