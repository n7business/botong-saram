---
id: ai-tools-0041
domain: ai-tools
claim: 네이버 카페·인스타그램처럼 로그인이 필요한 사이트를 에이전트로 수집할 때는 ID·비밀번호를 에이전트에 넘기지 말고, 에이전트가 띄운 브라우저
  창에서 사람이 직접 로그인(2단계 인증 포함)한 뒤 그 세션으로 수집하게 한다.
status: candidate
evidence: anecdote
confidence: 0.65
sources:
- url: https://www.youtube.com/watch?v=iJfRqfDetsI
  author: 일잘러 장피엠
  seen: '2026-11-03'
  quote: 에이전트는 ID와 비밀번호를 받거나 저장하지 않고
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
- 웹-수집
- 로그인
- 보안
- 네이버-카페
- 인스타그램
---
로그인 뒤에만 보이는 커뮤니티 글이나 해시태그 게시물도 수집할 수 있다. 에이전트가 로그인이 필요하다는 걸 알아채면 브라우저 창을 띄워 사용자에게 직접 로그인을 요청하고, ID와 비밀번호를 받거나 저장하지 않은 채 그 세션의 쿠키·로그인 상태만 이어받아 수집한다. 2단계 인증도 사람이 통과하면 그 상태로 계속 진행된다. 프롬프트에 계정 정보를 적어 주는 방식은 피하고, 이 '직접 로그인 후 세션 인계' 방식을 쓴다. 네이버 카페 최근 글 100개, 인스타그램 해시태그 게시물 50개의 계정명·본문·좋아요 수를 이 방식으로 엑셀에 모았다.
