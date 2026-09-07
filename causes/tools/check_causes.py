"""Mechanical checks + lexical-shortcut analysis for a causes.jsonl.

Usage: uv run --with scikit-learn --with numpy python check_causes.py causes.jsonl [--per-cell 18] [--words 2 7]
       [--vocab-min 12 --vocab-share 0.65] [--form-cap 0.45] [--prev round1.jsonl]
Prints a digest; exits 1 if any hard rule fails.
"""

import argparse
import collections
import itertools
import json
import re
import sys

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold, cross_val_score

ap = argparse.ArgumentParser()
ap.add_argument("path")
ap.add_argument("--per-cell", type=int, default=18)
ap.add_argument("--words", type=int, nargs=2, default=[2, 7])
ap.add_argument("--vocab-min", type=int, default=12)
ap.add_argument("--vocab-share", type=float, default=0.65)
ap.add_argument("--form-cap", type=float, default=0.45)
ap.add_argument("--forms-per-cell", type=int, default=1)
ap.add_argument("--prev", help="previous-round jsonl, to count kept items")
ap.add_argument(
    "--frozen",
    action="store_true",
    help="frozen set: report cell sizes and pair counts instead of enforcing them",
)
a = ap.parse_args()

rows = [json.loads(l) for l in open(a.path) if l.strip()]
B = ["harmful", "neutral", "positive"]
RNG = {"harmful": (-100, -34), "neutral": (-33, 33), "positive": (34, 100)}
DOM = "arts education environment animals physical_health mental_health science media safety justice politics agriculture economy religion sports social international".split()
FORMS = "advocacy research venture capital institution service programme".split()
BANNED = "routine established comfortable ordinary standard conventional affluent well-equipped decorative ceremonial".split()
tok = lambda t: re.findall(r"[a-z][a-z'-]+", t.lower())
fails = []


def rule(ok, msg):
    print(("  ok   " if ok else "  FAIL ") + msg)
    if not ok:
        fails.append(msg)


print(f"== {a.path}: {len(rows)} rows")
rule(
    sorted({r["domain"] for r in rows}) == sorted(DOM),
    "all 17 domains present, no others",
)
cells = collections.Counter((r["domain"], r["valence"]) for r in rows)
rule(
    a.frozen or (len(cells) == 51 and set(cells.values()) == {a.per_cell}),
    f"exactly {a.per_cell} per cell ({len(cells)} cells, sizes {sorted(set(cells.values()))})",
)
bad = [
    r["id"]
    for r in rows
    if not RNG[r["valence"]][0] <= r["est_score"] <= RNG[r["valence"]][1]
]
rule(not bad, f"est_score inside bucket range ({len(bad)} outside)")
ids = [r["id"] for r in rows]
rule(len(ids) == len(set(ids)), "ids unique")
texts = [r["text"] for r in rows]
rule(len(texts) == len(set(texts)), "texts unique")
wl = [len(r["text"].split()) for r in rows]
badl = [r["id"] for r, n in zip(rows, wl) if not a.words[0] <= n <= a.words[1]]
rule(
    not badl,
    f"{a.words[0]}-{a.words[1]} words ({len(badl)} outside; mean {np.mean(wl):.1f})",
)
badb = [(r["id"], w) for r in rows for w in tok(r["text"]) if w in BANNED]
rule(not badb, f"banned adjectives absent ({len(badb)} hits: {badb[:5]})")
badf = [r["id"] for r in rows if r["form"] not in FORMS]
rule(not badf, f"form in the seven ({len(badf)} not)")
# forms per cell and set-level cap
fc = collections.Counter((r["domain"], r["valence"], r["form"]) for r in rows)
missing = [
    (d, v, f) for d in DOM for v in B for f in FORMS if fc[(d, v, f)] < a.forms_per_cell
]
rule(
    a.frozen or not missing,
    f"every form >= {a.forms_per_cell} in every cell ({len(missing)} missing, e.g. {missing[:4]})",
)
fb = {
    f: [sum(1 for r in rows if r["form"] == f and r["valence"] == v) for v in B]
    for f in FORMS
}
over = {f: c for f, c in fb.items() if sum(c) and max(c) / sum(c) > a.form_cap}
rule(not over, f"no form > {a.form_cap:.0%} in one bucket ({over})")
print("     form x bucket:", {f: c for f, c in fb.items()})
# vocabulary rule
wc = {b: collections.Counter() for b in B}
for r in rows:
    for w in set(tok(r["text"])):
        wc[r["valence"]][w] += 1
allw = collections.Counter()
[allw.update(c) for c in wc.values()]
skew = sorted(
    [
        (max(wc[b][w] for b in B) / n, n, w, [wc[b][w] for b in B])
        for w, n in allw.items()
        if n >= a.vocab_min
    ],
    reverse=True,
)
viol = [x for x in skew if x[0] > a.vocab_share]
rule(
    a.frozen or not viol,
    f"no word with >= {a.vocab_min} occurrences above {a.vocab_share:.0%} in one bucket ({len(viol)} violate)",
)
for share, n, w, c in viol[:25]:
    print(f"       {w:18s} {c}  share {share:.2f}")
# score sequence rule
seq = {}
for r in rows:
    n = int(r["id"].rsplit("-", 1)[1])
    seq.setdefault((r["domain"], r["valence"]), {})[n] = r["est_score"]
