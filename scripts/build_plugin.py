#!/usr/bin/env python3
"""④ 빌드. archive → plugin/ (Claude Code·Codex 호환 플러그인). SKILL.md는 여기서만 생성한다.

원칙: 모든 주장을 넣고 '누가·몇 명이 말했나'를 등급으로 붙인다(검증은 문턱이 아니라 표시).
  🏛 공식 발표 > 👥 N명이 말함 > 👤 한 사람이 말함 · ⚠️ 다시 확인 · ⛔ 하지 말 것
구조(점진 공개 — 스킬 호출 때 컨텍스트를 아끼려고):
  skills/<dom>/SKILL.md   규칙 + 공식·여러 명·주의·금지 한 줄 목록
  skills/<dom>/people.md  한 사람만 말한 것, 사람별 한 줄 목록
  skills/<dom>/items/<id>.md  항목 상세(본문·원문 인용·출처)
사용: build_plugin.py"""
import json, shutil
from common import *

REPO = "n7business/botong-saram"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/plugin/skills"
STALE_DAYS = 7
DISCLAIMER = "> 이 영역은 일반 정보이며 개별 사안은 노무사·세무사·변호사·행정사 등 전문가 확인이 필요합니다. 법령은 시행일 기준으로 달라질 수 있습니다.\n"

def speakers(c, idx):
    """주장한 사람(채널) 이름 목록 — 같은 사람의 영상 2개는 1명."""
    out = []
    for s in c.get("sources", []):
        src = src_lookup(s, idx) or {}
        n = s.get("source") or src.get("name") or s.get("author") or "출처"
        if n not in out: out.append(n)
    return out

def grade(c, idx):
    if c["status"] == "deprecated": return "dep", "⛔ 하지 말 것"
    if c["status"] == "stale": return "stale", "⚠️ 다시 확인 필요"
    if c["status"] == "hypothesis": return "hyp", "🧪 실험 중"
    if any((src_lookup(s, idx) or {}).get("type") == "official" for s in c.get("sources", [])): return "off", "🏛 공식 발표"
    n = len(speakers(c, idx))
    if n >= 2: return "multi", f"👥 {n}명이 말함"
    return "single", "👤 한 사람이 말함" + (" · 수치 근거" if c["status"] == "verified" else "")

def detail(c, g, ppl):
    L = [f"# {c['claim']}", "", f"{g} · {', '.join(ppl)}", "", c.get("_body", "").strip(), ""]
    meta = [f"근거 {c.get('evidence')}", f"처음 {c.get('first_seen')}", f"최근 확인 {c.get('last_confirmed')}", f"재검토 {c.get('review_by') or '—'}"]
    if c.get("law_ref") and c["law_ref"].get("law"): meta.append(f"근거 조문 {c['law_ref']['law']} {c['law_ref'].get('article','')} (시행 {c['law_ref'].get('effective') or '미확인'})")
    if c.get("verified_by"): meta.append(f"검증 {c['verified_by']}")
    if c.get("supersedes"): meta.append(f"대체: {c['supersedes']}")
    L += ["- " + " · ".join(meta), "", "## 출처"]
    if c.get("contributor"): L.append(f"- 기고: {c['contributor'].get('name')}({c['contributor'].get('license','')}) {c['contributor'].get('profile_url','')}")
    for s in c.get("sources", []):
        L.append(f"- {s.get('author') or '출처'} · {s.get('seen','')} · {s.get('url','')}")
        if s.get("quote"): L.append(f"  > {str(s['quote']).strip()}")
    return "\n".join(L) + "\n"

def line(c, g, ppl):
    return f"- {g} · {c['claim']} — {', '.join(ppl[:4])}{' 외' if len(ppl) > 4 else ''} → `items/{c['id']}.md`"

