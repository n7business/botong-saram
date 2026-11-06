---
id: ai-tools-0176
domain: ai-tools
claim: AI에게 코드 수정을 맡기기 전과 한 작업 단위를 마칠 때마다 커밋해 두면, 일이 잘못됐을 때 원하는 시점을 골라 되돌릴 수 있다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=CcRM0IHYriM
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-06'
  quote: 작업 시작 전에 지금 상태 커밋 해줘
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
- url: https://www.youtube.com/watch?v=c8nIC6qzLUY
  author: 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm)
  seen: '2026-11-03'
  quote: 타임머신에다가이 포인트를 저장을 해 두는 거랑 같다고 했어요.
  source: 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- git
- 커밋
- 롤백
- 바이브코딩
- claude-code
mentions: 2
---
작업을 시작할 때 '작업 시작 전에 지금 상태 커밋해 줘'라고 지시하고, 작업이 끝나면 다시 커밋이나 푸시를 시킵니다. 깃은 언제 무엇을 바꿨는지 기록하므로 '최종본', 'V4'처럼 파일을 복사해 둘 필요가 없습니다. 칸 이름 같은 용어를 외울 필요는 없고, 커밋하면 내 저장소에 확정적으로 쌓인다는 것만 알면 됩니다. 커밋까지는 내 컴퓨터 안의 일이고, 푸시해야 깃허브에 올라갑니다. Claude Code가 '커밋할까요?'라고 물을 때 이 차이를 알고 답합니다.
