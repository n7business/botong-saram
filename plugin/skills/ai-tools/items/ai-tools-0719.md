# 맥이나 리눅스에서 Pro·Max 요금제로 클로드 코드를 쓰는데 답변에 저절로 나오는 차트가 필요 없다면 /config에서 자동 차트를 끄면 됩니다. v2.1.330부터 내장 기능 easel이 요청할 때와 MCP 지표 결과 아래에 차트를 그려 주기 때문입니다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

클로드 코드 v2.1.330에는 easel이라는 내장 모드가 추가됐습니다. 차트를 그려 달라고 하거나 MCP 도구가 지표 결과를 돌려줄 때 그 아래에 차트를 그려 줍니다. 대상은 macOS와 리눅스의 Pro·Max 요금제이고, 가능한 경우 Team·Enterprise 요금제도 포함됩니다. 매출이나 방문자 수 같은 숫자를 볼 때는 편하지만, 자동으로 나오는 차트가 거슬리면 /config에서 끌 수 있습니다.

- 근거 policy · 처음 2026-11-23 · 최근 확인 2026-11-23 · 재검토 2026-12-23 · 검증 공식 출처

## 출처
- anthropics · 2026-11-23 · https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
  > turn automatic charts off in `/config`
