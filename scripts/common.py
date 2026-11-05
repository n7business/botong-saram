"""보통사람 파이프라인 공통 모듈. 표준 라이브러리 + pyyaml."""
import json, os, re, subprocess, sys, hashlib, urllib.request, urllib.parse, urllib.error
from datetime import date, datetime, timedelta
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources" / "sources.yaml"
DOMAINS = ROOT / "sources" / "domains.yaml"
ARCHIVE = ROOT / "archive"
INBOX = ROOT / "inbox"
STATE = ROOT / "state"
CHANGELOG = ROOT / "changelog"
PLUGIN = ROOT / "plugin"
TG_ENV = Path.home() / ".config/envs/builderminseo-telegram.env"
STATE.mkdir(exist_ok=True); CHANGELOG.mkdir(exist_ok=True); INBOX.mkdir(exist_ok=True)

TODAY = date.today().isoformat()

def log(*a): print(f"[{datetime.now():%H:%M:%S}]", *a, flush=True)

def load_yaml(p):
    with open(p, encoding="utf-8") as f: return yaml.safe_load(f) or {}

def domains(): return load_yaml(DOMAINS)
def sources(): return load_yaml(SOURCES)

def source_index():
    """url host/handle → source dict (weight·license 조회용)."""
    idx = {}
    for dom, lst in sources().items():
        for s in lst or []:
            idx[norm_url(s.get("url", ""))] = dict(s, domain=dom)
    return idx

def norm_url(u):
    u = (u or "").strip().lower().rstrip("/")
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u

def source_for(url, idx):
    """같은 호스트의 소스 중 URL 공통 접두가 가장 긴 것. SNS는 호스트+핸들까지 일치해야 한다."""
    n = norm_url(url); host = n.split("/")[0]; best = None; best_len = -1
    for k, v in idx.items():
        if not k or k.split("/")[0] != host: continue
        if host in ("threads.net", "threads.com", "instagram.com", "youtube.com", "x.com", "blog.naver.com"):
            handle = "/".join(k.split("/")[:2])
            if not n.startswith(handle): continue
        common = len(os.path.commonprefix([n, k]))
        if common > best_len: best, best_len = v, common
    return best

def src_lookup(s, idx):
    """claim의 출처 1건 → sources.yaml 항목. 추출 때 기록한 source(채널 이름)가 있으면 그것, 없으면 URL로."""
    name = s.get("source")
    if name:
        for v in idx.values():
            if v.get("name") == name: return v
    return source_for(s.get("url"), idx)

# ---------- claim 파일 (frontmatter + 본문) ----------
FM = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)

def read_claim(p):
    m = FM.match(Path(p).read_text(encoding="utf-8"))
    if not m: raise ValueError(f"frontmatter 없음: {p}")
    fm = yaml.safe_load(m.group(1)) or {}
    fm["_path"] = str(p); fm["_body"] = m.group(2).strip()
    return fm

def write_claim(fm):
    fm = dict(fm); p = Path(fm.pop("_path")); body = fm.pop("_body", "")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip() + "\n---\n" + body.strip() + "\n", encoding="utf-8")

def claims(domain=None):
    out = []
    for d in sorted(ARCHIVE.iterdir()):
        if not d.is_dir() or (domain and d.name != domain): continue
        for p in sorted(d.glob("*.md")): out.append(read_claim(p))
    return out

def next_id(domain):
    nums = [int(m.group(1)) for p in (ARCHIVE / domain).glob("*.md") if (m := re.search(r"-(\d{4})\.md$", p.name))]
    return f"{domain}-{(max(nums) + 1 if nums else 1):04d}"

def claim_path(cid):
    dom = cid.rsplit("-", 1)[0]
    return ARCHIVE / dom / f"{cid}.md"

# ---------- 상태·변경 이력 ----------
def state_get(name, default=None):
    p = STATE / f"{name}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else (default if default is not None else {})

