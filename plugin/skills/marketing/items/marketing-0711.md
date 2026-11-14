# robots.txt 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www 주소에 둔 robots.txt는 www 없는 주소나 https 주소에는 적용되지 않는다는 점을 알고 주소마다 따로 확인해야 합니다.

🏛 공식 발표 · 네이버 서치어드바이저 가이드 (SEO 공식)

http://www.example.com/robots.txt의 내용은 http://example.com/과 https://example.com/에는 적용되지 않습니다. 홈페이지를 www 있는 주소와 없는 주소, http와 https로 함께 열어 두었다면 주소마다 robots.txt가 의도대로 들어 있는지 확인해야 합니다. 가장 깔끔한 방법은 대표 주소 하나만 남기고 나머지는 301로 이동시키는 것입니다. robots.txt를 고친 뒤에는 웹마스터도구 robots.txt 도구에서 수집 요청을 눌러 네이버에 바로 알릴 수 있습니다.

- 근거 policy · 처음 2026-11-15 · 최근 확인 2026-11-15 · 재검토 2027-01-14 · 검증 공식 출처

## 출처
- NAVER Corp. (네이버 서치어드바이저) · 2026-11-15 · https://searchadvisor.naver.com/guide/seo-basic-robots
  > robots.txt 파일에 작성된 규칙은 같은 호스트, 프로토콜 및 포트 번호 하위의 페이지에 대해서만 유효합니다.
