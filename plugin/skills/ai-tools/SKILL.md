---
name: botong-ai-tools
description: 보통사람 AI 도구·트렌드 — 업계 사람들이 반복해서 하는 말과 공식 발표 138건(공식 20·여러 명 4·한 사람 114·하지 말 것 0). AI 도구·트렌드 관련 질문·작업에 사용. 항목마다 누가 말했는지와 출처가 붙어 있음.
---
# 보통사람 · AI 도구·트렌드
빌드 2026-11-04 · 항목 138 (🏛 공식 20 / 👥 여러 명 4 / 👤 한 사람 114 / 🧪 실험 0 / ⚠️ 주의 0 / ⛔ 하지 말 것 0)

## 최신본 확인
이 파일의 빌드일은 2026-11-04이다. 오늘 날짜가 빌드일보다 7일 넘게 지났고 웹을 읽을 수 있으면, 답하기 전에 최신본 `https://raw.githubusercontent.com/n7business/botong-saram/main/plugin/skills/ai-tools/SKILL.md`를 읽고 그 내용을 우선한다. 상세는 같은 경로의 `items/<id>.md`, 사람별 목록은 `people.md`. 못 읽으면 '내용이 2026-11-04 기준'이라고 밝힌다.

## 쓰는 법
- 이 지식은 '보통 사람들이 요즘 이렇게 한다'는 기록이다. 모두 사실 검증된 것이 아니므로 등급을 함께 말한다.
- 🏛 공식 발표·📚 연구·저서는 그대로 따른다. 👥 여러 명이 말한 것은 '업계에서 보통 이렇게 한다'로, 👤 한 사람이 말한 것은 '○○는 이렇게 말한다'로 전한다.
- ⚠️·⛔ 항목에 해당하는 요청이면 먼저 경고한다. 재검토일이 지난 항목은 불확실하다고 말한다.
- 답에 쓴 항목은 `items/<id>.md`를 열어 원문 인용과 출처 링크를 같이 준다.
- 여기 없는 주제는 `people.md`(한 사람만 말한 114건, 사람별)를 키워드로 찾아본다.

