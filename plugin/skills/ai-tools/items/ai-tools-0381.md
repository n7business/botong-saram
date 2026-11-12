# AI가 쓴 코드가 너무 많아 한 줄씩 읽을 수 없다면 그 변경이 무엇을 하려는 것인지, 의도가 맞는지를 중심으로 검토하되 검토 자체는 빼먹지 말아야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic 팀은 지금도 모든 변경 요청을 사람이 검토하지만, 코드를 한 줄씩 읽는 대신 변경의 의도를 확인하는 방식으로 바꿨다고 밝혔습니다. AI가 만드는 코드 양이 사람이 읽을 수 있는 양을 넘어서면 전부 정독하는 방식은 유지할 수 없습니다. 그렇다고 검토를 건너뛰면 안 되고, '이 수정이 내가 요청한 문제를 푸는 것이 맞는가', '건드리면 안 되는 곳까지 바꾸지 않았는가'를 확인해야 합니다. 결제나 개인정보처럼 피해가 큰 부분은 지금처럼 더 꼼꼼히 봐야 합니다.

- 근거 anecdote · 처음 2026-11-09 · 최근 확인 2026-11-09 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-09 · https://www.anthropic.com/research/redesigning-source-control
  > they now examine the intent of the change as opposed to reading every line of code.
