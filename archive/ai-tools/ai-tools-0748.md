---
id: ai-tools-0748
domain: ai-tools
claim: 사내 문서로 AI용 지식 위키를 만들 때는 여러 문서를 합쳐 봐야 답이 나오는 질문이 많은 경우에만 만들고, 검색 도구는 계속 함께 쓰게
  해야 한다. Anthropic 실험에서 여러 문서에 걸친 질문은 위키를 쓰면 87%, 검색만 쓰면 73%였지만, 문서 하나에서 찾으면 되는 과제에서는
  위키의 효과가 뚜렷하지 않았기 때문이다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: Claude scored 87% when it consulted the wiki, compared with 73% when it used
    search alone
  source: Anthropic Engineering 블로그
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2026-12-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- RAG
- 위키
- 사내문서
- 검색
verified_by: 실무자 실측(단일 출처)
---
Anthropic은 AI가 문서 묶음을 읽고 주제별로 서로 연결된 페이지(위키)를 만들게 한 뒤 질문에 답하게 했습니다. 인수합병 관련 질문 24개는 절반 이상이 여러 문서를 합쳐 봐야 풀리는 문제였는데, 이런 문항에서 위키를 쓰면 87%, 검색만 쓰면 73%를 맞혔습니다. 다른 회사 문서 35만 건으로 한 시험에서는 검색만 쓰면 53%, 검색과 위키를 함께 쓰면 61%였고, 질문 하나당 토큰을 약 2만 개 아꼈습니다. 반면 답이 문서 한 곳에 있는 과제에서는 위키가 검색보다 나은 점이 뚜렷하지 않았고, 어떤 과제에서는 위키가 원본 문서보다 커져 정리 효과가 없었습니다. 그래서 위키는 검색을 대신하는 것이 아니라 검색 옆에 두는 지도로 쓰고, 원본보다 커지지 않는지도 살펴야 합니다.
