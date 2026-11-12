# 클로드 코드가 사소한 결정마다 묻는 게 번거로우면 출력 스타일을 Proactive로 바꾸면 되지만, 권한 확인 창은 그대로 뜨므로 승인 기준까지 느슨해지는 것은 아니다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

Proactive 스타일에서는 작업을 받는 즉시 시작하고, 일상적인 결정은 묻지 않고 합리적으로 가정해 진행합니다. 계획을 요청하지 않으면 계획 모드로 넘어가지도 않으며, 가정이 틀리면 중간에 언제든 방향을 바꿀 수 있습니다. 데이터를 지우거나 운영 중인 시스템을 바꾸기 전에 먼저 물으라는 지시가 들어 있지만, 이는 Claude가 따르는 지시일 뿐 강제 장치는 아닙니다. 어떤 도구 실행에 확인을 받을지는 권한 모드가 그대로 정하므로, 스타일을 바꾼 뒤에도 권한 창은 직접 보고 승인하십시오. /output-style proactive로 바꿀 수 있고, 설정 파일에 직접 적을 때는 'Proactive'처럼 대소문자를 정확히 써야 합니다.

- 근거 policy · 처음 2026-11-09 · 최근 확인 2026-11-09 · 재검토 2026-12-09 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-09 · https://code.claude.com/docs/en/output-styles
  > Switching to the Proactive style doesn't change your permission mode.
