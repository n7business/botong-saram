# 클로드 코드에서 프롬프트 캐시를 1시간으로 늘리는 ENABLE_PROMPT_CACHING_1H=1은 캐시 쓰기 요금이 더 비싸므로, 작업 사이 공백이 5분을 자주 넘길 때만 켜야 한다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

클로드 코드는 프롬프트 캐싱을 자동으로 켜고 기본 유지 시간은 5분입니다. ENABLE_PROMPT_CACHING_1H=1로 1시간 캐시를 요청할 수 있지만, 1시간짜리 캐시 쓰기는 더 높은 요율로 청구됩니다. 대화를 쉬지 않고 이어 가는 작업이라면 5분 캐시로 충분하고 1시간 설정은 비용만 늘릴 수 있습니다. 메인 대화와 그 밖의 요청에 유지 시간을 따로 정하는 설정도 있으니 프롬프트 캐싱 문서를 함께 확인하세요.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2026-12-11 · 검증 공식 출처

## 출처
- Anthropic · 2026-11-11 · https://code.claude.com/docs/en/azure-ai-foundry
  > cache writes with a 1-hour TTL are billed at a higher rate
