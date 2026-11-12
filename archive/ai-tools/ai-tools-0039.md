---
id: ai-tools-0039
domain: ai-tools
claim: GitHub에 공개된 에이전트는 빈 폴더를 만들어 Claude Code나 ChatGPT Work로 연 뒤 링크를 붙여넣고 '이 저장소를
  현재 폴더에 클론하고 쓸 수 있게 세팅해 줘'라고만 하면 설치되고, README를 사람이 읽을 필요가 없다.
status: candidate
evidence: anecdote
confidence: 0.7
sources:
- url: https://www.youtube.com/watch?v=iJfRqfDetsI
  author: 일잘러 장피엠
  seen: '2026-11-03'
  quote: 이건 사람만 읽는게 아닙니다.
  source: 일잘러 장피엠
- url: https://www.youtube.com/watch?v=P9EfmIrgjXw
  author: 일잘러 장피엠
  seen: '2026-11-03'
  quote: 에이전트나 스킬이라고 하는게 말은 거창하지만 결국 한 폴더 속 파일의 집합이거든요.
  source: 일잘러 장피엠
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- github
- 에이전트-설치
- 비개발자
---
에이전트·스킬은 결국 한 폴더 안의 파일 묶음이므로 비개발자도 GitHub에서 받아 쓸 수 있다. 컴퓨터 아무 곳에 빈 폴더를 만들고 Claude Code(또는 ChatGPT Work) 데스크톱 앱에서 그 폴더를 연 다음, GitHub 링크를 붙여넣고 '이 GitHub 저장소를 현재 폴더에 클론하고 사용할 수 있게 세팅해 줘'라고 요청한다. '클론'이라는 용어를 몰라도 'GitHub 링크를 적용하고 싶은데 어떻게 하면 돼?'라고 물으면 된다. README는 에이전트가 읽고 알아서 세팅하는 문서이므로 사람이 이해하려 애쓰지 않아도 된다. 설치 도중 실패하면 댓글이나 검색 대신 에이전트에게 '이거 왜 실패했어? 고쳐 줘'라고 하면 이유를 설명하고 고쳐 준다.
