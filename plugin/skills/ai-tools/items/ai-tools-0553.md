# 클로드 코드 설정 파일에 outputStyle을 적을 때는 Concise·Explanatory처럼 대소문자를 정확히 맞춰야 하는데, explanatory처럼 이름이 정확히 맞지 않으면 오류 없이 기본(Default) 스타일로 실행되기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

출력 스타일을 매번 /output-style로 고르지 않고 늘 쓰려면 ~/.claude/settings.json에 outputStyle을 적어 둡니다. 이 값은 대소문자를 구분하므로 기본 제공 스타일은 Proactive, Concise, Explanatory, Learning처럼 첫 글자를 대문자로 적어야 합니다. 이름이 정확히 맞지 않으면 별다른 경고 없이 Default 스타일이 적용됩니다. 반면 /output-style 명령은 대소문자를 가리지 않습니다. 프로젝트 설정 파일에 다른 값이 있으면 그쪽이 사용자 설정보다 우선합니다.

- 근거 policy · 처음 2026-11-14 · 최근 확인 2026-11-14 · 재검토 2026-12-14 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-14 · https://code.claude.com/docs/en/output-styles
  > A value that doesn't match a style name exactly, such as `explanatory`, gives you the Default style.
