# 보통사람 (botong-saram)

살아있는 지식 아카이브 → Claude Code 플러그인. 설계는 `docs/vision.md`가 정본.

## 구조
- `sources/sources.yaml` 추적 계정 목록 · `inbox/` 수집 원문(gitignore) · `archive/<영역>/<id>.md` 지식 항목(frontmatter 스키마는 vision.md) · `plugin/` 빌드 산출물.
- 흐름은 한 방향: sources → inbox → archive(candidate) → 검증 → archive(verified) → plugin. SKILL.md 직접 편집 금지.

## 규칙
- 검증은 문턱이 아니라 등급: 플러그인엔 merged 뺀 모든 주장을 🏛 공식 / 👥 N명 / 👤 한 사람 / ⚠️ / ⛔ 로 표시해 넣는다(11/4 결정). verified는 '수치·교차 확인됨' 표시일 뿐 포함 조건 아님.
- 단일 출처 항목은 verified 불가(비법률 수치 실측 예외). deprecated 항목은 삭제하지 않고 "하지 말 것"으로 플러그인에 남긴다.
- 배포 대상 사이트는 **역삼836(yeoksam836.com, ~/gh/n7business/Yeoksam836)**. 상단 메뉴 「보통사람」.
- 수집기는 맥미니 launchd + `aside exec`(프로필 u0). 크레덴셜은 `~/.config/envs/` 경로 참조만.

## 운영 (11/4~)
- 공개 저장소 https://github.com/n7business/botong-saram . 맥미니(`ssh macmini`, ~/gh/n7business/botong-saram)가 매일 06:30 수집·빌드 후 **push**한다 → 맥북에서 고치기 전 반드시 `git pull`.
- 플러그인 version은 비워 둔다(커밋 기준 자동 업데이트). 각 SKILL.md에 '7일 지나면 raw GitHub 최신본 읽기' 문구가 들어간다.
- 맥미니 state/·inbox/는 gitignore라 맥미니에만 있다. 맥북에서 수동 수집한 날은 rsync로 맞춘다.