## 🏛 공식 발표 · 📚 연구·저서
- 🏛 공식 발표 · 시스템 프롬프트나 CLAUDE.md에 '답변 N단어 이내' 같은 출력 길이 제한을 넣으면 코딩 품질이 측정 가능하게 떨어진다. — Anthropic Engineering 블로그 → `items/ai-tools-0002.md`
- 🏛 공식 발표 · AI 코드 리뷰를 시킬 때 변경 파일만 주지 말고 연관 저장소·의존 코드까지 맥락으로 주고 최신 모델을 쓰면 놓치던 버그를 잡는다. — Anthropic Engineering 블로그 → `items/ai-tools-0003.md`
- 🏛 공식 발표 · Claude Code가 갑자기 앞 내용을 잊고 반복하거나 둔해지면 모델 탓보다 먼저 CLI 버전을 v2.1.116 이상으로 올린다. — Anthropic Engineering 블로그 → `items/ai-tools-0004.md`
- 🏛 공식 발표 · AI 도구 품질 이상은 막연한 불만 대신 /feedback 명령이나 재현 가능한 구체 예시로 보고해야 실제 수정으로 이어진다. — Anthropic Engineering 블로그 → `items/ai-tools-0005.md`
- 🏛 공식 발표 · AI 응답에 엉뚱한 외국어 문자나 명백한 구문 오류가 섞이면 사용량·시간대 탓이 아닌 인프라 버그일 수 있으므로 같은 대화를 고집하지 말고 새 대화로 재시도한다. — Anthropic Engineering 블로그 → `items/ai-tools-0006.md`
- 🏛 공식 발표 · Homebrew나 WinGet으로 설치한 Claude Code는 자동 업데이트되지 않으므로 주기적으로 직접 업그레이드 명령을 실행해야 최신 기능과 보안 패치를 받는다. — Claude Code 공식 문서 → `items/ai-tools-0007.md`
- 🏛 공식 발표 · Claude Code를 안정적으로 쓰려면 Homebrew의 stable 채널(claude-code)을 설치하고, 신기능을 바로 쓰려면 latest 채널(claude-code@latest)을 설치한다. — Claude Code 공식 문서 → `items/ai-tools-0008.md`
- 🏛 공식 발표 · CLAUDE.md는 200줄 이내로 유지하고, 가끔만 필요한 참고 자료는 스킬이나 .claude/rules/ 파일로 분리한다. — Claude Code 공식 문서 → `items/ai-tools-0009.md`
- 🏛 공식 발표 · Claude Code가 같은 규칙이나 명령을 두 번 틀리면 채팅에서 매번 고쳐주지 말고 CLAUDE.md에 그 규칙을 적는다. — Claude Code 공식 문서 → `items/ai-tools-0010.md`
- 🏛 공식 발표 · 파일을 수십 개 읽는 조사 작업이나 컨텍스트가 차오를 때는 메인 대화에서 직접 시키지 말고 서브에이전트로 보내 요약만 받는다. — Claude Code 공식 문서 → `items/ai-tools-0011.md`
- 🏛 공식 발표 · CLAUDE.md나 출력 스타일에 적은 지시는 강제되지 않으므로, 매번 반드시 실행돼야 하는 일(포맷터·린트 등)은 훅(hook)으로 건다. — Claude Code 공식 문서 → `items/ai-tools-0012.md`
- 🏛 공식 발표 · Claude Code 추론 강도는 한 단계에 고정하지 말고 구현·기계적 편집은 낮음, 검증·버그 수정은 높음으로 작업 단계마다 바꾸고, 강도를 올리기 전에 모델이 스스로 검사할 수단(테스트·빌드 스크립트)부터 준다. — 요즘IT, Anthropic Engineering 블로그 → `items/ai-tools-0015.md`
- 🏛 공식 발표 · Opus 4.8의 빠른 모드(fast mode)는 2026-10-30 지원 중단, 2026-11-30 제거되며 제거 후엔 일반 Opus 4.8로 대체되지 않고 오류만 나므로 그 전에 Opus 5.5로 옮긴다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0019.md`
- 🏛 공식 발표 · Claude Code가 작업 폴더 밖 파일을 건드리는 사고를 막으려면 settings.json에 permissions.blockWritesOutsideWorkingDirectories를 켜서 모든 권한 모드에서 외부 경로 쓰기를 차단한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0020.md`
- 🏛 공식 발표 · 스크립트에서 claude -p의 종료 코드로 성공 여부를 판단하려면 Claude Code를 2.1.314 이상(디스크 꽉 참 감지는 2.1.317 이상)으로 올려야 하며, 그 이전 버전은 시작 실패나 저장 실패 시에도 0을 반환한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0021.md`
- 🏛 공식 발표 · 프롬프트에 'ultrathink'라는 단어가 들어가면 그 턴이 가장 높은 추론 강도(xhigh)로 실행돼 시간과 비용이 늘어나므로, 붙여넣은 글 등에서 의도치 않게 켜지는 걸 막으려면 CLAUDE_CODE_DISABLE_ULTRATHINK=1로 끈다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0022.md`
- 🏛 공식 발표 · 서브에이전트가 메인 세션의 높은 추론 강도를 그대로 물려받아 비용이 새는 걸 막으려면 CLAUDE_CODE_SUBAGENT_EFFORT로 서브에이전트 기본 강도를 따로 낮게 지정한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0023.md`
- 🏛 공식 발표 · Claude Code 2.1.317부터 웹·셸 도구가 계정 이메일을 외부로 보내려 하면 확인을 묻는데, 직접 의도한 경우가 아니면 거절해야 이메일이 User-Agent나 요청 본문에 실려 외부 서비스에 남는 걸 막는다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0024.md`
- 🏛 공식 발표 · 2.1.317 이전 Claude Code에서는 입력창의 글자를 지우려고 Ctrl+C를 누르면 돌고 있던 백그라운드 에이전트가 전부 중단되므로, 구버전에서는 Ctrl+C 대신 다른 방법으로 입력을 지우거나 업데이트한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0025.md`
- 🏛 공식 발표 · 맥·리눅스에서 Claude Code를 무인으로 돌리는 환경(launchd·cron·클라우드 세션)은 2.1.316 이상으로 올려야 하며, 그 이전 버전은 인증 거부 등으로 스스로 종료될 때 실행 중이던 셸 명령을 남겨 둬 좀비 프로세스가 쌓일 수 있다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0026.md`

## 👥 여러 사람이 반복해서 말하는 것
- 👥 3명이 말함 · Claude Code는 무료 플랜에서는 쓸 수 없으므로 월 정액 Pro 구독으로 시작하고, 내 업무 흐름에 도움이 된다고 확인되면 그때 Max로 올린다. — 짐코딩 (@gymcoding), 요즘IT, 레인 | AI 바이브코딩 (@Vibe_RaiN) → `items/ai-tools-0132.md`
- 👥 2명이 말함 · IDE 설치·프로젝트 생성·GitHub 연결 같은 개발 환경 설정에서 막히면 검색하지 말고 Claude Code에 그대로 물어보고, 오류 메시지는 복사해서 통째로 던진다. — 요즘IT, 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm) → `items/ai-tools-0035.md`
- 👥 2명이 말함 · Claude Code에 바로 '만들어 줘'라고 시키지 말고 플랜 모드(Shift+Tab 두 번)에서 탐색→계획을 먼저 받아 충분히 고친 뒤 구현시켜야, 구현 후 수정하느라 토큰이 더 드는 것을 막는다. — 짐코딩 (@gymcoding), 요즘IT → `items/ai-tools-0133.md`
- 👥 2명이 말함 · 영상 AI 모델을 고를 때는 한 플랫폼에서 한 글자도 고치지 않은 같은 프롬프트·같은 레퍼런스 사진·같은 길이와 화면 비율로 모델마다 한 번씩만 생성하되, 프롬프트의 각 부분이 검사 항목 하나(글자·제품 일관성·립싱크·물리)를 맡도록 짜고 처음 나온 결과끼리 감점표로 채점한다. — 코드깎는노인, 노마드 코더 Nomad Coders → `items/ai-tools-0137.md`

## 👤 한 사람이 말한 것 114건 → `people.md`
