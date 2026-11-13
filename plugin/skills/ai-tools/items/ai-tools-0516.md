# AI용 문서 위키는 여러 문서의 내용을 합치거나 계산해야 답이 나오는 업무에 만들어야 하고, 답이 문서 한 곳에 그대로 있는 업무라면 위키를 만들어도 효과가 거의 없으므로 검색만 써도 된다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic 실험에서 합병 관련 질문 24개 가운데 여러 문서의 정보를 합쳐야 하는 문항은 위키를 참고했을 때 87%, 검색만 썼을 때 73%를 기록했습니다. 반면 답이 거의 문서 하나에 있는 법률 의견서 과제에서는 위키를 써도 검색보다 뚜렷하게 나아지지 않았습니다. 위키를 만들고 유지하는 데도 시간과 토큰이 들어가므로, 내 업무 질문이 여러 자료를 넘나드는지 먼저 따져 보고 위키를 만들지 정하는 것이 좋습니다.

- 근거 observed · 처음 2026-11-13 · 최근 확인 2026-11-13 · 재검토 2026-12-10 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-13 · https://www.anthropic.com/research/components-of-agent-memory
  > Claude scored 87% when it consulted the wiki, compared with 73% when it used search alone
