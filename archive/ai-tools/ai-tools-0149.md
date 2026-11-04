---
id: ai-tools-0149
domain: ai-tools
claim: A2A로 오래 걸리는 일을 맡길 때는 폴링 대신 스트리밍이나 푸시로 진행을 확인하면 주고받는 데이터가 크게 줄어든다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://yozm.wishket.com/magazine/detail/4025/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 같은 일을 스트리밍으로 확인하면 이벤트 4개를 합쳐 1,287바이트였고
  source: 요즘IT
- url: https://yozm.wishket.com/magazine/detail/4024/
  author: 조훈(Hoon Jo)
  seen: '2026-11-05'
  quote: 연결한 뒤에도 보내기에 실패하면 서버 로그에만 남으니
  source: 요즘IT
first_seen: '2026-11-05'
last_confirmed: '2026-11-05'
review_by: '2026-12-05'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- A2A
- 폴링
- 스트리밍
- 푸시 알림
verified_by: 실무자 실측(단일 출처)
---
15초짜리 작업을 1초 간격으로 폴링하면 16번 확인하면서 6,916바이트를 받았습니다. 같은 일을 스트리밍으로 확인하면 1,287바이트, 푸시로 확인하면 465바이트였습니다. 다만 푸시는 알림 설정을 담아 둘 곳과 푸시를 보내는 부분을 직접 만들어 연결해야 합니다. 연결한 뒤에도 발송 실패는 서버 로그에만 남으니 그 로그를 함께 봅니다. 1초 안에 끝나는 짧은 호출에서는 진행 확인이나 취소를 쓸 일이 없어, 응답에 함께 오는 태스크 정보가 버려집니다.
