#!/usr/bin/env python3
"""① 수집. sources.yaml의 소스를 돌며 inbox/<날짜>/에 원문 저장.
official·blog·newsletter → HTTP, SNS(threads·instagram·youtube·x) → aside exec.
사용: collect.py [--domain marketing] [--only 이름부분] [--no-aside] [--dry]"""
import argparse, json, os, re, subprocess, sys
from common import *

SNS = {"threads", "instagram", "youtube", "x"}
ASIDE_PROMPT = """다음 페이지를 열어 최근 7일 안에 올라온 게시물을 최대 {n}개 모으고, 다른 말 없이 JSON 배열만 출력하세요.
URL: {url}
- SNS 프로필이면 답글 탭이 아닌 게시물(스레드) 탭에서 화면을 여러 번 아래로 스크롤하며 모읍니다. 처음 보이는 2~3개에서 멈추지 마세요. 7일보다 오래된 글이 나오거나 {n}개를 채우면 멈춥니다.
- 같은 사람이 이어 쓴 스레드 체인(본문-댓글1-댓글2)은 게시물을 열어 이어진 본문까지 합쳐 하나의 text로 적습니다.
- 목록 페이지(블로그·게시판)면 각 글을 열어 본문까지 읽습니다.
형식: [{{"url": "게시물 고유 URL", "author": "작성자 핸들", "date": "YYYY-MM-DD", "text": "본문 전체"}}]
게시물이 없으면 []. 로그인·팔로우·좋아요 등 어떤 상호작용도 하지 마세요. 읽기만."""

ANSI = re.compile(r"\x1b\[[0-9;]*m")
def last_json_array(out):
    """Aside 출력(ANSI·로그 섞임)에서 마지막으로 파싱되는 JSON 배열을 찾는다."""
    txt = ANSI.sub("", out); dec = json.JSONDecoder()
    for i in range(len(txt) - 1, -1, -1):
        if txt[i] != "[": continue
        try:
            v, _ = dec.raw_decode(txt[i:])
            if isinstance(v, list) and (not v or isinstance(v[0], dict)): return v
        except json.JSONDecodeError: continue
    return []

def merge_state(name, upd):
    cur = state_get(name); cur.update(upd); state_set(name, cur)

def slug(s): return re.sub(r"[^a-z0-9가-힣]+", "-", s.lower()).strip("-")[:60]

def fetch_http(src, seen_links):
    """목록 페이지를 읽고, 같은 호스트의 새 글 링크를 follow(기본 5)개까지 따라가 개별 글 본문을 모은다."""
    import urllib.parse
    html = http_get(src["url"]); text, links = html_to_text(html)
    host = urllib.parse.urlparse(src["url"]).netloc; items = []; n = int(src.get("follow", 5))
    pat = re.compile(src["link_pattern"]) if src.get("link_pattern") else None
    for href, title in links:
        if len(items) >= n: break
        u = urllib.parse.urljoin(src["url"], href)
        if urllib.parse.urlparse(u).netloc != host or u == src["url"] or len(title) < 8: continue
        if pat and not pat.search(u): continue
        if not pat and not re.search(r"(view|detail|read|Ntt|article|post|\d{4,})", u, re.I): continue
        if re.search(r"(users\?|/tag/|/category/|login|signup|#)", u, re.I): continue
        if u in seen_links: continue
        try:
            t, _ = html_to_text(http_get(u)); items.append({"url": u, "title": title, "text": t[:12000]}); seen_links[u] = TODAY
        except Exception as e: log(f"  링크 실패 {u}: {e}")
    body = "\n\n".join(f"### {i['title']}\nURL: {i['url']}\n{i['text']}" for i in items)
    return {"text": body or text[:30000], "items": items, "links": links[:100]}

PAGE_PROMPT = """다음 페이지를 열어 본문을 읽고, 하위 안내 문서 링크가 있으면 최대 {n}개까지 열어 본문도 읽으세요. 다른 말 없이 JSON 배열만 출력하세요.
URL: {url}
형식: [{{"url": "문서 URL", "author": "발행 주체", "date": "문서에 표시된 날짜 또는 오늘", "text": "본문 전체(요약하지 말 것)"}}]
로그인·클릭 외 상호작용 금지. 읽기만."""

YT = os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp")
YT_PROMPT = """유튜브 영상 {url} 을 열고 (설명란 더보기 → "스크립트 표시"로 자막을 읽거나, 자막이 없으면 영상 내용을 끝까지 확인) 화자가 말하는 **실행 가능한 노하우·주장을 빠짐없이** 정리하세요. 재생 외 좋아요·구독·댓글 등 상호작용 금지.
다른 말 없이 JSON만: {{"url": "{url}", "title": "제목", "date": "업로드일 YYYY-MM-DD", "text": "화자의 주장을 순서대로 모두 쓴 본문(요약하지 말고 주장마다 2~3문장, 수치·조건·예외 포함)", "quotes": ["화자가 실제로 말한 문장 그대로 5개(각 50자 이내)"]}}"""