def main():
    doms = domains(); idx = source_index(); lc = state_get("lawcheck", {}); built = 0; summary = []
    if (PLUGIN / "skills").exists(): shutil.rmtree(PLUGIN / "skills")  # 지워진 항목이 남지 않게 매번 새로
    (PLUGIN / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    for dom, d in doms.items():
        cs = [c for c in claims(dom) if c["status"] != "merged"]
        if not cs: continue
        base = PLUGIN / "skills" / dom; (base / "items").mkdir(parents=True, exist_ok=True)
        groups = {k: [] for k in ("off", "multi", "single", "hyp", "stale", "dep")}
        for c in cs:
            k, g = grade(c, idx); ppl = speakers(c, idx)
            groups[k].append((c, g, ppl))
            (base / "items" / f"{c['id']}.md").write_text(detail(c, g, ppl), encoding="utf-8")
        groups["multi"].sort(key=lambda x: -len(x[2]))
        n = {k: len(v) for k, v in groups.items()}
        head = [f"---\nname: botong-{dom}\ndescription: 보통사람 {d['ko']} — 업계 사람들이 반복해서 하는 말과 공식 발표 {len(cs)}건(공식 {n['off']}·여러 명 {n['multi']}·한 사람 {n['single']}·하지 말 것 {n['dep']}). {d['ko']} 관련 질문·작업에 사용. 항목마다 누가 말했는지와 출처가 붙어 있음.\n---",
                f"# 보통사람 · {d['ko']}",
                f"빌드 {TODAY} · 항목 {len(cs)} (🏛 공식 {n['off']} / 👥 여러 명 {n['multi']} / 👤 한 사람 {n['single']} / 🧪 실험 {n['hyp']} / ⚠️ 주의 {n['stale']} / ⛔ 하지 말 것 {n['dep']})", ""]
        if d.get("legal"): head += [f"마지막 개정 확인 {lc.get('at', '미확인')}" + (" ⚠️ 확인 지연" if not lc.get("at") or (date.today() - date.fromisoformat(lc['at'])).days > 10 else ""), DISCLAIMER]
        head += ["## 최신본 확인",
                 f"이 파일의 빌드일은 {TODAY}이다. 오늘 날짜가 빌드일보다 {STALE_DAYS}일 넘게 지났고 웹을 읽을 수 있으면, 답하기 전에 최신본 `{RAW}/{dom}/SKILL.md`를 읽고 그 내용을 우선한다. 상세는 같은 경로의 `items/<id>.md`, 사람별 목록은 `people.md`. 못 읽으면 '내용이 {TODAY} 기준'이라고 밝힌다.", "",
                 "## 쓰는 법",
                 "- 이 지식은 '보통 사람들이 요즘 이렇게 한다'는 기록이다. 모두 사실 검증된 것이 아니므로 등급을 함께 말한다.",
                 "- 🏛 공식 발표는 그대로 따른다. 👥 여러 명이 말한 것은 '업계에서 보통 이렇게 한다'로, 👤 한 사람이 말한 것은 '○○는 이렇게 말한다'로 전한다.",
                 "- ⚠️·⛔ 항목에 해당하는 요청이면 먼저 경고한다. 재검토일이 지난 항목은 불확실하다고 말한다.",
                 "- 답에 쓴 항목은 `items/<id>.md`를 열어 원문 인용과 출처 링크를 같이 준다.",
                 f"- 여기 없는 주제는 `people.md`(한 사람만 말한 {n['single']}건, 사람별)를 키워드로 찾아본다.", ""]
        body = []
        for k, title in (("dep", "## ⛔ 하지 말 것"), ("stale", "## ⚠️ 다시 확인 필요 (개정·충돌·기한 경과)"), ("off", "## 🏛 공식 발표"), ("multi", "## 👥 여러 사람이 반복해서 말하는 것"), ("hyp", "## 🧪 실험 중")):
            if groups[k]: body += [title] + [line(*x) for x in groups[k]] + [""]
        if groups["single"]: body += [f"## 👤 한 사람이 말한 것 {n['single']}건 → `people.md`", ""]
        (base / "SKILL.md").write_text("\n".join(head + body), encoding="utf-8")
        by = {}
        for x in groups["single"]: by.setdefault(x[2][0] if x[2] else "출처", []).append(x)
        P = [f"# 보통사람 · {d['ko']} — 사람별 (한 사람만 말한 것)", f"빌드 {TODAY}. 다른 사람이 같은 말을 하면 SKILL.md의 '여러 사람' 목록으로 올라간다.", ""]
        for who, xs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            P += [f"## {who} ({len(xs)}건)"] + [f"- {c['claim']} → `items/{c['id']}.md`" + (" · 수치 근거" if c["status"] == "verified" else "") for c, g, ppl in xs] + [""]
        (base / "people.md").write_text("\n".join(P), encoding="utf-8")
        built += 1; summary.append(f"{d['ko']} {len(cs)}")
    # version을 비워 두면 Claude Code가 git 커밋으로 새 버전을 판단한다(하루 여러 번 빌드해도 전달됨).
    manifest = {"name": "botong-saram",
                "description": f"요즘 보통사람이라면 이 정도는 알아요 — 업계 인플루언서·실무자·공식 기관이 반복해서 하는 말을 사람별로 모은 소규모 사업자 지식(마케팅·사업화·지표·제조AX·인허가·사업계획서·AI도구·노무·세무·기본법·창업자 마인드). 누가 몇 명이 말했는지·출처 포함, 매일 갱신(빌드 {TODAY}).",
                "author": {"name": "역삼836 · 보통사람", "url": "https://yeoksam836.com"}, "homepage": "https://yeoksam836.com", "repository": f"https://github.com/{REPO}", "license": "CC-BY-4.0",
                "keywords": ["korea", "small-business", "marketing", "tax", "labor", "knowledge"]}
    (PLUGIN / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    entries = []
    for p in sorted(CHANGELOG.glob("*.json"), reverse=True)[:12]:
        lst = json.loads(p.read_text(encoding="utf-8")); kinds = {}
        for e in lst: kinds.setdefault(e["kind"], []).append(f"{e['id']}" + (f" ({e['note']})" if e.get("note") else ""))
        entries.append(f"## {p.stem}\n" + "\n".join(f"- **{k}** {len(v)}건: " + ", ".join(v[:15]) for k, v in kinds.items()))
    (PLUGIN / "CHANGELOG.md").write_text("# 보통사람 변경 이력\n\n" + "\n\n".join(entries) + "\n", encoding="utf-8")
    (PLUGIN / "README.md").write_text(f"""# 보통사람 플러그인 (빌드 {TODAY})

## Claude Code
```
/plugin marketplace add {REPO}
/plugin install botong-saram@botong-saram
```
자동 업데이트: `/plugin` → Marketplaces → botong-saram → **Enable auto-update** (한 번만). 켜 두면 세션을 열 때 새 내용을 받습니다.
수동 갱신: `/plugin marketplace update botong-saram`

## Codex
```
codex plugin marketplace add {REPO}
```
갱신: `codex plugin marketplace upgrade botong-saram`

자동 업데이트를 못 켜는 환경이어도, 스킬이 빌드일보다 {STALE_DAYS}일 넘게 지나면 GitHub 최신본을 먼저 읽도록 되어 있습니다.

영역별 항목: """ + " · ".join(summary) + "\n\n기고자 모집 → https://yeoksam836.com\n", encoding="utf-8")
    heartbeat("build", note=f"skills={built} {TODAY}")
    log(f"빌드 완료 skills={built} {TODAY}")

if __name__ == "__main__": main()
