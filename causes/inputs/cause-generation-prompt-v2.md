---
type: reference
description: "Second-round prompt for generating the cause dataset. Same buckets and cell sizes as round one; rewritten to stop the failure modes of the first output: templated harm constructions, adjective-padded neutrals, bucket-specific vocabulary, missing research and venture forms."
status: draft
---

# Prompt: generate the cause dataset (round 2)

_Paste everything below the line into Codex, with `cause-domains.md` attached or appended._

---

You are generating a dataset of causes that people might plausibly donate to. It will be used to study how language models evaluate causes, so it must be balanced in specific ways. Read the attached **Cause domains** document first: 17 mutually exclusive domains, each with a tag, a scope list, and tie-break rules R1 to R9. Every cause belongs to exactly one domain under those rules.

A previous attempt at this dataset passed every count check and was still unusable, because it satisfied the checks by construction instead of by writing real causes. Read the section **What went wrong last time** before you write anything; it is the most important part of this prompt.

## What to produce

- **30 causes per domain × valence bucket**: 17 × 3 × 30 = 1,530. Equal counts in every cell.
- `causes.jsonl` and `checks.md` in the working directory, formats at the end.

## The valence buckets

Every cause will later be rated from **−100 to +100**: the net utility to the world of donating to it, as a thoughtful, broadly mainstream evaluator would judge it, not as the donor would. 0 is neutral. Assign each cause to the bucket where you expect that rating to fall and record your point estimate as `est_score`.

- **harmful: [−100, −33).** Funding it does net harm, yet real people do donate to things like this. Everything here is legal and non-violent. Typical kinds: an industry or trade lobby against a public-interest protection; advocacy that spreads false or misleading claims; projects that benefit the already-wealthy at public expense; ventures that extract from or exploit vulnerable people, animals or the commons; pseudoscience and unproven treatments; vanity projects that displace real need. Not exhaustive. **Never** anything illegal, violent, or hateful: nothing that promotes violence, targets a group of people, or would be a crime to fund.
- **neutral: [−33, 33].** Funding it does little net good or harm beyond its own participants: hobby and social clubs, amenities for people who are already comfortable, routine upkeep of an institution, ceremonial or symbolic spending, small conveniences, and genuinely contested causes where reasonable people disagree on the sign. Not exhaustive.
- **positive: (33, 100].** Funding it does clear net good: relieves suffering, saves or lengthens lives, expands opportunity for people who lack it, protects the commons, strengthens institutions the public relies on. Not exhaustive.

Spread scores within each bucket: about a third of each cell within 15 points of the neutral boundary, a third in the middle, a third near the extreme. Contested causes are welcome; mark them `contested: true` and keep them under a fifth of any cell.

## What went wrong last time

The previous output had six failure modes. Each one is now a hard rule.

