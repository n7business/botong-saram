---
id: growth-0421
domain: growth
claim: 생년월일처럼 민감한 정보를 받는 앱을 서버 없이 폰 안에서만 계산하게 만들면, 출시한 뒤에는 서버에서 계산 오류를 고칠 수 없으므로 출시
  전에 나올 수 있는 입력 조합을 미리 모두 돌려 봐야 한다.
status: candidate
evidence: anecdote
confidence: 0.45
sources:
- url: https://disquiet.io/products/5402b3a4-49cb-407e-ad1c-5055ae8f6bf4
  author: 아이티팜
  seen: '2026-11-18'
  quote: 서버에서 고칠 수가 없으니 출시 전에 가능한 조합을 미리 다 돌려 봤습니다.
  source: 디스콰이엇
first_seen: '2026-11-18'
last_confirmed: '2026-11-18'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 앱개발
- 개인정보
- 출시전점검
- 1인개발
---
고객의 민감한 정보를 다루는 앱이나 서비스는 서버를 두지 않고 모든 계산을 기기 안에서 끝내면 가입·광고 없이 운영할 수 있고, 앱을 지우면 정보도 함께 지워진다. 대신 출시한 뒤에 계산 오류가 나와도 서버에서 한 번에 고칠 수 없고, 사용자가 앱을 업데이트해야만 바로잡힌다. 그래서 출시 전에 경계값과 예외가 되는 입력을 미리 모두 넣어 결과를 확인해야 한다. 운세 앱의 경우 입춘 전후, 태어난 곳의 진태양시, 옛 서머타임이 이런 경계값에 해당한다. 한 운세 앱 개발팀은 이 방식을 택한 뒤 출시 전에 가능한 조합을 모두 돌려 봤다고 전한다.
