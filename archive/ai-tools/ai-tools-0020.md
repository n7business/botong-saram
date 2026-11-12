---
id: ai-tools-0020
domain: ai-tools
claim: Claude Code가 작업 폴더 밖 파일을 건드리는 사고를 막으려면 settings.json에 permissions.blockWritesOutsideWorkingDirectories를
  켜서 모든 권한 모드에서 외부 경로 쓰기를 차단한다.
status: verified
evidence: policy
confidence: 0.85
sources:
- url: https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#21314
  author: anthropics
  seen: '2026-11-03'
  quote: Write, Edit and NotebookEdit refuse paths outside the working directories
    in every permission mode
  source: Claude Code 릴리스 노트 (CHANGELOG)
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- claude-code
- permissions
- safety
- settings
verified_by: 공식 출처
---
Claude Code 2.1.314부터 permissions.blockWritesOutsideWorkingDirectories 설정이 추가됐다. 켜 두면 Write·Edit·NotebookEdit 도구가 작업 디렉터리 밖 경로를 모든 권한 모드(auto 모드 포함)에서 거부한다. 자동 승인 모드로 오래 돌리거나 예약 작업을 쓰는 1인 사업자에게 특히 유용한 안전장치다. 홈 디렉터리의 설정 파일이나 다른 프로젝트를 실수로 덮어쓰는 사고를 설정 한 줄로 예방할 수 있다. 여러 폴더를 함께 다뤄야 하면 --add-dir로 작업 디렉터리를 명시적으로 늘린다.
