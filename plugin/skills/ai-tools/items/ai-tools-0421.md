# NAS 공유 폴더나 WSL 폴더 같은 네트워크 경로의 파일을 클로드 코드로 고쳤다면, 2.1.321 이전 버전은 파일 전체를 바꾸거나 노트북 첫 셀을 지울 수 있었으므로 업데이트하고 그동안 고친 파일을 백업과 대조해야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

2.1.321 이전 버전에서는 UNC 공유, WSL 폴더, /net 마운트 같은 네트워크 경로에서 편집 오류가 있었습니다. Edit가 같은 문구 여러 곳 중 첫 번째만 바꾸거나, 바꿀 문구가 비어 있으면 파일 전체를 덮어쓰거나, 노트북을 일반 텍스트처럼 편집하는 문제입니다. NotebookEdit는 셀을 지정하지 않으면 첫 셀을 지우거나 덮어쓰기도 했습니다. 사무실 NAS에 둔 업무 파일을 클로드 코드로 작업했다면 업데이트한 뒤 최근에 고친 파일이 백업본과 맞는지 확인하세요.

- 근거 policy · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 공식 출처

## 출처
- anthropics · 2026-11-10 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > replacing a whole file on an empty `old_string`
