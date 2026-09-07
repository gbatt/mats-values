# Review of the round-1 cause set

Reviewed 2026-09-07. Input: `../codex/round1/causes.jsonl` (1,530 causes, 17 domains × 3 buckets × 30). Output: `causes_reviewed.jsonl` (every input row plus a `review` object and a `fix` field) and a CSV for manual review.

## Verdict

**Regenerate.** The set passes every count check and fails as data. The positive bucket is largely real causes; the harmful and neutral buckets are built from a handful of sentence templates and filler adjectives, so a reader can tell the bucket from the grammar without understanding the cause. That is the shortcut the dataset exists to exclude. Editing cannot fix it, because the pattern covers most of two buckets. Regenerate all three buckets together under the round-2 prompt (`../inputs/cause-generation-prompt-v2.md`) rather than keeping the round-1 positives: mixing kept positives with regenerated harmful and neutral items would make bucket recoverable from writing style.

## Per-item review (six reviewers, one per two or three domains, every item read)

| Bucket | plaus 2 (real cause) | plaus 1 (contrived) | plaus 0 (not a cause) | natural | templated or padded | recommend keep / edit / drop |
|---|---:|---:|---:|---:|---:|---|
| harmful | 55 | 322 | 133 | 162 | 348 | 49 / 321 / 140 |
| neutral | 99 | 277 | 134 | 153 | 357 | 70 / 306 / 134 |
| positive | 460 | 49 | 1 | 488 | 22 | 455 / 54 / 1 |

Templated or padded: harmful = safeguard removal (131) + diversion (147) + other unnatural (70); neutral = adjective padding (252) + other unnatural (105).

Other flags: bucket disagreements 18 (ten harmful items judged neutral, six positive judged neutral); prohibited content 12 (all embezzlement, fraud or illegal-conduct constructions in the harmful bucket; none violent or hateful); evaluative wording 12; unclear or ungrammatical 53; domain errors 4.

## Mechanical findings (whole set)

- **Bucket-specific vocabulary.** 45 words with 15+ occurrences have 80%+ of them in one bucket; 846 of 1,530 causes contain at least one. A bag-of-words logistic regression evaluated leave-one-domain-out scores 90% with all words and **72% with those 45 words alone** (chance 33%). The generator balanced the 15 marker words we listed exactly and left every other word unbalanced.
- **Harm by construction.** 49% of harmful causes match a safeguard-removal or diversion template ("restoring theatres while removing wheelchair access", "a patient lounge replacing a public dialysis ward").
- **Neutral by adjective.** 57% of neutral causes carry routine, established, comfortable, ordinary, standard, conventional, affluent, well-equipped, decorative or ceremonial.
- **Scores are a schedule.** Harmful cells across 17 domains use 4 distinct 30-score sequences, all the same ladder (−38, −46, −56, −65, −76, −84) rotated; neutral uses 3. `est_score` carries no information beyond the bucket.
- **Two forms missing.** No research and no venture causes anywhere.
- **One template per pair.** The three minimal pairs use the same three frames in all 17 domains; "a lobby for", "a pressure group" and "a campaign for" open 92 causes.

## Fixes applied in `causes_reviewed.jsonl`

Only rule-based or grammatical repairs, each recorded in the row's `fix` field:

- 4 domain moves per the tie-break rules: education-neutral-29 → arts (R6), safety-neutral-04 → sports, politics-neutral-12 → social, social-neutral-21 → sports (R9). Cell sizes are therefore 29–32 in six neutral cells.
- 2 truncated positive texts completed: sports-positive-12, religion-positive-17.

No bucket relabels, rescoring, or deletions: those are flagged for manual review, not applied.

## Files

- `causes_reviewed.jsonl`: input rows + `review` {plaus, construct, bucket_ok, sugg_valence, score_ok, domain_ok, sugg_domain, rule, lang, note, skewed_words, template, recommend} + `fix`.
- The CSV for Sheets (kept outside the repo) has the same columns flattened plus empty `my_decision` and `my_notes` columns.
