---
id: ai-tools-0684
domain: ai-tools
claim: 잃어버리면 곤란한 AI 프로젝트는 Git 커밋만 해 두지 말고 GitHub 비공개 저장소에 푸시해 두어야 하며, 여러 컴퓨터를 오간다면
  시작할 때 받아오고(pull) 끝나면 올려야(push) 한다. Git 기록은 프로젝트 폴더 안에만 있어 폴더를 지우거나 컴퓨터가 고장 나면 함께
  사라지고, GitHub는 드롭박스처럼 자동으로 올라가지 않기 때문이다.
status: candidate
evidence: consensus
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 그러니까 시작할 때 받아오고 끝나면 올린다
  source: 코드깎는노인
first_seen: '2026-11-21'
last_confirmed: '2026-11-21'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- github
- 백업
- push
- pull
- 여러기기
---
커밋은 내 컴퓨터에 기록을 남기는 것이고, 푸시는 그 커밋을 GitHub로 보내는 것입니다. 커밋하지 않은 변경도, 커밋만 하고 푸시하지 않은 커밋도 GitHub에는 없습니다. 에이전트가 '푸시 안 된 커밋 1개'라고 하면 그 기록은 아직 내 컴퓨터에만 있다는 뜻입니다. 무료 개인 계정에서도 비공개 저장소를 만들 수 있고, 컴퓨터를 바꾸면 clone으로 전체 이력을 그대로 가져올 수 있습니다. 두 컴퓨터에서 받아오기·올리기를 잊은 채 따로 고치면 나중에 두 버전을 합쳐야 합니다.
