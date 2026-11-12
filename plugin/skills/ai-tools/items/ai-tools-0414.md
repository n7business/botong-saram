# AI에게 문서 묶음을 정리한 위키를 만들게 하는 것은 여러 문서를 엮어야 답이 나오는 질문이 많을 때만 하고, 문서 하나에서 검색으로 찾을 수 있는 일에는 만들지 말아야 들인 품만큼 효과를 본다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic 실험에서 여러 문서를 합치고 계산이나 판단까지 해야 하는 합병 관련 질문은 위키를 참고했을 때 87%, 검색만 썼을 때 73%를 맞혔습니다. 반대로 대부분 기준을 문서 하나에서 찾을 수 있는 과제에서는 위키의 효과가 뚜렷하지 않았습니다. 어떤 과제에서는 위키가 원본 문서보다 커져 요약 구실을 전혀 하지 못했습니다. 계약서·서류 묶음을 AI로 정리할 때는 질문이 여러 문서를 넘나드는지 먼저 따져 보고, 위키가 원본보다 커지지 않는지 확인해야 합니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > Claude scored 87% when it consulted the wiki, compared with 73% when it used search alone.
