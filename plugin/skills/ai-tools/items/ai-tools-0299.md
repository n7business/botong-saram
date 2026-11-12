# 새 프로젝트를 시작하면 AI에게 .gitignore부터 만들게 해야 API 키와 시크릿 키가 커밋되어 GitHub에 올라가는 일을 막을 수 있다.

👥 2명이 말함 · 레인 | AI 바이브코딩 (@Vibe_RaiN), 양실장의 바이브코딩대학 (@VibecodingUniversity)

키가 파일에 적힌 채 커밋되어 GitHub에 올라가면 다른 사람이 코드를 받을 때 키까지 받을 수 있고, 공개 레포라면 누구나 볼 수 있습니다. .gitignore는 Git이 아예 추적하지 않을 파일 목록입니다. 작업 초기에 '새 프로젝트니까 .gitignore부터 만들어줘'라고 지시해 환경 변수·보안키·민감 정보를 등록합니다. 한 번 나간 키는 되돌릴 수 없으므로 .gitignore가 만들어진 뒤에도 키 관리에 계속 유의합니다.

- 근거 consensus · 처음 2026-11-07 · 최근 확인 2026-11-07 · 재검토 2026-12-07 · 검증 독립 2곳 weight 1.4

## 출처
- 레인 | AI 바이브코딩 (@Vibe_RaiN) · 2026-11-07 · https://www.youtube.com/watch?v=wa5BtVLAcNs
  > 한 번 나간 키는 되돌릴 수가 없어요.
- 양실장의 바이브코딩대학 (@VibecodingUniversity) · 2026-11-07 · https://www.youtube.com/watch?v=D-3Iojr7dIc
  > API 키 같은 것들은 기터브 같은 공개 저장소에 그대로 올리면 안 됩니다.
