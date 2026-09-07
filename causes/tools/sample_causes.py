"""Draw a seeded random sample from a causes.jsonl, for the write-up's 'randomly selected, not cherry-picked' examples.
Usage: python sample_causes.py causes.jsonl [--n 12] [--seed 0] [--per-bucket]
"""

import argparse
import collections
import json
import random

ap = argparse.ArgumentParser()
ap.add_argument("path")
ap.add_argument("--n", type=int, default=12)
ap.add_argument("--seed", type=int, default=0)
ap.add_argument(
    "--per-bucket",
    action="store_true",
    help="n per bucket instead of n overall",
)
a = ap.parse_args()
rng = random.Random(a.seed)
rows = [json.loads(l) for l in open(a.path) if l.strip()]
if a.per_bucket:
    by = collections.defaultdict(list)
    [by[r["valence"]].append(r) for r in rows]
    picks = [
        r for b in ("harmful", "neutral", "positive") for r in rng.sample(by[b], a.n)
    ]
else:
    picks = rng.sample(rows, a.n)
print(f"seed {a.seed}, {len(picks)} of {len(rows)} from {a.path}")
for r in picks:
    print(
        f"  {r['id']:28s} {r['valence']:8s} {r['est_score']:5d}  {r['form']:11s} {r['text']}"
    )
