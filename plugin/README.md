# 보통사람 플러그인 (빌드 2026-11-13)

## Claude Code
```
/plugin marketplace add n7business/botong-saram
/plugin install botong-saram@botong-saram
```
자동 업데이트: `/plugin` → Marketplaces → botong-saram → **Enable auto-update** (한 번만). 켜 두면 세션을 열 때 새 내용을 받습니다.
수동 갱신: `/plugin marketplace update botong-saram`

## Codex
```
codex plugin marketplace add n7business/botong-saram
```
갱신: `codex plugin marketplace upgrade botong-saram`

자동 업데이트를 못 켜는 환경이어도, 스킬이 빌드일보다 7일 넘게 지나면 GitHub 최신본을 먼저 읽도록 되어 있습니다.

## 이 플러그인이 하는 일
- 영역별 스킬 11개(마크다운 파일)만 들어 있습니다. 훅·MCP 서버·실행 스크립트가 없고, 어떤 정보도 밖으로 보내지 않습니다.
- Claude가 질문에 맞는 스킬을 열어 SKILL.md·all.md·people.md·items/<id>.md를 읽고, 항목마다 붙은 등급(🏛 공식·👥 여러 명·👤 한 사람·⚠️·⛔)과 원문 출처를 함께 답합니다.
- 빌드일이 7일 넘게 지났고 웹을 읽을 수 있으면 `https://raw.githubusercontent.com/n7business/botong-saram/main/plugin/skills/<영역>/SKILL.md` 최신본을 읽도록 안내합니다(읽기만 함).
- 스킬이 안 열리면 질문에 "보통사람 기준으로"를 붙이세요. 다른 플러그인이 아주 많으면 Claude가 스킬을 못 고를 수 있습니다.

영역별 항목: 마케팅·홍보·디자인 590 · 사업화·매출 증대 316 · 매출·경영 지표 164 · 생산·현장 AX 153 · 행정·인허가 152 · 사업계획서·정부지원 402 · AI 도구·트렌드 498 · 인사·노무 163 · 세무 196 · 기본법 262 · 창업자 마인드·습관 165

기고자 모집 → https://yeoksam836.com

## 원작자 삭제 요청
보통사람에 내 글이나 계정이 실려 있는데 빼고 싶으시면 계정 주소만 알려 주세요. 확인 후 바로 수집 대상에서 빼고 관련 항목을 모두 지웁니다.
- 이메일: founder@yeoksam836.com
- GitHub 이슈: https://github.com/n7business/botong-saram/issues/new?template=takedown.md

보통사람은 원문 일부를 출처 링크와 함께 짧게 인용합니다. CC-BY-4.0은 보통사람이 쓴 정리·구성에만 적용되며, 인용된 원문의 권리는 원작자에게 있습니다.
