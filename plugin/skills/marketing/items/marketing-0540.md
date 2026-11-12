# robots.txt 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www가 붙은 주소와 붙지 않은 주소, http와 https 주소마다 맨 위 경로에 robots.txt를 따로 두어야 한다.

🏛 공식 발표 · 네이버 서치어드바이저 가이드 (SEO 공식)

네이버는 http://www.example.com/robots.txt의 규칙을 http://example.com이나 https://example.com에는 적용하지 않습니다. 그래서 한 주소에만 robots.txt를 고쳐 두면 다른 주소로는 의도와 다르게 수집되거나 막힐 수 있습니다. 실제로 쓰는 주소 조합마다 robots.txt가 정상으로 열리는지 확인합니다. 가장 깔끔한 방법은 대표 주소 하나를 정해 나머지 주소를 301로 보내는 것입니다. robots.txt를 고친 뒤에는 웹마스터도구의 robots.txt 도구에서 수집 요청을 눌러 네이버에 바로 알릴 수 있습니다.

- 근거 policy · 처음 2026-11-11 · 최근 확인 2026-11-11 · 재검토 2027-01-10 · 검증 공식 출처

## 출처
- NAVER Corp. (네이버 서치어드바이저) · 2026-11-11 · https://searchadvisor.naver.com/guide/seo-basic-robots
  > 같은 호스트, 프로토콜 및 포트 번호 하위의 페이지에 대해서만 유효합니다.
