---
id: ai-tools-0299
domain: ai-tools
claim: 새 프로젝트를 시작하면 AI에게 .gitignore부터 만들게 해야 API 키와 시크릿 키가 커밋되어 GitHub에 올라가는 일을 막을
  수 있다.
status: verified
evidence: consensus
confidence: 0.85
sources:
- url: https://www.youtube.com/watch?v=wa5BtVLAcNs
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-07'
  quote: 한 번 나간 키는 되돌릴 수가 없어요.
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
- url: https://www.youtube.com/watch?v=D-3Iojr7dIc
  author: 양실장의 바이브코딩대학 (@VibecodingUniversity)
  seen: '2026-11-07'
  quote: API 키 같은 것들은 기터브 같은 공개 저장소에 그대로 올리면 안 됩니다.
  source: 양실장의 바이브코딩대학 (@VibecodingUniversity)
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- gitignore
- API키
- 보안
verified_by: 독립 2곳 weight 1.4
---
키가 파일에 적힌 채 커밋되어 GitHub에 올라가면 다른 사람이 코드를 받을 때 키까지 받을 수 있고, 공개 레포라면 누구나 볼 수 있습니다. .gitignore는 Git이 아예 추적하지 않을 파일 목록입니다. 작업 초기에 '새 프로젝트니까 .gitignore부터 만들어줘'라고 지시해 환경 변수·보안키·민감 정보를 등록합니다. 한 번 나간 키는 되돌릴 수 없으므로 .gitignore가 만들어진 뒤에도 키 관리에 계속 유의합니다.
