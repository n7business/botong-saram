# AI가 작업 중에 남긴 메모는 틀려도 다음 세션에서 그대로 믿고 쓰이므로, 주기적으로 원래 대화 기록과 대조해 고치게 해야 같은 실수가 되풀이되는 일을 막을 수 있다.

🏛 공식 발표 · Anthropic Engineering 블로그, 조코딩 JoCoding

AI는 작업하면서 중요하다고 판단한 것을 메모에 적는데, 처음부터 틀렸거나 상황이 바뀌어 낡은 메모도 다음 세션에서는 사실로 믿습니다. 포켓몬 실험에서 클로드는 건물 위치를 잘못 적은 메모 때문에 같은 함정에 세 번 빠졌고, 끝내 다음 도시에 가지 못했습니다. 메모를 원래 기록과 대조해 고치는 과정(드리밍)을 거치자 바로 길을 찾아 다음 도시에 도착했습니다. 업무에서도 AI 메모리를 오래 쓰려면 원본 대화나 자료와 맞춰 보며 메모를 정리하는 시간을 따로 두는 것이 좋습니다.

- 근거 observed · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 독립 2곳 weight 1.7

## 출처
- Anthropic Engineering · 2026-11-10 · https://www.anthropic.com/research/components-of-agent-memory
  > Dreaming gives Claude a way to test its notes against the original transcripts
- 조코딩 JoCoding · 2026-11-10 · https://www.youtube.com/watch?v=Ni0gE4LeSlc
  > 작업 사이에 AI를 '재워야' 한다.
