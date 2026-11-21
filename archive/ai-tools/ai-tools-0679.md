---
id: ai-tools-0679
domain: ai-tools
claim: 클로드 코드의 체크포인트는 작업 중에 빨리 되돌릴 때만 쓰고, 오래 남겨야 하는 기록은 Git 커밋으로 남겨야 한다. 체크포인트는 기본
  설정에서 한 달쯤 지나면 지워지고, bash 명령으로 수정·삭제·이동한 파일은 되돌리지 못하기 때문이다.
status: candidate
evidence: policy
confidence: 0.75
sources:
- url: https://www.youtube.com/watch?v=nbdnpBBZJvc
  author: 코드깎는노인
  seen: '2026-11-21'
  quote: 체크포인트는 기본 설정으로 한 달쯤 지나면 지워지거든요
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
- claude-code
- 체크포인트
- git
---
클로드 코드 체크포인트는 클로드 코드가 파일 내용을 직접 고친 변경만 저장합니다. bash 명령으로 지우거나 옮기거나 고친 파일은 체크포인트로 되돌릴 수 없습니다. 기본 설정에서는 체크포인트가 한 달쯤 지나면 지워집니다. 화자에 따르면 앤트로픽도 장기 기록에는 Git 같은 버전 관리 도구를 계속 쓰라고 안내합니다. 작업 중 빠른 되돌리기는 체크포인트로 하고, 남겨 둘 상태는 커밋하세요.
