# claude -p로 결과를 파일에 저장하는 자동 작업을 돌린다면 v2.1.330 이상으로 업데이트해야 한다. 이전 버전에서는 디스크가 가득 차 저장에 실패해도 아무 메시지 없이 성공(종료 코드 0)으로 끝나 실패를 알아챌 수 없었기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

이전 버전의 claude -p는 출력 파일을 저장하는 디스크가 가득 차도 오류 없이 종료 코드 0으로 끝났다. 그래서 스크립트나 예약 실행은 결과 파일이 비었거나 잘렸는데도 성공한 것으로 기록했다. v2.1.330부터는 오류를 출력하고 종료 코드 1로 끝난다. 다만 가득 찬 NFS 네트워크 저장소는 여전히 놓칠 수 있으므로, 중요한 자동 작업은 결과 파일 크기나 내용을 따로 검사하는 단계를 두는 게 좋다.

- 근거 policy · 처음 2026-11-21 · 최근 확인 2026-11-21 · 재검토 2026-12-21 · 검증 공식 출처

## 출처
- anthropics (Anthropic) · 2026-11-21 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > it now prints an error and exits 1, though a full NFS export may go unnoticed
