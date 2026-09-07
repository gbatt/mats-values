"""Convert the frozen cause set and the template module into interp-utils inputs.

Usage: python to_items.py
Writes causes/final/items_v1.jsonl (one interp-utils item per cause) and
prompts/templates_v1.json (template name -> text) plus prompts/templates_meta.json
(construct and cause position per template), all relative to the repo root.
"""

import importlib.util
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
causes = [
    json.loads(l) for l in open(root / "causes/final/causes_v1.jsonl") if l.strip()
]

with open(root / "causes/final/items_v1.jsonl", "w") as f:
    for c in causes:
        item = {
            "id": c["id"],
            "slots": {"cause": c["text"]},
            "tags": {
                "domain": c["domain"],
                "valence": c["valence"],
                "form": c["form"],
                "est_score": c["est_score"],
                "contested": c["contested"],
                "pair_id": c["pair_id"],
                "pair_type": c["pair_type"],
                "patched": c["patched"],
            },
        }
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

spec = importlib.util.spec_from_file_location(
    "templates", root / "prompts/stated_cause_value.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
templates = {
    name.replace("TEMPLATE_", "").lower(): getattr(mod, name)
    for name in dir(mod)
    if name.startswith("TEMPLATE_")
}
meta = {
    "v1": {"construct": "effect", "cause_position": "after_rubric", "note": "utility"},
    "v2": {
        "construct": "effect",
        "cause_position": "before_rubric",
        "note": "value, donor context",
    },
    "v3": {
        "construct": "effect",
        "cause_position": "after_rubric",
        "note": "usefulness",
    },
    "v4": {
        "construct": "preference",
        "cause_position": "before_rubric",
        "note": "foundation decision maker",
    },
    "v5": {
        "construct": "preference",
        "cause_position": "after_rubric",
        "note": "friend asks for a view",
    },
}
assert set(templates) == set(meta), (sorted(templates), sorted(meta))
for name, text in templates.items():
    assert "{cause}." in text, name
    assert text.count("{cause}") == 1, name
json.dump(
    templates,
    open(root / "prompts/templates_v1.json", "w"),
    indent=1,
    ensure_ascii=False,
)
json.dump(meta, open(root / "prompts/templates_meta.json", "w"), indent=1)
print(
    f"items: {len(causes)} -> causes/final/items_v1.jsonl | templates: {sorted(templates)} -> prompts/templates_v1.json"
)
