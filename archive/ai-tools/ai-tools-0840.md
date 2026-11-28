---
id: ai-tools-0840
domain: ai-tools
claim: AI로 만든 도구에 쓰는 OAuth 토큰과 API 키는 채팅창에 붙여 넣지 말고 .env.local 같은 키 파일에 직접 적어야 하며,
  이 파일은 .gitignore에 넣어 Git 이력과 깃허브 푸시에서 빼야 한다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=mYCdZJIT9Ks
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-28'
  quote: OAuth 토큰은 보안 위험이 있으므로 .gitignore로 이력 관리와 깃허브 푸시에서 빼야 한다.
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-28'
last_confirmed: '2026-11-28'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 보안
- api-key
- gitignore
- env
- oauth
---
OAuth 토큰과 API 키는 내 구글 계정과 연결된 중요한 값입니다. 화자는 이 값을 .env.local이라는 키 보관 파일에 기록하고, 이 파일이 이력 관리에서 빠지게 했습니다. 키를 채팅창에 쓰는 것은 조심해야 하고, 파일을 직접 열어 고치는 것이 정석입니다. 프로젝트 폴더에서 Git 이력 관리를 시작할 때는 토큰 파일이 .gitignore에 들어갔는지 꼭 확인해야 합니다. 그래야 깃허브에 올렸을 때 키가 함께 공개되지 않습니다.
