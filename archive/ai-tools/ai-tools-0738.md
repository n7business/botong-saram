---
id: ai-tools-0738
domain: ai-tools
claim: AI 코딩 도구에 일을 맡길 때는 '꾸며 줘', '고쳐 줘'로 끝내지 말고, 시작 전에 무엇이 되면 완료인지를 검사 가능한 항목으로 정해
  주고 그 항목대로 확인한 결과를 보여 달라고 해야 한다.
status: verified
evidence: consensus
confidence: 0.55
sources:
- url: https://www.gpters.org/dev/post/when-graded-my-claude
  author: 정한샘
  seen: '2026-11-23'
  quote: 두 번 다 "완료 기준과 검증"이 가장 낮았어요(27점, 17점).
  source: 지피터스 GPTers
- url: https://www.anthropic.com/research/harness-design-long-running-apps
  author: Anthropic
  seen: '2026-11-19'
  quote: agreeing on what "done" looked like for that chunk of work before any code
    was written.
  source: Anthropic Engineering 블로그
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-19'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 프롬프트
- 완료기준
- 클로드코드
- 코덱스
- 지시작성
verified_by: 실무자 실측(단일 출처)
mentions: 2
---
화자는 일이 한 번에 끝나는 날과 몇 번씩 다시 설명하는 날이 갈리는 이유를 찾으려고, 자기 클로드 코드·코덱스 대화를 Anthropic·OpenAI 공식 가이드 기준으로 채점했습니다. 종합 점수는 58점과 53점이었고, 두 번 다 '완료 기준과 검증'이 27점과 17점으로 가장 낮았습니다. 끝났는지 판단할 기준을 말해 주지 않으면 에이전트도 스스로 확인할 방법이 없습니다. 예를 들어 'README 좀 꾸며 줘' 대신 '잘나가는 레포 10곳 이상의 공통점을 표로 보여 주고, 반영한 항목마다 근거를 달고, 깨진 링크가 없는지 확인한 결과도 보여 줘'처럼 쓰면 됩니다. 다만 채점을 AI가 해서 같은 대화도 돌릴 때마다 점수가 조금씩 달라질 수 있습니다.
