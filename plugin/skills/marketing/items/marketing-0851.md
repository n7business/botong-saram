# robots.txt 규칙은 같은 호스트·프로토콜·포트에만 적용되므로, www가 붙은 주소의 robots.txt는 www 없는 주소나 https 주소에는 적용되지 않는다는 점을 알고 주소마다 따로 설정해야 합니다.

🏛 공식 발표 · 네이버 서치어드바이저 가이드 (SEO 공식)

http://www.example.com/robots.txt에 적은 규칙은 http://example.com/이나 https://example.com/에는 적용되지 않습니다. 그래서 한쪽에만 차단이나 허용 규칙을 걸면 다른 주소에서는 의도와 다르게 수집될 수 있습니다. robots.txt 파일이 없거나 4xx로 응답하면 네이버는 모든 페이지를 수집해도 되는 것으로 봅니다. 수정한 뒤에는 웹마스터도구 robots.txt 도구에서 수집 요청을 누르고, 페이지별 수집 가능 여부도 테스트해 보세요.

- 근거 policy · 처음 2026-11-20 · 최근 확인 2026-11-20 · 재검토 2027-01-19 · 검증 공식 출처

## 출처
- 네이버 서치어드바이저 · 2026-11-20 · https://searchadvisor.naver.com/guide/seo-basic-robots
  > http://www.example.com/robots.txt의 내용은 http://example.com/ 와 https://example.com/에는 적용되지 않습니다.
