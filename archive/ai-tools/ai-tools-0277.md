---
id: ai-tools-0277
domain: ai-tools
claim: 문서로 AI 위키를 만드는 일은 여러 문서를 합쳐 답해야 하는 업무에 쓰고, 문서 하나에서 검색으로 찾을 수 있는 업무라면 검색만으로
  시작하는 편이 낫다.
status: verified
evidence: observed
confidence: 0.75
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-07'
  quote: Claude scored 87% when it consulted the wiki, compared with 73% when it used
    search alone.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-07'
last_confirmed: '2026-11-07'
review_by: '2026-12-07'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- knowledge-base
- wiki
- search
verified_by: 실무자 실측(단일 출처)
---
합병 문서 질문 24개 중 여러 문서를 조합하거나 판단·계산이 필요한 항목에서 Claude는 위키를 볼 때 87%, 검색만 쓸 때 73%를 기록했습니다. 반면 대부분의 기준을 문서 하나에서 충족할 수 있는 LAB 과제에서는 위키의 뚜렷한 이득이 없었습니다. 다른 LAB 과제에서는 위키가 원본 문서보다 커져 사실상 아무것도 압축하지 못했습니다. 위키를 만들기 전에 자주 하는 질문이 여러 문서를 함께 봐야 하는 것인지 확인하고, 위키 크기가 원본에 가까워지면 다시 검토해야 합니다.
