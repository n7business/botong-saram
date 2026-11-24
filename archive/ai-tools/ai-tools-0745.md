---
id: ai-tools-0745
domain: ai-tools
claim: AI 메모리에는 화면이나 원본 자료에서 언제든 다시 볼 수 있는 정보를 쌓지 말고, 직접 겪어서 알아낸 규칙·전략·계획만 남겨야 한다.
  Anthropic 실험에서 모든 것을 기록한 모델은 파일 413개를 만들고도 진행이 가장 더뎠고, 꼭 필요한 것만 적은 모델은 파일 9개로 훨씬
  멀리 나아갔기 때문이다.
status: verified
evidence: observed
confidence: 0.65
sources:
- url: https://www.anthropic.com/research/components-of-agent-memory
  author: Anthropic Engineering
  seen: '2026-11-24'
  quote: Sonnet 3.7 wrote 413 memory files across 225 folders and earned one badge
  source: Anthropic Engineering 블로그
first_seen: '2026-11-24'
last_confirmed: '2026-11-24'
review_by: '2026-12-24'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- agent-memory
- claude-code
- 메모리
- 정리
verified_by: 실무자 실측(단일 출처)
---
Anthropic이 포켓몬 게임으로 시험해 보니, Sonnet 3.7은 전투·아이템·인물마다 파일을 따로 만들어 폴더 225개에 파일 413개를 쌓았고 배지는 1개를 얻었습니다. Fable 5는 폴더 2개에 파일 9개와 현황판 파일 하나만 두고 배지 4개를 얻었습니다. 잔액이나 현재 위치처럼 바로 확인할 수 있는 정보는 금방 낡아서, 기록이 많을수록 메모리를 뒤지는 데 시간이 더 들고 정작 일은 진행되지 않았습니다. 사무실에서도 거래처 현재 잔액처럼 원장에서 바로 볼 수 있는 값보다는 '이 거래처는 서류를 두 번 요청해야 보낸다' 같이 겪어서 알게 된 규칙을 메모리에 남기는 것이 좋습니다. 두 모델 모두 한 번씩만 돌려 본 비교라는 점도 감안해야 합니다.
