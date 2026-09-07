# causes/tools

- `check_causes.py` — mechanical rules for a round's `causes.jsonl` (cell counts, length, banned words, forms, vocabulary skew, score sequences, pairs) plus the lexical-shortcut analysis (per-word bucket skew, construction regexes, leave-one-domain-out bag-of-words classifier). Round-1 numbers: `--per-cell 30 --words 3 12 --vocab-min 15 --vocab-share 0.8`; round-2 defaults match the round-2 prompt.
- `review_brief.md` — the per-item review brief given to each reviewer (one reviewer per two or three domains); defines the review JSONL schema.
- `assemble_review.py` — merges reviewer JSONLs with the data into a reviewed JSONL and a CSV for manual review, with a keep / edit / drop recommendation per row.
