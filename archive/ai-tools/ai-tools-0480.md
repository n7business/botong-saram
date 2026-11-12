---
id: ai-tools-0480
domain: ai-tools
claim: 웹페이지(HTML)로 만든 AI 영상을 파일로 저장할 때 화면 녹화를 쓰면 계산이 많은 장면에서 프레임이 빠질 수 있으므로, 한 프레임씩
  그려서 찍는 렌더링 방식으로 내보내야 한다.
status: candidate
evidence: anecdote
confidence: 0.6
sources:
- url: https://www.youtube.com/watch?v=zprZqlNpE9M
  author: 코드깎는노인
  seen: '2026-11-11'
  quote: 다만 계산이 많은 장면에서는 녹화 도중 프레임이 빠질 수 있다.
  source: 코드깎는노인
first_seen: '2026-11-11'
last_confirmed: '2026-11-11'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 영상제작
- 렌더링
- 모션그래픽
---
코딩 에이전트로 만든 모션 그래픽 영상은 동영상 파일이 아니라 브라우저에서 재생되는 웹페이지로 나오는 경우가 많다. 이것을 화면 녹화로 저장하면 무거운 장면에서 프레임이 빠져 끊겨 보일 수 있다. 프레임을 하나씩 그려 찍는 렌더링 스크립트를 쓰면 프레임 손실 없이 원하는 해상도로 MP4를 만들 수 있다. 직접 실행이 어렵다면 에이전트에게 '영상 파일로 만들어 줘'라고 맡기면 된다.
