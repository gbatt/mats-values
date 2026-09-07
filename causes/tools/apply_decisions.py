"""Apply manual decisions to a round's patch list.

Usage: python apply_decisions.py round_dir
Reads round_dir/decisions.json ({id: {decision: keep|replace, by, note}}), round_dir/patch_ids.json
and round_dir/causes_reviewed.jsonl; rewrites patch_ids.json / patch_ids.md and stamps the
decision into each reviewed row's "decision" field.
"""
import json
import sys

d = sys.argv[1].rstrip("/")
decisions = json.load(open(f"{d}/decisions.json"))
ids = json.load(open(f"{d}/patch_ids.json"))
rows = [json.loads(l) for l in open(f"{d}/causes_reviewed.jsonl")]
by_id = {o["id"]: o for o in rows}

for i, dec in decisions.items():
    if dec["decision"] == "keep":
        ids.pop(i, None)
    elif dec["decision"] == "replace" and i not in ids:
        ids[i] = [f"manual: {dec.get('note', '')}"]
    by_id[i]["decision"] = dec

json.dump(ids, open(f"{d}/patch_ids.json", "w"), indent=1)
with open(f"{d}/patch_ids.md", "w") as f:
    f.write("| id | text | reason |\n|---|---|---|\n")
    for i in sorted(ids):
        f.write(f"| {i} | {by_id[i]['text']} | {'; '.join(dict.fromkeys(ids[i]))} |\n")
with open(f"{d}/causes_reviewed.jsonl", "w") as f:
    for o in rows:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(f"decisions applied: {len(decisions)}; patch list now {len(ids)} items")
