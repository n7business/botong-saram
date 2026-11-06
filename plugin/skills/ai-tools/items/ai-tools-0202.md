# Postman 같은 도구로 API를 직접 테스트하다 잘 안 되면 Host·Accept·Content-Type 요청 헤더가 제대로 설정됐는지 확인한다.

👤 한 사람이 말함 · 양실장의 바이브코딩대학 (@VibecodingUniversity)

요청 헤더는 많지만 알아 두면 도움이 되는 것은 세 개입니다. Host는 요청 대상, Accept는 내가 이해할 수 있는 응답 형태, Content-Type은 내가 보내는 데이터의 형태이며 API 호출에서는 보통 application/json을 씁니다. 응답의 Content-Type이 요청의 Accept와 맞아야 잘 동작합니다. 바이브 코딩을 할 때는 AI가 대개 알아서 맞춰 주므로, 직접 테스트할 때 점검 항목으로 쓰면 됩니다.

- 근거 consensus · 처음 2026-11-06 · 최근 확인 2026-11-06 · 재검토 —

## 출처
- 양실장 (양실장의 바이브코딩대학) · 2026-11-06 · https://www.youtube.com/watch?v=bBXtm7_9F4U
  > 헤더를 제대로 설정하지 않으면 잘 안 되는 경우가 있어서
