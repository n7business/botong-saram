---
name: botong-ai-tools
description: 보통사람 AI 도구·트렌드 — 업계 사람들이 반복해서 하는 말과 공식 발표 364건(공식 44·여러 명 11·한 사람 309·하지 말 것 0). AI 도구·트렌드 관련 질문·작업에 사용. 항목마다 누가 말했는지와 출처가 붙어 있음.
---
# 보통사람 · AI 도구·트렌드
빌드 2026-11-07 · 항목 364 (🏛 공식 44 / 👥 여러 명 11 / 👤 한 사람 309 / 🧪 실험 0 / ⚠️ 주의 0 / ⛔ 하지 말 것 0)

## 최신본 확인
이 파일의 빌드일은 2026-11-07이다. 오늘 날짜가 빌드일보다 7일 넘게 지났고 웹을 읽을 수 있으면, 답하기 전에 최신본 `https://raw.githubusercontent.com/n7business/botong-saram/main/plugin/skills/ai-tools/SKILL.md`를 읽고 그 내용을 우선한다. 상세는 같은 경로의 `items/<id>.md`, 사람별 목록은 `people.md`. 못 읽으면 '내용이 2026-11-07 기준'이라고 밝힌다.

## 쓰는 법
- 이 지식은 '보통 사람들이 요즘 이렇게 한다'는 기록이다. 모두 사실 검증된 것이 아니므로 등급을 함께 말한다.
- 🏛 공식 발표·📚 연구·저서는 그대로 따른다. 👥 여러 명이 말한 것은 '업계에서 보통 이렇게 한다'로, 👤 한 사람이 말한 것은 '○○는 이렇게 말한다'로 전한다.
- ⚠️·⛔ 항목에 해당하는 요청이면 먼저 경고한다. 재검토일이 지난 항목은 불확실하다고 말한다.
- 답에 쓴 항목은 `items/<id>.md`를 열어 원문 인용과 출처 링크를 같이 준다.
- 여기 없는 주제는 `people.md`(한 사람만 말한 309건, 사람별)를 키워드로 찾아본다.

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
- 🏛 공식 발표 · claude -p로 예약 작업을 돌린다면 claude auth status로 저장된 claude.ai 로그인의 만료일을 확인하고 표준 오류 경고까지 로그에 남겨야, 로그인 만료로 작업이 멈추기 전에 대비할 수 있다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0160.md`
- 🏛 공식 발표 · Claude Code의 /schedule로 클라우드 예약 작업을 만들 때 요청하지 않은 커넥터가 붙었다는 경고가 뜨면, 안내된 방법으로 제거해야 예약 작업이 필요 없는 외부 서비스까지 연결된 채 돌지 않는다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0161.md`
- 🏛 공식 발표 · Claude Code v2.1.318부터는 IDE 터미널에서 실행해도 IDE 확장이 자동으로 설치·업데이트되지 않으므로, 외부 터미널의 /ide나 편집기의 확장 화면에서 직접 설치·업데이트한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0162.md`
- 🏛 공식 발표 · Claude Code v2.1.318 이전 버전에서는 메시지를 보낸 직후 친 키가 권한 확인 창의 답으로 처리될 수 있으므로, 업데이트하고 그전까지는 확인 창을 읽은 뒤에 키를 누른다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0164.md`
- 🏛 공식 발표 · 코드 저장소가 없는 사람도 v2.1.318의 No repository 옵션을 고르면 Anthropic 호스팅 환경에서 저장소 선택 없이 Claude Code 클라우드 세션을 시작할 수 있다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0166.md`
- 🏛 공식 발표 · Claude Code v2.1.317 이전 버전은 검색이 시간 제한에 걸려 일부만 찾고도 전체 결과로 취급할 수 있으므로, 파일이 많은 폴더를 다룬다면 업데이트하고 '없다'는 답은 직접 확인한다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0167.md`
- 🏛 공식 발표 · AI 에이전트의 메모리에는 화면이나 시스템에서 바로 확인되는 정보를 쌓지 말고, 직접 알아낸 전략·계획·검증된 규칙만 적어야 오래된 기록을 뒤지느라 작업이 늦어지는 일을 줄일 수 있다. — Anthropic Engineering 블로그 → `items/ai-tools-0273.md`
- 🏛 공식 발표 · 최신 Claude 모델에는 메모리에 무엇을 적을지 고정 규칙을 주지 말고 메모리의 용도만 알려 줘야, 메모리로 얻는 성능 향상을 잃지 않는다. — Anthropic Engineering 블로그 → `items/ai-tools-0274.md`
- 🏛 공식 발표 · 구형 AI 모델을 쓸 때는 답하기 전에 메모리를 읽고 자기 가설을 직접 시험하라고 지시해야 메모리 효과를 제대로 얻을 수 있다. — Anthropic Engineering 블로그 → `items/ai-tools-0275.md`
- 🏛 공식 발표 · AI가 남긴 메모는 원본 대화 기록과 대조해 고쳐야, 처음부터 틀렸거나 낡은 메모를 다음 세션에서 그대로 믿고 같은 실패를 반복하는 일을 막을 수 있다. — Anthropic Engineering 블로그 → `items/ai-tools-0276.md`
- 🏛 공식 발표 · 문서로 AI 위키를 만드는 일은 여러 문서를 합쳐 답해야 하는 업무에 쓰고, 문서 하나에서 검색으로 찾을 수 있는 업무라면 검색만으로 시작하는 편이 낫다. — Anthropic Engineering 블로그 → `items/ai-tools-0277.md`
- 🏛 공식 발표 · AI 지식 위키를 만들어도 검색 도구를 없애지 말고 함께 제공해야 답변 점수가 더 높고 토큰도 절약된다. — Anthropic Engineering 블로그 → `items/ai-tools-0278.md`
- 🏛 공식 발표 · 매 세션 자동으로 불러오는 AI 메모와 지시문은 짧은 색인으로 유지하고 세부 내용은 아래 파일로 내려 링크만 남겨야, 토큰 낭비와 지시 불이행을 줄일 수 있다. — Anthropic Engineering 블로그 → `items/ai-tools-0279.md`
- 🏛 공식 발표 · AI로 계약서 지식을 정리할 때는 여러 에이전트가 표 하나에 동시에 요약하게 하지 말고 계약서마다 한 에이전트가 한 페이지에 조항을 원문 그대로 옮기게 해야 사실 누락을 줄일 수 있다. — Anthropic Engineering 블로그 → `items/ai-tools-0280.md`
- 🏛 공식 발표 · 클로드 코드를 Homebrew나 WinGet으로 설치했다면 자동 업데이트가 되지 않으므로, 업그레이드 명령을 직접 실행해야 최신 기능과 보안 수정을 받을 수 있다. — Claude Code 공식 문서 → `items/ai-tools-0281.md`
- 🏛 공식 발표 · Homebrew로 클로드 코드를 설치할 때 큰 결함이 있는 버전을 피하고 싶으면 `claude-code`를, 새 버전을 바로 받고 싶으면 `claude-code@latest`를 고른다. — Claude Code 공식 문서 → `items/ai-tools-0282.md`
- 🏛 공식 발표 · Claude Agent SDK로 만든 제품을 남에게 제공할 때는 사전 승인 없이 claude.ai 로그인이나 사용 한도를 쓰게 하면 안 되며, API 키 인증을 써야 한다. — Claude Code 공식 문서 → `items/ai-tools-0283.md`
- 🏛 공식 발표 · Claude Agent SDK로 만든 제품에는 'Claude Code'라는 이름이나 이를 흉내 낸 시각 요소를 쓰면 안 되고, 자체 브랜드를 유지해야 한다. — Claude Code 공식 문서 → `items/ai-tools-0284.md`
- 🏛 공식 발표 · 클로드 코드 예약 작업은 컴퓨터가 꺼져 있어도 돌아가야 하면 클라우드 예약으로, 내 컴퓨터의 파일과 도구가 필요하면 데스크톱 예약으로 만든다. — Claude Code 공식 문서 → `items/ai-tools-0285.md`
- 🏛 공식 발표 · 터미널 없이 클로드 코드를 쓰고 싶다면 CLI를 따로 설치할 필요 없이 유료 구독으로 데스크톱 앱의 Code 탭을 쓰면 된다. — Claude Code 공식 문서 → `items/ai-tools-0286.md`
- 🏛 공식 발표 · 저장소에 다른 코딩 에이전트용 AGENTS.md가 이미 있다면 클로드 코드가 이를 CLAUDE.md 대신 읽을 수 있으므로, 지시문을 처음부터 따로 만들지 않아도 된다. — Claude Code 공식 문서 → `items/ai-tools-0287.md`
- 🏛 공식 발표 · 클로드 코드를 설치한 뒤 `claude`를 찾을 수 없다고 나오면 다시 설치하기 전에 설치 폴더가 PATH에 들어 있는지부터 확인한다. — Claude Code 공식 문서 → `items/ai-tools-0288.md`
- 🏛 공식 발표 · 클로드 코드의 빠른 응답이 꼭 필요한 대화형 작업에만 `/fast`를 켜고, 비용이 더 중요할 때는 꺼 두어야 토큰 비용을 불필요하게 늘리지 않는다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0289.md`
- 🏛 공식 발표 · 클로드 코드 작업을 여러 개 백그라운드로 돌릴 때는 `claude agents`로 에이전트 뷰를 열어야, 대화 기록을 일일이 넘겨 보지 않고 내 입력이 필요한 세션을 바로 찾을 수 있다. — Claude Code 릴리스 노트 (CHANGELOG) → `items/ai-tools-0290.md`

## 👥 여러 사람이 반복해서 말하는 것
- 👥 3명이 말함 · Claude Code는 무료 플랜에서는 쓸 수 없으므로 월 정액 Pro 구독으로 시작하고, 내 업무 흐름에 도움이 된다고 확인되면 그때 Max로 올린다. — 짐코딩 (@gymcoding), 요즘IT, 레인 | AI 바이브코딩 (@Vibe_RaiN) → `items/ai-tools-0132.md`
- 👥 2명이 말함 · IDE 설치·프로젝트 생성·GitHub 연결 같은 개발 환경 설정에서 막히면 검색하지 말고 Claude Code에 그대로 물어보고, 오류 메시지는 복사해서 통째로 던진다. — 요즘IT, 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm) → `items/ai-tools-0035.md`
- 👥 2명이 말함 · Claude Code에 바로 '만들어 줘'라고 시키지 말고 플랜 모드(Shift+Tab 두 번)에서 탐색→계획을 먼저 받아 충분히 고친 뒤 구현시켜야, 구현 후 수정하느라 토큰이 더 드는 것을 막는다. — 짐코딩 (@gymcoding), 요즘IT → `items/ai-tools-0133.md`
- 👥 2명이 말함 · 영상 AI 모델을 고를 때는 한 플랫폼에서 한 글자도 고치지 않은 같은 프롬프트·같은 레퍼런스 사진·같은 길이와 화면 비율로 모델마다 한 번씩만 생성하되, 프롬프트의 각 부분이 검사 항목 하나(글자·제품 일관성·립싱크·물리)를 맡도록 짜고 처음 나온 결과끼리 감점표로 채점한다. — 코드깎는노인, 노마드 코더 Nomad Coders → `items/ai-tools-0137.md`
- 👥 2명이 말함 · 챗GPT 프로·비즈니스 구독자가 월 최대 500달러 상당의 API 크레딧을 받으려면 구독 7일 뒤 오픈AI 설정의 빌링(결제) 화면에서 'API 크레딧 청구하기'를 직접 눌러 신청해야 하며, 안 쓴 크레딧은 결제 주기가 끝나면 사라진다. — 지피터스 GPTers, 조코딩 JoCoding → `items/ai-tools-0159.md`
- 👥 2명이 말함 · AI에게 코드 수정을 맡기기 전과 한 작업 단위를 마칠 때마다 커밋해 두면, 일이 잘못됐을 때 원하는 시점을 골라 되돌릴 수 있다. — 레인 | AI 바이브코딩 (@Vibe_RaiN), 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm) → `items/ai-tools-0176.md`
- 👥 2명이 말함 · AI 에이전트가 만든 코드는 테스트 통과나 봇의 승인만 보고 합치지 말고, 코드를 쓰지 않은 별도 에이전트가 사용자처럼 직접 실행해 본 판정을 받아야 한다. — 요즘IT, 짐코딩 (@gymcoding) → `items/ai-tools-0203.md`
- 👥 2명이 말함 · 클로드 코드에서 위험한 명령 차단과 테스트 실행처럼 반드시 지켜야 할 규칙은 CLAUDE.md에 부탁하지 말고 퍼미션과 훅으로 강제해야 한다. — 짐코딩 (@gymcoding), 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm) → `items/ai-tools-0254.md`
- 👥 2명이 말함 · AI가 사용자 대신 잘못된 가정을 하고 불필요한 코드까지 고치는 일을 줄이려면, 지시문에 모호하면 선택지를 드러내고 문제를 고치는 줄만 바꾸라는 규칙을 적어 둔다. — 노마드 코더 Nomad Coders, 서울대 한범 교수의 AI 바이브코딩 (@ProfHanBuhm) → `items/ai-tools-0295.md`
- 👥 2명이 말함 · 새 프로젝트를 시작하면 AI에게 .gitignore부터 만들게 해야 API 키와 시크릿 키가 커밋되어 GitHub에 올라가는 일을 막을 수 있다. — 레인 | AI 바이브코딩 (@Vibe_RaiN), 양실장의 바이브코딩대학 (@VibecodingUniversity) → `items/ai-tools-0299.md`
- 👥 2명이 말함 · AI에게는 틀려도 사람이 되돌릴 수 있는 지점까지만 맡기고, 되돌리기 어려운 결정은 사람에게 남겨야 오류의 대가가 커지는 일을 막을 수 있다. — 요즘IT, 윤자동 | AI자동화로 세상을 돕는중 (@yun_ja_dong) → `items/ai-tools-0328.md`

## 👤 한 사람이 말한 것 309건 → `people.md`
