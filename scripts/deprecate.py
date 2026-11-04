#!/usr/bin/env python3
"""사후 거부·폐기. 사용: deprecate.py <id> "사유" [--status stale]"""
import sys
from common import *
cid = sys.argv[1]; reason = sys.argv[2] if len(sys.argv) > 2 else "민서 거부"; st = "stale" if "--status" in sys.argv and "stale" in sys.argv else "deprecated"
c = read_claim(claim_path(cid)); c["status"] = st; c.setdefault("tags", []).append(f"{st}:{TODAY}"); c["_body"] += f"\n\n**{st} ({TODAY})**: {reason}"
write_claim(c); record_change(st, cid, reason); log(f"{cid} → {st}: {reason}")
