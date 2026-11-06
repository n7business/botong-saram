---
id: ai-tools-0167
domain: ai-tools
claim: Claude Code v2.1.317 이전 버전은 검색이 시간 제한에 걸려 일부만 찾고도 전체 결과로 취급할 수 있으므로, 파일이 많은
  폴더를 다룬다면 업데이트하고 '없다'는 답은 직접 확인한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/releases/tag/v2.1.317
  author: ashwin-ant
  seen: '2026-11-06'
  quote: Fixed Claude treating partial Grep and Glob results as complete when a search
    hit its time limit
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- 검색
- 업데이트
- 검증
verified_by: 공식 출처
---
v2.1.317 이전에는 Grep·Glob 검색이 시간 제한에 걸렸을 때 Claude가 일부 결과를 전체 결과로 취급하는 문제가 있었고, 이 버전에서 수정됐다. 그래서 이전 버전이 파일이 많은 폴더에서 '해당 파일이 없다'거나 '여기서만 쓰인다'고 답하면 검색이 중간에 끊긴 결과일 수 있다. v2.1.317 이상으로 업데이트한다. 삭제나 일괄 수정처럼 검색 결과에 따라 움직이는 작업은 실행 전에 범위를 직접 확인한다.
