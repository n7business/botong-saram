---
id: ai-tools-0513
domain: ai-tools
claim: AI가 쌓아 둔 메모는 그대로 믿지 말고 주기적으로 원래 작업 기록(대화 기록)과 대조해 고치게 해야 하는데, 처음부터 틀렸거나 상황이
  바뀌어 틀려진 메모를 다음 세션의 AI가 그대로 믿고 같은 실수를 되풀이하기 때문이다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-13'
  quote: Dreaming gives Claude a way to test its notes against the original transcripts
  source: Anthropic Engineering 블로그
- url: https://www.youtube.com/watch?v=Ni0gE4LeSlc
  author: 조코딩 JoCoding
  seen: '2026-11-10'
  quote: 작업 사이에 AI를 '재워야' 한다.
  source: 조코딩 JoCoding
first_seen: '2026-11-13'
last_confirmed: '2026-11-13'
review_by: '2026-12-10'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- dreaming
- 검증
verified_by: 독립 2곳 weight 1.7
mentions: 2
---
AI는 작업 중에 중요하다고 판단한 내용을 메모로 남기기 때문에, 메모가 처음부터 틀렸거나 상황이 바뀌어 맞지 않게 될 수 있습니다. 다음 세션의 AI는 그 메모를 의심 없이 읽고 따릅니다. Anthropic 실험에서 위치를 잘못 적은 메모를 그대로 둔 클로드는 같은 함정에 세 번 빠진 뒤 다음 도시에 끝내 가지 못했습니다. 메모를 작업 기록과 대조해 고치는 과정(dreaming)을 거친 클로드는 동굴로 바로 돌아가 다음 도시에 도착했습니다. 일이 없는 시간에 '메모 내용을 원래 기록과 대조해 틀린 것을 고쳐라'라고 따로 시키는 것이 좋습니다.
