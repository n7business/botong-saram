---
id: ai-tools-0061
domain: ai-tools
claim: 급여·이체·세무·정부과제 서류 같은 행정 업무를 AI 에이전트에 맡길 때는 OTP 입력·이체 실행·최종 제출·외부 발신 글은 사람 승인
  단계로 고정하고, 막히면 '조회→스크립트→브라우저→화면 조작→사람 호출' 순서로 같은 오류가 두 번 나면 다음 방법으로 넘어가게 규칙을 정한다.
status: verified
evidence: observed
confidence: 0.7
sources:
- url: https://www.gpters.org/newsletter/post/yeongeo-ulreongjeung-isseodo-gwaencanhayo-gugeul-miteu-silsigan-ai-tongyeog-4CiqevBY69LrFLe
  author: 지피터스_강지인
  seen: '2026-11-03'
  quote: 돈이 나가거나 서류를 내는 일은 사람이 하기로 먼저 정했어요.
  source: 지피터스 GPTers
first_seen: '2026-11-03'
last_confirmed: '2026-11-03'
review_by: '2026-12-03'
supersedes: null
superseded_by: null
experiment: null
law_ref: null
contributor: null
tags:
- AI에이전트
- 행정자동화
- 사람승인
- 에스컬레이션
- 슬랙
verified_by: 실무자 실측(단일 출처)
---
지피터스는 행정 담당자가 2주 비운 사이 급여·이체·월 결산·세무·정부과제 서류 등 업무 묶음 8개, 업무 50개 이상을 AI 총무 에이전트에 넘겼다. 반복 업무 38개를 쪼개면 145단계인데 사람 손이 가는 건 41단계만 남겼다. 돈이 나가거나 서류를 내는 일(OTP, 이체 실행, 최종 제출, 외부 발신 글)은 사람이 하기로 먼저 정했고, 제출도 사람이 슬랙에 '제출해'라고 댓글을 달아야 진행된다. 막혔을 때는 로그인 없이 조회→스크립트→브라우저 조작→화면 조작→사람 호출 순서로 시도하고, 같은 오류가 두 번 나면 다음 방법으로 넘어가며, 뒤쪽 방법으로 성공하면 스크립트화를 제안하게 했다. 사람에게 묻기 전에 사내 도구→기관 사이트→드라이브 순으로 찾고, 못 찾은 곳을 함께 적게 했다. 8월 18일~10월 28일 슬랙 지시 752건 중 절반을 1분 안에 처리했고, 9월 은행 거래 436건 대조에 47초가 걸렸다.
