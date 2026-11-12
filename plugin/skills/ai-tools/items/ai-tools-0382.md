# 운영 중인 시스템을 AI로 감시하려면 하나의 AI에게 여러 시스템을 맡기지 말고, 시스템마다 전담 AI를 두어 로그와 지표를 계속 보게 해야 일반 알림이 놓치는 미묘한 이상을 잡아낼 수 있다.

🏛 공식 발표 · Anthropic Engineering 블로그

Anthropic은 시스템 구성 요소마다 슬랙 채널을 따로 만들고, 각 채널의 Claude에게 그 구성 요소 하나의 상태만 집요하게 살피게 했습니다. 이 Claude들은 텔레메트리와 로그를 볼 수 있으며, 차트를 새로 고치며 이상한 점을 찾는 숙련 엔지니어처럼 움직였습니다. 기존 알림도 함께 운영했지만, 전담 AI는 알림이 잡지 못하는 미묘하고 새로운 문제를 발견했습니다. 이 방식은 기존 알림을 대체하는 것이 아니라 보완하는 것이므로, 기본 알림은 그대로 유지해야 합니다.

- 근거 anecdote · 처음 2026-11-09 · 최근 확인 2026-11-09 · 재검토 —

## 출처
- Anthropic Engineering · 2026-11-09 · https://www.anthropic.com/research/redesigning-source-control
  > we tasked Claude with being obsessively focused on the health of a single component.
