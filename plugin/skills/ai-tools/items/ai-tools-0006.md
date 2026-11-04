# AI 응답에 엉뚱한 외국어 문자나 명백한 구문 오류가 섞이면 사용량·시간대 탓이 아닌 인프라 버그일 수 있으므로 같은 대화를 고집하지 말고 새 대화로 재시도한다.

🏛 공식 발표 · Anthropic Engineering 블로그

2025년 8~9월 Anthropic은 세 가지 인프라 버그를 겪었다. 영어 질문에 태국어·중국어 문자가 섞이거나 코드에 뻔한 구문 오류가 나오는 출력 손상, 요청이 잘못된 서버로 가는 라우팅 오류, 컴파일러 버그였다. 라우팅은 'sticky'해서 한 번 잘못된 서버에 걸리면 그 대화의 후속 요청도 같은 서버로 갈 확률이 높았다. Anthropic은 수요·시간대·서버 부하로 모델 품질을 낮추지 않는다고 명시했다. 따라서 이상 출력이 한 대화에서 반복되면 새 대화를 열어 비교하고, 중요한 산출물은 사람이 한 번 더 검토한다.

- 근거 observed · 처음 2026-11-03 · 최근 확인 2026-11-03 · 재검토 2026-12-03 · 검증 실무자 실측(단일 출처)

## 출처
- Anthropic Engineering · 2026-11-03 · https://www.anthropic.com/research/a-postmortem-of-three-recent-issues
  > We never reduce model quality due to demand, time of day, or server load.