def state_set(name, data):
    (STATE / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

def record_change(kind, cid, note=""):
    p = CHANGELOG / f"{TODAY}.json"
    lst = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
    lst.append({"ts": datetime.now().isoformat(timespec="seconds"), "kind": kind, "id": cid, "note": note})
    p.write_text(json.dumps(lst, ensure_ascii=False, indent=1), encoding="utf-8")

def heartbeat(job, ok=True, note=""):
    hb = state_get("heartbeat")
    hb[job] = {"at": datetime.now().isoformat(timespec="seconds"), "ok": ok, "note": note}
    state_set("heartbeat", hb)

# ---------- 외부 호출 ----------
def http_get(url, timeout=25, _hops=0):
    url = urllib.parse.quote(url, safe=":/?&=#%+$@!*'(),;~")  # 한글 경로·쿼리 인코딩
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 Chrome/130 Safari/537.36", "Accept-Language": "ko,en"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 307, 308) and e.headers.get("Location") and _hops < 3:
            return http_get(urllib.parse.urljoin(url, e.headers["Location"]), timeout, _hops + 1)
        raise

def html_to_text(html):
    html = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", html)
    import html as _h
    links = [(_h.unescape(h), _h.unescape(re.sub(r"<.*?>", "", t)).strip()) for h, t in re.findall(r'(?is)<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html)]
    text = re.sub(r"(?s)<.*?>", " ", html)
    text = re.sub(r"&nbsp;", " ", text); text = re.sub(r"[ \t]+", " ", text); text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip(), [(h, t) for h, t in links if t and len(t) > 3]

def telegram(text):
    if not TG_ENV.exists(): log("telegram env 없음, 출력으로 대체:\n" + text); return
    env = dict(l.split("=", 1) for l in TG_ENV.read_text().splitlines() if "=" in l)
    data = json.dumps({"chat_id": env["CHAT_ID"].strip(), "text": text[:4000], "parse_mode": "HTML", "disable_web_page_preview": True}).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{env['BOT_TOKEN'].strip()}/sendMessage", data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r: return json.loads(r.read())

def run_claude(prompt, allowed_tools=None, model=None, timeout=900):
    """Claude Code headless. JSON 결과를 기대하며, 코드펜스는 벗긴다."""
    cmd = ["claude", "-p", "--output-format", "json", "--permission-mode", "bypassPermissions"]
    if model or os.environ.get("BOTONG_MODEL"): cmd += ["--model", model or os.environ["BOTONG_MODEL"]]
    if allowed_tools: cmd += ["--allowedTools", ",".join(allowed_tools)]
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout, cwd=str(ROOT / "state"))
    if r.returncode != 0: raise RuntimeError(f"claude 실패 rc={r.returncode}: {r.stderr[-800:]}")
    wrapper = json.loads(r.stdout); text = wrapper.get("result", "")
    m = re.search(r"```(?:json)?\s*(.*?)```", text, re.S)
    text = m.group(1) if m else text
    try: return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r"(\{.*\}|\[.*\])", text, re.S)
        if not m: raise RuntimeError("JSON 파싱 실패: " + text[:500])
        return json.loads(m.group(1))

def sha(s): return hashlib.sha1(s.encode("utf-8")).hexdigest()[:12]


_DL = re.compile(r"(\d{4})[-.년]\s*(\d{1,2})[-.월]\s*(\d{1,2})일?(?:\s*\d{1,2}:\d{2})?(?:\s*[~∼-]\s*(?:(\d{4})[-.년]\s*)?(\d{1,2})[-.월]\s*(\d{1,2})일?(?:\s*\d{1,2}:\d{2})?)?(\s*(?:\([^)]{0,8}\)\s*)?(?:까지|마감))?")
def deadline_of(text):
    """주장 문장 속 신청·모집 마감일. 'YYYY-MM-DD까지/마감' 또는 'A~B' 기간의 끝날만 마감으로 본다(시행일 '부터'는 제외)."""
    best = None
    for m in _DL.finditer(text or ""):
        y, mo, d, y2, mo2, d2, tail = m.groups()
        try:
            if mo2: dl = date(int(y2 or y), int(mo2), int(d2))
            elif tail: dl = date(int(y), int(mo), int(d))
            else: continue
        except ValueError: continue
        best = max(best, dl) if best else dl
    return best
