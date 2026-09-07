# causes_v1 — frozen 2026-09-07

`causes_v1.jsonl`: 889 causes, the dataset for the scoring and probing stages. Same fields as the generator's output (id, domain, valence, est_score, form, text, contested, pair_id, pair_type) plus `patched` (true for the 274 items written in the round-2 patch, false for items unchanged since round 2). The `domain` field is authoritative; ids are the round-3 ids and keep their original prefix even where the domain was relabelled.

## Provenance

Round 1 (1,530 causes) was rejected on review. Round 2 (918, 18 per domain × valence bucket, 2 to 7 words) passed the mechanical checks; per-item review plus Nikhil's spot checks produced a 212-item patch. Round 3 is round 2 with 274 items replaced (the 212, 53 replaced by the generator to meet the four-per-subject cap, and 9 pair partners); the other 644 records are byte-identical to round 2. The full trail is in `../reviewed/REVIEW.md`, the generator inputs in `../inputs/`, and every raw round in `../codex/`.

From round 3 to this file: 29 items dropped, 4 items relabelled to another domain under the tie-break rules, 8 pair declarations removed because the partner was dropped. No text was edited. The 24 items whose intended bucket the reviewers disputed are kept unchanged, since the label used downstream is the model's own score, not `valence` or `est_score`.

## Cell sizes

| domain | harmful | neutral | positive |
|---|---:|---:|---:|
| agriculture | 17 | 18 | 18 |
| animals | 18 | 17 | 18 |
| arts | 18 | 18 | 17 |
| economy | 17 | 18 | 18 |
| education | 17 | 18 | 17 |
| environment | 18 | 18 | 18 |
| international | 16 | 17 | 15 |
| justice | 18 | 18 | 19 |
| media | 16 | 18 | 18 |
| mental_health | 17 | 17 | 18 |
| physical_health | 18 | 17 | 18 |
| politics | 15 | 16 | 17 |
| religion | 15 | 18 | 18 |
| safety | 17 | 18 | 18 |
| science | 18 | 18 | 18 |
| social | 17 | 16 | 19 |
| sports | 17 | 18 | 18 |

Valence buckets: harmful 289, neutral 298, positive 302. Equal cells were a generation target, not an analysis requirement: splits stratify by proportion and leave-one-domain-out is by domain.

## Known leans (measured in `../reviewed/REVIEW.md`, round 3)

- About 30 harmful items read as neutral to a reader without domain knowledge; they thin the intended harmful bucket rather than mislabel it.
- Subject concentration inside a few harmful cells (politics autocracy, education pseudo-credentials, mental_health fringe therapy, religion pay-for-blessing).
- Advocacy phrasing: harmful advocacy tends to "campaign" / "coalition", positive to "… advocacy"; within the advocacy form the organisational noun predicts a held-out domain's bucket at 56% against a 45% baseline.
- After the drops, three cells have no item of one form (physical_health neutral and economy neutral lack advocacy; religion harmful lacks research), the advocacy form is 42 / 18 / 33 across buckets (45.2% harmful against the 45% generation cap), and one word crosses the 65% vocabulary line (see the checker output). The checker run with `--frozen` reports these as diagnostics; nothing further is generated to fix them.
- Bag-of-words on the text, leave-one-domain-out: 65% with all words, 41% with the 45 most skewed words (chance 33%). Report this baseline beside every probe number.

## Dropped (29)

- `agriculture-harmful-08`: duplicate
- `animals-neutral-13`: duplicate
- `arts-positive-11`: duplicate
- `economy-harmful-18`: not a cause / unclear / not a target
- `economy-neutral-05`: not a cause / unclear / not a target
- `education-harmful-17`: not a cause / unclear / not a target
- `international-harmful-12`: not a cause / unclear / not a target
- `international-harmful-15`: duplicate
- `international-neutral-14`: not a cause / unclear / not a target
- `international-positive-14`: duplicate
- `international-positive-16`: not a cause / unclear / not a target
- `media-harmful-11`: not a cause / unclear / not a target
- `media-harmful-16`: duplicate
- `mental_health-harmful-12`: not a cause / unclear / not a target
- `mental_health-neutral-17`: duplicate
- `physical_health-neutral-13`: not a cause / unclear / not a target
- `politics-harmful-01`: duplicate
- `politics-harmful-09`: not a cause / unclear / not a target
- `politics-harmful-15`: not a cause / unclear / not a target
- `politics-neutral-08`: duplicate
- `politics-neutral-11`: duplicate
- `politics-positive-13`: duplicate
- `religion-harmful-07`: not a cause / unclear / not a target
- `religion-harmful-08`: duplicate
- `religion-harmful-09`: duplicate
- `safety-harmful-03`: duplicate
- `social-harmful-18`: duplicate
- `social-neutral-08`: duplicate
- `sports-harmful-18`: not a cause / unclear / not a target

## Relabelled (4)

- `education-positive-03` → `social`
- `politics-harmful-15` → `international`
- `social-neutral-04` → `economy`
- `international-positive-05` → `justice`

## Pair declarations removed (8)

- `arts-harmful-02` (was minimal pair `arts-m1`)
- `mental_health-positive-18` (was minimal pair `mental_health-m1`)
- `politics-harmful-06` (was minimal pair `politics-m1`)
- `religion-neutral-07` (was minimal pair `religion-m4`)
- `sports-neutral-11` (was minimal pair `sports-m1`)
- `social-harmful-13` (was minimal pair `social-m4`)
- `international-harmful-11` (was minimal pair `international-m4`)
- `international-neutral-17` (was minimal pair `international-m3`)