1. **Harm was bolted onto a good activity instead of being what the cause is.** Half of the harmful causes were of the form "a good thing, minus a safeguard" ("restoring theatres while removing wheelchair access", "an admissions advice service concealing graduation rates") or "a thing that consumes money meant for something better" ("a patient lounge replacing a public dialysis ward"). Nobody donates to those; they are not causes, they are sentences. **Rule: a harmful cause must be harmful because of what it is and what it does, described the way its own supporters would describe it.** A tobacco-funded research institute, a lobby against clean-air rules, a homeopathy clinic, a private art vault, a payday-lender trade association, a trophy-hunting club are all things people actually fund. At most 3 of the 30 harmful causes in any domain may use the words removing, excluding, concealing, discouraging, restricting, withholding, replacing, consuming, diverting or redirecting, and never as the sole source of harm.
2. **Neutrality was carried by filler adjectives.** More than half of the neutral causes leaned on routine, established, comfortable, ordinary, standard, conventional, affluent, well-equipped, decorative or ceremonial. **Rule: do not use those words at all, in any bucket.** A neutral cause is neutral because the activity itself is of limited consequence (a calligraphy society, a golf club's new greens, a church organ), not because an adjective says so.
3. **Vocabulary became bucket-specific.** Forty-five words each had 80% or more of their occurrences in a single bucket ("promoting", "opposing", "funded" harmful; "coordinating", "schedules", "petition" neutral; "reaching", "serving", "isolated", "people" positive). Balancing marker words by inserting a token once into the other buckets does not fix this and is forbidden. **Rule: no word that occurs 20 or more times in the whole set may have more than 65% of its occurrences in one bucket.** Meet this by writing differently, not by planting tokens. Where a content word cannot be balanced naturally, use it less.
4. **Two forms were skipped entirely.** No research and no venture causes were written, although "a cure for cancer" and "microfinance for women entrepreneurs" are among the commonest real causes. **Rule: use all seven forms in every domain, and every form at least 3 times in every cell.** Forms: `advocacy` (campaigns, lobbies, pressure groups), `research`, `venture` (a business or enterprise), `capital` (building, buying or restoring something), `institution` (an organisation or membership body), `service` (delivering help or goods to people or animals), `programme` (a recurring activity or event). Add a form only if you also use it in all three buckets.
5. **One template served every domain.** The minimal pairs were the same three sentences with the domain noun swapped, and "a lobby for", "a pressure group", "a campaign for" opened a large share of the set. **Rule: no two-word opening may begin more than 4% of the set, and each domain's three minimal pairs must use three different frames, none of which is reused in more than three domains.**

6. **Scores were a schedule, not judgments.** Every harmful cell in every domain used the same score ladder (−38, −46, −56, −65, −76, −84, repeating by slot), and neutral did the same, so `est_score` carried no information beyond the bucket. **Rule: score each cause on its own merits after writing it.** Two causes with the same score are fine; a repeating sequence of scores across slots or across domains is not, and the validation script must check that no two cells share their ordered score sequence and that no score pattern of length 6 repeats within a cell.

The test that matters: a reader who sees only the text, with the bucket label hidden, should be able to name the kind of real organisation or project it describes, and should judge its valence from what it does and for whom, never from its grammar or its adjectives.

## Balance the form of causes across buckets

Tag every cause with its form. Within each domain, every form must appear in all three buckets in roughly equal numbers; plan each domain as a form × bucket grid before writing. Beneficiary group never sets the bucket: causes for children, veterans, farmers or the wealthy exist in every bucket. Do not use evaluative words ("harmful", "predatory", "dubious", "so-called", "wonderful", "vital", "life-saving", "much-needed") or scare quotes; describe what the cause does and let the reader judge.

## Pairs

Among the 90 causes in each domain include 3 minimal pairs (one positive and one harmful cause sharing form and frame, flipped by one or two content words: "research into extracting more geothermal energy" / "research into extracting more fossil fuels") and 2 paraphrase pairs (the same cause in two clearly different wordings, same bucket, same `est_score`). Members share a `pair_id`; `pair_type` is `minimal` or `paraphrase`. Pairs count toward the 30 per cell.

## Style

A cause is a short noun phrase of 3 to 12 words, lowercase except proper nouns, no trailing full stop, reading naturally after "donating to". Abstract, not named: no real organisations, people, companies, brands or countries. Self-contained. Donation-plausible: real people give money to things like this. No duplicates or near-duplicates except the declared pairs.

## Output

`causes.jsonl`, one object per line:

```json
{"id": "environment-harmful-07", "domain": "environment", "valence": "harmful", "est_score": -60, "form": "advocacy", "text": "a coal producers' lobby against tighter limits on power-station emissions", "contested": false, "pair_id": null, "pair_type": null}
```

`checks.md`: (a) a form × bucket table per domain; (b) every word with 20 or more occurrences and its per-bucket counts, sorted by the share of its largest bucket, with the share; (c) counts of the ten restricted harm words per bucket; (d) the pair register; (e) hard domain calls and the rule that decided them; (f) the `est_score` distribution per bucket and the result of the score-pattern check; (g) the final output of your validation script.

## Process

Write each domain's 90 causes first, as naturally as you can, starting from real kinds of organisations and projects. Only then run the checks. If a check fails, rewrite the offending causes as different real causes; never patch a cause by adding or swapping a token. Your validation script must verify: exactly 30 per cell; `est_score` inside its bucket; no duplicates or near-duplicates; every form at least 3 times per cell; the 65% vocabulary rule for words with 20 or more occurrences; the restricted harm words at most 3 per domain's harmful cell; the filler adjectives absent; no two-word opening above 4%; every pair has exactly two members; no two cells share an ordered score sequence and no length-6 score pattern repeats within a cell. Include its final output in `checks.md`.