def fetch_youtube(src, seen_links, n=2):
    """채널 최신 영상 n개: yt-dlp로 목록 → 영상별 Aside 읽기(자막 기반 주장 정리 + 원문 인용)."""
    url = src["url"].rstrip("/"); listing = url if "/videos" in url else url + "/videos"
    r = subprocess.run([YT, "--flat-playlist", "--playlist-end", str(n * 3), "--print", "%(id)s|%(title)s", "--extractor-args", "youtube:lang=ko", listing], capture_output=True, text=True, timeout=120)
    vids = [l.split("|", 1) for l in r.stdout.strip().split("\n") if "|" in l]
    posts = []
    for vid, title in vids:
        vurl = f"https://www.youtube.com/watch?v={vid}"
        if vurl in seen_links: continue
        if len(posts) >= n: break
        rr = subprocess.run(["aside", "exec", "--account", "u0", "--effort", "low", YT_PROMPT.format(url=vurl)], capture_output=True, text=True, timeout=600)
        txt = ANSI.sub("", rr.stdout); i = txt.rfind('{"url"')
        try: d, _ = json.JSONDecoder().raw_decode(txt[i:]) if i >= 0 else (None, 0)
        except json.JSONDecodeError: d = None
        if not d or not d.get("text"): log(f"  영상 읽기 실패 {vid}"); seen_links[vurl] = TODAY; continue
        d["url"] = vurl; d.setdefault("title", title); d["author"] = src.get("author", src["name"]); posts.append(d); seen_links[vurl] = TODAY
        log(f"  영상 {vid} {len(d['text'])}자 인용 {len(d.get('quotes', []))}")
    text = "\n\n".join(f"### {p['title']}\nURL: {p['url']} ({p.get('date')})\n{p['text']}\n인용: " + " / ".join(f'"{q}"' for q in p.get("quotes", [])) for p in posts)
    return {"posts": posts, "text": text}

def fetch_aside(src, n=15, days=7):
    prompt = (PAGE_PROMPT if src.get("mode") == "page" else ASIDE_PROMPT.replace("최근 7일", f"최근 {days}일")).format(url=src["url"], n=n if src.get("mode") != "page" else int(src.get("follow", 6)))
    cmd = ["aside", "exec", "--account", "u0", "--effort", "low", prompt]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if r.returncode != 0: raise RuntimeError(f"aside rc={r.returncode}: {r.stderr[-500:]}")
    posts = last_json_array(r.stdout)
    return {"posts": posts, "text": "\n\n".join(f"[{p.get('date')}] {p.get('author')} {p.get('url')}\n{p.get('text')}" for p in posts)}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--domain"); ap.add_argument("--only"); ap.add_argument("--no-aside", action="store_true"); ap.add_argument("--dry", action="store_true"); ap.add_argument("--days", type=int, default=7, help="SNS 최근 n일"); ap.add_argument("--videos", type=int, default=2, help="유튜브 채널당 영상 수")
    a = ap.parse_args()
    doms = domains(); seen = state_get("collect_seen"); seen_links = state_get("collect_links"); out_dir = INBOX / TODAY; out_dir.mkdir(parents=True, exist_ok=True)
    n_ok = n_skip = n_err = 0
    for dom, lst in sources().items():
        if a.domain and dom != a.domain: continue
        for src in lst or []:
            if a.only and a.only not in src.get("name", ""): continue
            if doms.get(dom, {}).get("legal") and src.get("type") != "official" and (not src.get("license") or src.get("license_unverified")):
                log(f"건너뜀(자격 미확인) {dom}/{src['name']}"); n_skip += 1; continue
            if src.get("unverified"): log(f"건너뜀(URL 미확인) {dom}/{src['name']}"); n_skip += 1; continue
            if a.dry: log(f"[dry] {dom}/{src['name']} {src['type']} {src['url']}"); continue
            try:
                if src.get("type") in SNS:
                    if a.no_aside: n_skip += 1; continue
                    data = fetch_youtube(src, seen_links, n=a.videos) if src.get("type") == "youtube" else fetch_aside(src, n=15, days=a.days)
                else:
                    via_aside = False
                    try: data = fetch_http(src, seen_links)
                    except Exception as e:
                        if a.no_aside: raise
                        log(f"HTTP 실패({str(e)[:60]}) → aside 폴백 {dom}/{src['name']}"); data = fetch_aside(src); via_aside = True
                    if not via_aside and len(data.get("text", "")) < 600 or (src.get("follow", 5) and not data.get("items") and src.get("type") == "official"):
                        if a.no_aside: log(f"JS 페이지, aside 필요 {dom}/{src['name']}"); n_skip += 1; continue
                        log(f"HTTP 본문 부족 → aside 폴백 {dom}/{src['name']}"); data = fetch_aside(src)
                h = sha(data.get("text", ""))
                key = f"{dom}/{src['name']}"
                if seen.get(key) == h: log(f"변경 없음 {key}"); n_skip += 1; continue
                rec = {"domain": dom, "source": src, "fetched_at": datetime.now().isoformat(timespec="seconds"), **data}
                (out_dir / f"{dom}__{slug(src['name'])}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
                seen[key] = h; n_ok += 1; log(f"저장 {key} ({len(data.get('text',''))}자)")
                merge_state("collect_seen", {key: h}); merge_state("collect_links", seen_links)  # 영역별 병렬 실행 시 덮어쓰기 방지
            except Exception as e:
                n_err += 1; log(f"실패 {dom}/{src['name']}: {e}")
    merge_state("collect_seen", seen); merge_state("collect_links", seen_links)
    heartbeat("collect", ok=n_err == 0, note=f"ok={n_ok} skip={n_skip} err={n_err}")
    log(f"수집 완료 ok={n_ok} skip={n_skip} err={n_err}")

if __name__ == "__main__": main()
