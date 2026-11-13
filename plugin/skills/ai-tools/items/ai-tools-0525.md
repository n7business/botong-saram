# 내 컴퓨터에 설치한 클로드 코드 플러그인은 claude.ai/code 같은 클라우드 세션에서 불러오지 않으므로, 웹에서도 같은 플러그인을 쓰려면 클라우드 세션 쪽에 따로 설정해야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

사용자 범위로 설치한 플러그인은 같은 컴퓨터의 터미널, 데스크톱 앱 로컬 세션, VS Code 확장에서 함께 쓸 수 있습니다. 세 곳이 같은 설정 파일을 읽기 때문입니다. 하지만 브라우저의 claude.ai/code를 포함한 클라우드 세션은 로컬 설정의 플러그인을 불러오지 않습니다. 사무실 컴퓨터에서 잘 되던 스킬이 웹 세션에서 보이지 않으면 이 때문이니, 공식 문서의 Install a plugin 안내에 따라 클라우드 세션이 무엇을 불러오는지 확인하세요. 팀원 모두가 써야 하는 플러그인은 프로젝트 범위로 .claude/settings.json에 넣어도, 각자 자기 컴퓨터에 설치해야 합니다.

- 근거 policy · 처음 2026-11-13 · 최근 확인 2026-11-13 · 재검토 2026-12-13 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-13 · https://code.claude.com/docs/en/plugins
  > A cloud session, including one in the browser at claude.ai/code, doesn't load the plugins in your local settings.
