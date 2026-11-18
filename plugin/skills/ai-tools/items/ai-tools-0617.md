# API 키나 게이트웨이로 클로드 코드 auto mode를 쓰면서 무료 대상이 아니라 요금이 붙는 안전 검사로 돌아가고 있다면 지금 바로 설정을 점검해야 한다. 곧 나올 버전에서 이 대체 경로가 없어져, 검사하던 작업마다 확인을 묻거나 거부하게 되기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

auto mode는 작업마다 안전 검사(분류기)를 거치는데, 일부 API 키·게이트웨이 환경에서는 요금이 붙는 분류기 요청으로 대신 처리해 왔습니다. v2.1.327의 안내문은 다음 버전에서 이 대체 경로를 없앤다고 알리고 있습니다. 그러면 사람이 지켜보지 않는 예약 작업이나 /loop 작업은 확인을 기다리며 멈추거나 거부됩니다. /status의 Auto mode server 줄과 중간에 둔 게이트웨이·프록시 설정을 미리 확인해 두세요.

- 근거 policy · 처음 2026-11-19 · 최근 확인 2026-11-19 · 재검토 2026-12-19 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-19 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > an upcoming release removes the fallback; each action it would have checked will be asked about or denied