seqs = [tuple(v[k] for k in sorted(v)) for v in seq.values()]
dup_seq = len(seqs) - len(set(seqs))
rep6 = sum(
    1
    for s in seqs
    if len(s) >= 12
    and any(
        s[i : i + 6] == s[j : j + 6]
        for i in range(len(s) - 11)
        for j in range(i + 6, len(s) - 5)
    )
)
rule(
    dup_seq == 0 and rep6 == 0,
    f"no repeated score sequences (dup cell sequences {dup_seq}, cells with a repeating 6-pattern {rep6})",
)
for b in B:
    s = [r["est_score"] for r in rows if r["valence"] == b]
    near = sum(1 for x in s if abs(abs(x) - 33) <= 15)
    print(
        f"     {b}: mean {np.mean(s):.0f} sd {np.std(s):.0f} min {min(s)} max {max(s)}; within 15 of boundary {near}/{len(s)}; contested {sum(r['contested'] for r in rows if r['valence'] == b)}"
    )
# pairs
pairs = collections.defaultdict(list)
for r in rows:
    if r.get("pair_id"):
        pairs[r["pair_id"]].append(r)
badp = [
    k for k, v in pairs.items() if len(v) != 2 or len({x["pair_type"] for x in v}) != 1
]
mins = [v for v in pairs.values() if v[0]["pair_type"] == "minimal"]
paras = [v for v in pairs.values() if v[0]["pair_type"] == "paraphrase"]
badmin = [
    v[0]["pair_id"]
    for v in mins
    if v[0]["valence"] == v[1]["valence"]
    or len(set(v[0]["text"].split()) ^ set(v[1]["text"].split())) > 4
]
badpar = [
    v[0]["pair_id"]
    for v in paras
    if v[0]["valence"] != v[1]["valence"] or v[0]["est_score"] != v[1]["est_score"]
]
permin = collections.Counter(v[0]["domain"] for v in mins)
perpar = collections.Counter(v[0]["domain"] for v in paras)
rule(not badp, f"pairs well-formed ({len(pairs)} pairs, {len(badp)} malformed)")
rule(
    a.frozen or all(permin[d] >= 3 for d in DOM),
    f">= 3 minimal pairs per domain (min {min(permin[d] for d in DOM)}, total {len(mins)})",
)
rule(
    a.frozen or all(perpar[d] == 2 for d in DOM),
    f"2 paraphrase pairs per domain (counts {sorted(set(perpar[d] for d in DOM))})",
)
rule(
    not badmin,
    f"minimal pairs differ by <= 2 words across buckets ({len(badmin)} bad: {badmin[:4]})",
)
rule(not badpar, f"paraphrase pairs same bucket + score ({len(badpar)} bad)")
# near-duplicates outside pairs
T = [(r["id"], set(tok(r["text"])), r.get("pair_id")) for r in rows]
nd = [
    (round(len(ta & tb) / len(ta | tb), 2), x, y)
    for (x, ta, px), (y, tb, py) in itertools.combinations(T, 2)
    if not (px and px == py) and len(ta & tb) / len(ta | tb) >= 0.7
]
print(
    f"  info near-duplicates outside pairs (jaccard >= .7): {len(nd)}",
    sorted(nd, reverse=True)[:6],
)
# constructions
PAT = {
    "safeguard_removal": r"\b(removing|excluding|concealing|discouraging|restricting|withholding|weakening|narrowing|omitting|hiding)\b",
    "diversion": r"\b(replacing|consuming|diverting|redirecting|absorbing|displacing|instead of)\b",
    "verb_clause": r"\b\w+ing\b",
}
for k, p in PAT.items():
    print(
        f"  info {k:18s}",
        "  ".join(
            f"{b} {100 * np.mean([bool(re.search(p, r['text'])) for r in rows if r['valence'] == b]):3.0f}%"
            for b in B
        ),
    )
# classifier
y = np.array([r["valence"] for r in rows])
g = np.array([r["domain"] for r in rows])


def cv(vec, name):
    X = vec.fit_transform(texts)
    s = cross_val_score(
        LogisticRegression(max_iter=3000), X, y, cv=GroupKFold(n_splits=17), groups=g
    )
    print(f"  info LODO bag-of-words acc, {name}: {s.mean():.3f} (chance .333)")


cv(CountVectorizer(binary=True), "all words")
top = [w for _, _, w, _ in skew[:45]]
cv(
    CountVectorizer(binary=True, vocabulary=top),
    f"top-45 most skewed words (>= {a.vocab_min} occ.)",
)
cv(
    CountVectorizer(binary=True, analyzer=lambda t: [" ".join(t.split()[:2])]),
    "first two words",
)
print(
    "  info top openings:",
    collections.Counter(" ".join(r["text"].split()[:2]) for r in rows).most_common(8),
)
if a.prev:
    prev = {json.loads(l)["text"] for l in open(a.prev) if l.strip()}
    kept = collections.Counter(r["valence"] for r in rows if r["text"] in prev)
    print(f"  info kept from previous round: {sum(kept.values())} {dict(kept)}")
print(f"\n{len(fails)} hard-rule failures" if fails else "\nall hard rules pass")
sys.exit(1 if fails else 0)
