---
id: ai-tools-0175
domain: ai-tools
claim: AI로 새 프로젝트를 시작할 때는 첫 커밋 전에 .gitignore부터 만들어 API 키 같은 민감 정보를 등록해야 하며, 키가 한 번
  깃허브에 올라간 뒤에 적으면 늦다.
status: candidate
evidence: consensus
confidence: 0.85
sources:
- url: https://www.youtube.com/watch?v=CcRM0IHYriM
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-06'
  quote: 한 번 나간 키는 되돌릴 수가 없어요.
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- git
- gitignore
- 보안
- API키
- 바이브코딩
---
새 프로젝트를 시작할 때 AI에게 '새 프로젝트니까 깃이그노어부터 만들어 줘'라고 지시하고 환경 변수와 보안 키 등 민감 정보를 모두 등록하게 합니다. 여기에 적힌 파일은 깃이 추적하지 않아 커밋에도 푸시에도 포함되지 않습니다. 키가 적힌 파일이 깃허브에 올라가면 코드를 받는 사람이 키까지 받을 수 있고, 공개 저장소라면 누구나 볼 수 있습니다. 커밋은 되돌리고 브랜치는 버리면 되지만 이미 나간 키는 되돌릴 수 없습니다.
