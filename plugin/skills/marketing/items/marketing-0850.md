# 같은 내용을 여러 주소로 보여 줘야 하는데 대표 주소로 301 redirect하기 어렵다면, 각 페이지 HTML에 <link rel="canonical">로 대표 주소를 적어 네이버 검색에 대표 URL로 나오게 해야 합니다.

🏛 공식 발표 · 네이버 서치어드바이저 가이드 (SEO 공식)

네이버는 같은 내용을 여러 주소로 보여 줄 때 대표 주소로 301 redirect하라고 권장합니다. www가 있는 주소와 없는 주소도 둘 중 하나로 정해 redirect해야 합니다. 쇼핑몰 플랫폼이나 호스팅 제약으로 redirect가 어렵다면 <link rel="canonical" href="대표주소">를 넣으세요. 그러면 검색 결과에 중복 없이 대표 URL이 나올 가능성이 커집니다. 도메인을 옮길 때도 새 사이트의 모든 페이지에 canonical을 지정해야 검색 노출 주소가 옛 도메인으로 남지 않습니다.

- 근거 policy · 처음 2026-11-20 · 최근 확인 2026-11-20 · 재검토 2027-01-19 · 검증 공식 출처

## 출처
- 네이버 서치어드바이저 · 2026-11-20 · https://searchadvisor.naver.com/guide/seo-basic-create
  > 대표 주소로 301 redirect 가 어렵다면 HTML 마크업 시 rel="canonical" 으로 대표 주소를 기입해주세요.
