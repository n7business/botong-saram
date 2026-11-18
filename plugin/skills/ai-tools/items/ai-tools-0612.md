# AI가 만든 앱이나 업무 화면은 코드·스크린샷·시안과 같은 겉모습만 보고 완성으로 판단하지 말고, 직접 또는 Playwright 같은 도구로 실제 화면을 사용자처럼 눌러 저장·확인창·등록 요청 같은 핵심 기능이 제대로 동작하는지 확인해야 한다.

🏛 공식 발표 · Anthropic Engineering 블로그, 요즘IT

앤트로픽 실험에서 에이전트 하나가 20분 동안 만든 게임 제작 앱은 처음 화면은 그럴듯했습니다. 그런데 실제 게임 모드에서는 캐릭터가 입력에 전혀 반응하지 않았습니다. 그래서 검토용 AI에게 Playwright MCP를 주어 실행 중인 앱을 사용자처럼 클릭하며 화면 기능·API·DB 상태를 확인하게 했습니다. 그러자 '드래그해도 영역이 채워지지 않는다', '삭제 키가 동작하지 않는다'처럼 바로 고칠 수 있는 구체적인 버그를 찾아냈습니다.

- 근거 observed · 처음 2026-11-19 · 최근 확인 2026-11-19 · 재검토 2026-12-19 · 검증 독립 2곳 weight 1.6

## 출처
- Anthropic · 2026-11-19 · https://www.anthropic.com/research/harness-design-long-running-apps
  > Applications from earlier harnesses often looked impressive but still had real bugs when you actually tried to use them.
- 김의중 · 2026-11-17 · https://yozm.wishket.com/magazine/detail/4040/
  > 저장 버튼을 눌러 보면 아무 일도 일어나지 않고, 떠야 할 확인창도 나가야 할 등록 요청도 없습니다.
