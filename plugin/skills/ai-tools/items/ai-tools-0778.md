# AI에게 챗봇 답변 채점을 맡길 때는 '10점 만점에 몇 점' 같은 총점 하나를 매기게 하지 말고, 기준을 '예/아니오'로 답할 수 있는 좁은 질문 여러 개로 나눠 하나씩 판정하게 해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

채점 기준을 '정중했나', '가격을 지어내지 않았나', '담당자 연결을 안내했나'처럼 예/아니오로 답할 수 있는 질문으로 쪼개서 채점 AI에게 줍니다. 질문이 좁고 분명할수록 채점 AI의 주관이 덜 끼어듭니다. 항목을 나눠 두면 어느 기준에서 점수가 깎였는지도 바로 보입니다. 애매한 경우를 채점 AI의 재량에 맡기지 말고, '이런 답은 불합격으로 본다'는 예를 채점 지시에 미리 적어 두어야 판정이 일정해집니다.

- 근거 consensus · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-25 · https://www.anthropic.com/research/building-strong-safety-evaluations
  > Opt for a set of yes/no questions over a single overall score.
