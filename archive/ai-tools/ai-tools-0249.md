---
id: ai-tools-0249
domain: ai-tools
claim: AI에게 여러 파일의 합계 계산을 처음 맡길 때는 합계만 받지 말고 행별 포함 여부와 제외 이유를 표시한 파일을 받아 직접 만든 검산표와
  대조해야 한다.
status: verified
evidence: observed
confidence: 0.8
sources:
- url: https://www.youtube.com/watch?v=Vad-0YRVEyA
  author: 라핀
  seen: '2026-11-06'
  quote: 처음 계산을 맡길 때는 검산을 해보고 맡기기.
  source: 직장인 AI 업무 자동화 | 라핀
first_seen: '2026-11-06'
last_confirmed: '2026-11-06'
review_by: '2026-12-06'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- 챗GPT
- 엑셀
- 검산
- 데이터처리
verified_by: 실무자 실측(단일 출처)
---
요청에는 기간과 결제 상태 같은 필터, 합산 기준, 결과 표 형식, 제외한 행의 이유를 넣는다. 합계만 봐서는 어떤 주문을 넣고 뺐는지 알 수 없으므로 주문 번호, 주문 일시, 결제 상태, 결제 금액, 포함 여부, 제외 이유 열이 있는 엑셀 파일을 만들어 달라고 한다. 사례에서는 포함 28건, 제외 8건으로 나온 시트를 직접 만든 검산표와 좌우로 비교해 값과 제외 건수가 일치하는지 확인했다. 매주 같은 기준으로 반복한다면 이 절차를 스킬로 저장해 다시 쓸 수 있다.
