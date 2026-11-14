# 클로드 코드 fast mode를 쓸 거라면 모델을 Opus 5.5로 두어야 가장 싸다. 100만 토큰당 입력·출력 요금이 Opus 5.5는 8·40달러인데 Opus 5·4.8은 10·50달러, Fable 5.2는 16·80달러이기 때문이다.

🏛 공식 발표 · Claude Code 릴리스 노트 (CHANGELOG)

fast mode 요금은 모델마다 다릅니다. 공식 문서 기준 100만 토큰당 입력·출력 요금은 Opus 5.5가 8·40달러로 가장 싸고, Opus 5와 Opus 4.8은 10·50달러, Fable 5.2는 16·80달러입니다. Sonnet과 Haiku는 fast mode를 지원하지 않습니다. 속도가 필요해 fast mode를 켠다면 /model로 Opus 5.5를 고르세요(v2.1.280 이상 필요). Opus 4.8의 fast mode는 2026-11-30에 없어지므로 그 전에 모델을 바꿔 두어야 합니다.

- 근거 policy · 처음 2026-11-15 · 최근 확인 2026-11-15 · 재검토 2026-12-15 · 검증 공식 출처

## 출처
- Anthropic (Claude Code Docs) · 2026-11-15 · https://code.claude.com/docs/en/fast-mode
  > \$16/\$80 on Fable 5.2, \$8/\$40 on Opus 5.5, and \$10/\$50 on Opus 5 and Opus 4.8.
