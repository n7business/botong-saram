# claude remote-control에 --settings로 설정 파일을 지정해 쓰다가 그 파일을 고쳤다면 claude remote-control을 다시 시작해야 하는데, 재시작 전까지는 새 세션이 시작되지 않기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

2.1.321에서 claude remote-control에 --settings <파일> 옵션이 추가되었습니다. 이 옵션을 쓰면 원격으로 여는 모든 세션에 같은 설정 파일이 적용됩니다. 그런데 실행 중에 설정 파일이 바뀌면 claude remote-control을 다시 시작할 때까지 새 세션이 열리지 않습니다. 휴대폰으로 사무실 컴퓨터의 클로드를 부리다가 갑자기 새 세션이 안 열린다면, 최근에 설정 파일을 고치지 않았는지 먼저 확인하세요.

- 근거 policy · 처음 2026-11-10 · 최근 확인 2026-11-10 · 재검토 2026-12-10 · 검증 공식 출처

## 출처
- anthropics · 2026-11-10 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > no new session starts until you restart `claude remote-control`
