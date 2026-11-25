# 클로드 코드 업데이트를 직접 챙기기 어렵다면 Homebrew나 WinGet 말고 공식 설치 명령(네이티브 설치)으로 설치해야 한다. 네이티브 설치는 백그라운드에서 자동으로 최신 버전으로 업데이트된다.

🏛 공식 발표 · Claude Code 공식 문서

공식 문서는 네이티브 설치를 권장 방식으로 안내합니다. 맥·리눅스·WSL에서는 curl -fsSL https://claude.ai/install.sh | bash로 설치합니다. 이렇게 설치하면 백그라운드에서 저절로 업데이트되어 새 기능과 보안 수정이 따로 손대지 않아도 들어옵니다. Homebrew·WinGet으로 설치하면 자동 업데이트가 되지 않으니, 그때는 업그레이드 명령을 주기적으로 직접 실행해야 합니다.

- 근거 policy · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 2026-12-25 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-25 · https://code.claude.com/docs/en/overview
  > Native installations automatically update in the background to keep you on the latest version.
