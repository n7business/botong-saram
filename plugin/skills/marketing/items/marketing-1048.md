# robots.txt를 HTML 문서로 응답하면 안에 있는 규칙이 무시되고 '모두 허용'으로 처리될 수 있고, 서버 오류(5xx)로 응답하면 '모두 허용하지 않음'으로 처리되므로, robots.txt는 사이트 맨 위 경로(루트)에 일반 텍스트 파일로 두고 정상(2xx) 응답이 나오게 해야 합니다.

🏛 공식 발표 · 네이버 서치어드바이저 가이드 (SEO 공식)

robots.txt는 반드시 example.com/robots.txt처럼 루트 경로에 두고 text/plain 형식으로 응답해야 합니다. HTML로 응답하면 유효한 규칙이 있어도 robots.txt가 없는 것(모두 허용)으로 해석될 수 있습니다. 4xx 오류로 응답하면 '모두 허용', 5xx 오류로 응답하면 '모두 허용하지 않음'으로 해석됩니다. 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www.example.com의 robots.txt는 example.com이나 https 주소에 적용되지 않습니다. 파일을 고친 뒤에는 웹마스터도구의 robots.txt 도구에서 수집 요청을 누르고 검증해 보세요.

- 근거 policy · 처음 2026-11-25 · 최근 확인 2026-11-25 · 재검토 2027-01-21 · 검증 공식 출처

## 출처
- NAVER Corp. (네이버 서치어드바이저) · 2026-11-25 · https://searchadvisor.naver.com/guide/seo-basic-robots
  > '모두 허용하지 않음'으로 해석합니다.
