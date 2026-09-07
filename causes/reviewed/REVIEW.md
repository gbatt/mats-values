# Cause set reviews

**Frozen 2026-09-07 as `../final/causes_v1.jsonl` (889 causes)** after Nikhil accepted the round-3 proposal: 29 drops, 4 relabels, 8 pair declarations removed, no text edited. Provenance and known leans in `../final/README.md`.

Three rounds, newest first: round 3 (round 2 after the patch), round 2, round 1.

# Review of round 3, the patched round-2 set (2026-09-07)

Input: `../codex/round3/causes.jsonl`, which is round 2 with 274 items replaced: the 212 listed in `round2/patch_ids.md`, 53 more that Codex replaced to meet the four-per-subject cap and the one-kind rules (authorised in the request's addendum), and 9 pair partners. Verified: the other 644 records are byte-identical to round 2, both hand-kept items are intact, every listed id changed. Output: `round3/causes_reviewed.jsonl` (round-2 review carried for unchanged items, fresh review for the 274), `round3/proposal.json`, and a CSV outside the repo with a `proposal` column.

## Verdict

**Usable. Freeze it with 29 drops and 4 domain relabels rather than send a third patch.** The four devices the patch targeted are gone or nearly so. What remains is a set of residual leans, each measured below, none of which a further generation pass is likely to remove without creating another, and all of which the experiment's own tests are designed to catch.

## Mechanical, round 2 against round 3

| | Round 2 | Round 3 |
|---|---:|---:|
| verb clause, harmful / neutral / positive | 28% / 25% / 20% | 28% / 23% / 19% |
| bag-of-words leave-one-domain-out, all words | 65% | 65% |
| same, 45 most skewed words only | 39% | 41% |
| critic's-label regex hits | 30 | 0 |
| harmful advocacy items phrased as a bare policy outcome | 27 of 45 | 0 (7 now name a campaign) |
| sports positives that are disability sport | 11 of 18 | 4 of 18 |
| hard-rule failures | 0 | 0 |

## Per-item review of the 274 replacements (three reviewers)

plaus 2 / 1 / 0: 169 / 101 / 4. Natural 229. Bucket disagreements 30, almost all harmful items a stranger would read as neutral. Domain errors 4. Critic's labels 8. Unclear 10. Live duplicate links 17 pairs.

## Residual leans, measured

- **Sign not in the phrase.** About 30 harmful replacements read as neutral to a stranger ("copyright enforcement seminars", "dermatoglyphics assessments"). Since the probe's label is the model's own score, these land wherever the model puts them; they thin the intended harmful bucket rather than mislabel it.
- **Subject clusters the replacements created.** Politics harmful autocracy 8 of 18, education harmful pseudo-credentials about 7, mental_health harmful fringe therapy about 8, religion harmful pay-for-blessing 6. Within-domain topic concentration; leave-one-domain-out holds out the whole domain, so it cannot leak across domains, and the minimal pairs test within.
- **Advocacy phrasing.** Harmful advocacy moved from policy nouns to "campaign" and "coalition" while positive advocacy kept "X advocacy" (ends 6 / 6 / 17). Within the 100 advocacy items, the organisational noun alone predicts a held-out domain's bucket at 56% against a 45% majority baseline; the last word alone at 62%, about the same as all words. Bounded to one form, and the bag-of-words baseline reported beside every probe number is what keeps it honest.
- **International harmful** was judged weak in both rounds; 6 of its replacements have no recoverable sign.

## The proposal (`round3/proposal.json`)

Drop 29: 13 that are not a cause, unclear, or not a target, and 16 that are the weaker member of a live duplicate pair (17 harmful, 8 neutral, 4 positive). Relabel 4 domains per R1 and R3. Keep the 24 remaining bucket disagreements as they are, since the model's score decides the bin. Result: 889 causes, cells of 15 to 18, and 8 pairs whose partner was dropped, to be un-declared. Equal cells were a generation target, not an analysis requirement: splits stratify by proportion and leave-one-domain-out is by domain.

The alternative, a third Codex pass of roughly 60 replacements plus advocacy rewording and cluster thinning, was not sent: each pass so far has removed one lean and introduced another, and the clock is the binding constraint.

---

# Review of the round-2 cause set (2026-09-07)

Input: `../codex/round2/causes.jsonl` (918 causes, 17 domains × 3 buckets × 18, 2 to 7 words). Output: `round2/causes_reviewed.jsonl` (every row plus a `review` object), `round2/patch_ids.md` (the 212 items to replace, with reasons), `round2/patch_request.md` (the message for the generator), and a CSV for manual review outside the repo.

## Verdict

**Usable after a targeted patch of 212 items; do not regenerate.** Positive and neutral cells are largely real kinds. The harmful bucket is the weak third and needs about 45% of its items replaced, for four reasons that are each a residual surface tell: policy-outcome nouns as advocacy items, critic's labels, research items whose sign is not in the noun, and repeated kinds within and across domains. The 706 unlisted items stay verbatim so the replacements are written under the same rules as the items they join.

## Round 1 against round 2, whole set

| | Round 1 | Round 2 |
|---|---:|---:|
| items | 1,530 | 918 |
| mean words | 8.3 | 3.7 |
| verb clause, by bucket (harmful / neutral / positive) | 96% / 72% / 90% | 28% / 25% / 20% |
| words with 15+ occurrences and 80%+ in one bucket | 44 | 0 |
| bag-of-words leave-one-domain-out accuracy, all words | 90% | 65% |
| same, 45 most skewed words only | 72% | 39% |
| same, first two words only | 43% | 38% |
| distinct score sequences across the 17 harmful cells | 4 | 17 |
| forms used | 5 of 7 | 7 of 7 |
| hard-rule failures under that round's rules | 4 | 0 |

Chance for the classifier is 33%. The remaining 65% with all words is content, not structure: the words that still lean on one bucket at low counts are kinds (deregulation, repeal, cooperative, rural, low-cost), and the two structural residuals below are what the patch removes.

## Per-item review (six reviewers, every item read)

| Bucket | plaus 2 (real kind) | plaus 1 (contrived) | plaus 0 (not a cause) | natural | keep / edit / drop |
|---|---:|---:|---:|---:|---|
| harmful | 146 | 151 | 9 | 230 | 93 / 204 / 9 |
| neutral | 188 | 117 | 1 | 276 | 159 / 146 / 1 |
| positive | 280 | 26 | 0 | 298 | 231 / 75 / 0 |

Round 1 for comparison: plaus 0 was 133 harmful, 134 neutral, 1 positive. "Edit" counts anything flagged, including plaus 1 alone, which is not by itself a reason to replace.

Flags: not a donation target 38 (23 harmful, 13 neutral, 2 positive); critic's label 30 (29 harmful); bucket disagreements 29 (23 harmful judged neutral, mostly research items scored as if they were the practice they study); domain errors 10 (rule R1, four of them in media); undeclared same-kind clusters 72 (60 pairs, 10 triples, 2 quadruples; 69 of the members harmful); kinds appearing in two domains 13; prohibited content 0.

## Residual structural tells, measured

- **Advocacy form.** 27 of 45 harmful advocacy items are policy-goal noun phrases; 0 of 21 neutral and 0 of 34 positive are. Each goal noun (deregulation 10, repeal 8, abolition 7, expansion 9, all harmful-only) sits under the 12-occurrence threshold of the vocabulary rule, which is why the rule did not see it.
- **Critic's vocabulary.** 29 of the 30 evaluative-language flags are in the harmful bucket (conspiracy ×6, denial, censorship, clickbait, monopolists).
- **Subject clusters.** Science harmful is 14 of 18 pseudoscience; mental_health neutral is 12 of 18 workplace, relaxation or mindfulness; sports positive is 11 of 18 adaptive or disability sport.

## The patch (212 items)

By bucket: 139 harmful, 43 neutral, 30 positive. By reason (an item can have several): same kind as another item, not a target, critic's label, bucket wrong, contrived and unnatural, unclear, not a cause (10), and domain move (10). A first version also listed the whole international harmful cell on the reviewer's summary verdict; that blanket rule was removed the same day because it swept in the four items the reviewer had rated clean, and the other 12 were already listed on their own flags. Seven harmful cells lose 9 or more of their 18; 51 listed items are pair members, handled in the request. Corrected the same day: a first version of the list carried 62 extra ids with no reason, the kept members of duplicate clusters, from a script slip; two items were kept by hand after Nikhil's spot check (education-harmful-17, physical_health-harmful-18, recorded in `round2/decisions.json`), and Nikhil confirmed the evaluative, unclear, not-a-target, bucket, domain, safeguard-removal and contrived classes item by item, plus two seeded samples of the unlisted items. Reasons per id are in `round2/patch_ids.md`.

## Fixes applied

None to the data. Every fix here is content generation, which goes back to the generator under the same rules; the reviewed JSONL carries the flags only.

---

# Review of the round-1 cause set (2026-09-07)

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
