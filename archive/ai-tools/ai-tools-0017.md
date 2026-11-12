---
id: ai-tools-0017
domain: ai-tools
claim: Claude로 PPT를 만들 때는 레퍼런스 이미지·컬러 코드·폰트 파일·로고 여백 지시를 함께 주고 2페이지 샘플만 먼저 뽑아 수정한
  뒤 전체를 생성하고, 완성된 디자인은 스킬로 저장해 재사용한다.
status: candidate
evidence: consensus
confidence: 0.55
sources:
- url: https://yozm.wishket.com/magazine/detail/3967/
  author: 디논 (요즘IT)
  seen: '2026-11-03'
  quote: 우선 2페이지만 샘플로 만들어달라고 했다.
  source: 요즘IT
- url: https://www.youtube.com/watch?v=IXQ-bzPksRo
  author: 레인 | AI 바이브코딩 (@Vibe_RaiN)
  seen: '2026-11-06'
  quote: 그래서 레퍼런스를 주게 되면 기본적으로이 정도 이상의 퀄리티가 나옵니다.
  source: 레인 | AI 바이브코딩 (@Vibe_RaiN)
first_seen: '2026-11-03'
last_confirmed: '2026-11-06'
review_by: null
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude
- PPT
- 스킬
- 디자인
mentions: 2
---
전체 페이지를 한 번에 생성하면 토큰이 많이 들고 느리므로, 먼저 1~2페이지 샘플을 만들어 폰트·그라데이션·여백을 확인하고 수정 요청한 다음 나머지를 같은 디자인으로 만들게 한다. 프롬프트에는 핀터레스트 등에서 찾은 레퍼런스 이미지 여러 장, 스포이드로 추출한 컬러 코드, OTF/TTF 폰트 파일, 모서리 반경 같은 디테일, 로고 넣을 공간을 비워달라는 지시를 포함한다. 로고 여백을 미리 말하지 않으면 제목이 페이지를 꽉 채워 추가 수정이 생긴다. 글자 간격·도형 크기 같은 세부 밸런스는 AI에 시키면 시간과 토큰이 낭비되니 파워포인트에서 직접 고친다. 마무리된 파일을 스킬로 만들어달라고 하면 색상·폰트·여백 규칙과 에셋이 포함된 스킬이 생성되어, 이후 같은 톤앤매너의 PPT를 슬래시(/)로 불러 빠르게 만들 수 있다. 수정이 3~4번 넘어가면 무료 토큰이 소진되니 유료 구독을 고려한다.
