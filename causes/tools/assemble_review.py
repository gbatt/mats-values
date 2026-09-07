"""Merge causes.jsonl with per-item reviewer JSONLs (schema in review_brief.md) -> reviewed JSONL + CSV + digest.
Usage: python assemble_review.py causes.jsonl review_dir out.jsonl out.csv [--apply-domain-fixes]
"""

import json, re, csv, glob, collections, sys
import argparse

_p = argparse.ArgumentParser()
_p.add_argument("src")
_p.add_argument("review_dir")
_p.add_argument("out_jsonl")
_p.add_argument("out_csv")
_p.add_argument("--apply-domain-fixes", action="store_true")
_a = _p.parse_args()
SRC = _a.src
REV = glob.glob(_a.review_dir + "/*.jsonl")
OUT_JSONL = _a.out_jsonl
OUT_CSV = _a.out_csv
APPLY_DOMAIN = _a.apply_domain_fixes

rows = [json.loads(l) for l in open(SRC)]
rev = {}
for f in REV:
    for l in open(f):
        l = l.strip()
        if not l:
            continue
        try:
            r = json.loads(l)
        except json.JSONDecodeError:
            print("bad line in", f, l[:80])
            continue
        rev[r["id"]] = r
print(f"reviews loaded: {len(rev)} from {len(REV)} files")

SKEW = "routine established from as comfortable promoting at funded opposing removing reaching into presenting meeting coordinating supporting low-income comparing restoring people grants affluent decorative standard schedules requesting isolated appointment serving underserved ordinary after petition consuming funds institute discouraging expanding hospitality well-equipped".split()
STOP = {"from", "as", "at", "into", "after"}
SKEWC = [w for w in SKEW if w not in STOP]
TEMPL = {
    "safeguard_removal": r"\b(removing|excluding|concealing|discouraging|restricting|withholding|weakening|narrowing|reducing|dropping|omitting|hiding|bypassing|skipping|ending|cancelling)\b",
    "diversion": r"\b(replacing|consuming|diverting|redirecting|absorbing|displacing|instead of)\b",
    "adjective_padding": r"\b(routine|established|comfortable|ordinary|standard|conventional|affluent|well-equipped|decorative|ceremonial)\b",
}
tok = lambda t: set(re.findall(r"[a-z][a-z'-]+", t.lower()))

out = []
for r in rows:
    v = rev.get(r["id"], {})
    lang = v.get("lang") or []
    o = dict(r)
    o["review"] = {
        "plaus": v.get("plaus"),
        "construct": v.get("construct"),
        "bucket_ok": v.get("bucket_ok"),
        "sugg_valence": v.get("sugg_valence"),
        "score_ok": v.get("score_ok"),
        "domain_ok": v.get("domain_ok"),
        "sugg_domain": v.get("sugg_domain"),
        "rule": v.get("rule"),
        "lang": lang,
        "note": v.get("note") or "",
        "skewed_words": sorted(tok(r["text"]) & set(SKEWC)),
        "template": [k for k, p in TEMPL.items() if re.search(p, r["text"])],
    }
    rv = o["review"]
    if not v:
        rec = "unreviewed"
    elif rv["plaus"] == 0 or "prohibited" in lang:
        rec = "drop"
    elif (
        rv["plaus"] == 1
        or rv["construct"] not in (None, "natural")
        or rv["bucket_ok"] is False
        or rv["domain_ok"] is False
        or lang
    ):
        rec = "edit"
    else:
        rec = "keep"
    rv["recommend"] = rec
    o["fix"] = None
    if APPLY_DOMAIN and rv["domain_ok"] is False and rv["sugg_domain"]:
        o["fix"] = f"domain {r['domain']} -> {rv['sugg_domain']} ({rv['rule']})"
        o["domain"] = rv["sugg_domain"]
    out.append(o)

with open(OUT_JSONL, "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")

cols = [
    "id",
    "domain",
    "valence",
    "est_score",
    "form",
    "text",
    "contested",
    "pair_id",
    "pair_type",
    "recommend",
    "plaus",
    "construct",
    "bucket_ok",
    "sugg_valence",
    "score_ok",
    "domain_ok",
    "sugg_domain",
    "rule",
    "lang",
    "reviewer_note",
    "skewed_words",
    "template",
    "fix",
    "my_decision",
    "my_notes",
]
with open(OUT_CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    for o in out:
        rv = o["review"]
        w.writerow(
            {
                **{k: o.get(k) for k in cols[:9]},
                "recommend": rv["recommend"],
                "plaus": rv["plaus"],
                "construct": rv["construct"],
                "bucket_ok": rv["bucket_ok"],
                "sugg_valence": rv["sugg_valence"],
                "score_ok": rv["score_ok"],
                "domain_ok": rv["domain_ok"],
                "sugg_domain": rv["sugg_domain"],
                "rule": rv["rule"],
                "lang": " ".join(rv["lang"]),
                "reviewer_note": rv["note"],
                "skewed_words": " ".join(rv["skewed_words"]),
                "template": " ".join(rv["template"]),
                "fix": o["fix"],
                "my_decision": "",
                "my_notes": "",
            }
        )

# digest
B = ["harmful", "neutral", "positive"]
C = collections.Counter
print("\nrecommend by bucket:")
for b in B:
    c = C(o["review"]["recommend"] for o in out if o["valence"] == b)
    print(f"  {b:9s}", dict(c))
print("recommend by domain (drop/edit/keep):")
for d in sorted({o["domain"] for o in out}):
    c = C(o["review"]["recommend"] for o in out if o["domain"] == d)
    print(
        f"  {d:16s} drop {c['drop']:3d}  edit {c['edit']:3d}  keep {c['keep']:3d}  unreviewed {c['unreviewed']:3d}"
    )
print(
    "plaus by bucket:",
    {b: dict(C(o["review"]["plaus"] for o in out if o["valence"] == b)) for b in B},
)
print(
    "construct by bucket:",
    {b: dict(C(o["review"]["construct"] for o in out if o["valence"] == b)) for b in B},
)
print(
    "bucket_ok=false:",
    sum(o["review"]["bucket_ok"] is False for o in out),
    "domain_ok=false:",
    sum(o["review"]["domain_ok"] is False for o in out),
    "lang flags:",
    dict(C(l for o in out for l in o["review"]["lang"])),
)
print(
    "sugg_valence:",
    dict(
        C(
            (o["valence"], o["review"]["sugg_valence"])
            for o in out
            if o["review"]["bucket_ok"] is False
        )
    ),
)
print(
    "domain moves:",
    dict(
        C(
            (o["id"].split("-")[0], o["review"]["sugg_domain"])
            for o in out
            if o["review"]["domain_ok"] is False
        )
    ),
)
