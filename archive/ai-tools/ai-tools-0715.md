---
id: ai-tools-0715
domain: ai-tools
claim: 클로드 코드의 /rewind로 파일을 되돌린 뒤에는 파일 내용이 원하는 시점의 것인지 직접 열어 확인해야 합니다. v2.1.330 이전
  버전에서는 대기 중이던 요청 두 개나 겹쳐 실행된 스킬이 함께 돌면 더 오래된 버전으로 복원되는 경우가 있었습니다.
status: verified
evidence: policy
confidence: 0.75
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  author: anthropics
  seen: '2026-11-23'
  quote: '`/rewind` sometimes restoring an older version of a file'
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-23'
last_confirmed: '2026-11-23'
review_by: '2026-12-23'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- rewind
- 체크포인트
- 업데이트
verified_by: 공식 출처
---
/rewind는 작업 중에 빨리 되돌릴 때 쓰는 기능입니다. 그런데 v2.1.330 이전에는 파일을 바꾼 응답 바로 뒤에 대기 중이던 요청 두 개나 겹쳐 실행된 스킬이 함께 돌면, 원하는 시점보다 더 오래된 버전으로 파일이 복원되는 경우가 있었습니다. v2.1.330 이상으로 업데이트하세요. 되돌린 뒤에는 파일을 열어 내용이 맞는지 확인하는 것이 좋습니다. 중요한 시점은 체크포인트에만 맡기지 말고 Git 커밋으로 남겨 두세요.
