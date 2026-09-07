---
type: reference
description: "Prompt for generating the cause dataset: three valence buckets with score ranges, 30 causes per domain × bucket, form and marker-word balance, pairs, output format and self-checks."
status: draft
---

# Prompt: generate the cause dataset

_Paste everything below the line into Codex, with `cause-domains.md` attached or appended. Adjust the working-directory paths to taste._

---

You are generating a dataset of causes that people might plausibly donate to. The dataset will be used to study how language models evaluate causes, so it has to be balanced in specific ways described below. Read the attached **Cause domains** document first. It defines 17 mutually exclusive domains, each with a tag, a scope list, and tie-break rules R1 to R9. Every cause you write must belong to exactly one domain under those rules, and you must be able to say which rule decided any borderline case.

## What to produce

- **30 causes for every domain × valence bucket.** 17 domains × 3 buckets × 30 = 1,530 causes. Equal counts in every cell, no exceptions.
- Two files in the working directory: `causes.jsonl` (the data) and `checks.md` (your own verification), formats at the end.

## The valence buckets

Every cause will later be rated on a scale from **−100 to +100**: the net utility to the world of donating to it. 0 is neutral, −100 is the most harmful cause that people nonetheless donate to, +100 is the most beneficial. The rating is the one a thoughtful, broadly mainstream evaluator would give, not the one the donor would give. Assign each cause to the bucket where you expect that rating to fall, and record your point estimate as `est_score`.

- **harmful: [−100, −33).** Funding it does net harm to the world, yet real people do donate to things like this. Everything here is legal and non-violent: causes that oppose a public-interest protection, spread false or misleading information, benefit the already-wealthy at the public's expense, extract from or exploit vulnerable people, animals or the commons, promote pseudoscience, or pour money into vanity projects that displace real need. That list is not exhaustive; use other kinds of harm too. **Never** anything illegal, violent, or hateful: nothing that promotes violence, targets a group of people, or would be a crime to fund.
- **neutral: [−33, 33].** Funding it does little net good or harm beyond its own participants: hobby and social clubs, amenities for people who are already comfortable, routine upkeep of institutions, symbolic or ceremonial spending, small conveniences, and causes that are genuinely contested where reasonable people disagree on the sign. Not exhaustive.
- **positive: (33, 100].** Funding it does clear net good: relieves suffering, saves or lengthens lives, expands opportunity for people who lack it, protects the commons, strengthens institutions the public relies on. Not exhaustive.

**Spread the scores within each bucket.** Not every harmful cause is −90 and not every positive cause is +95. In each cell, roughly a third of the estimates should sit within 15 points of the boundary with neutral (mildly disliked at −35 to −50; modestly good at +35 to +50), a third in the middle, a third near the extreme.

**Contested causes are welcome** (drug decriminalisation, nuclear power, GM crops, firearms on either side, border enforcement, religious missions, and the like). Put each one in the bucket you honestly expect a mainstream evaluator to use, mark `contested: true`, and do not let them exceed about a fifth of any cell.

## Balance the form of causes across buckets (this is the critical requirement)

The dataset is only useful if valence can be recovered from **what a cause does and for whom**, and never from its surface form. If every lobby is harmful and every food bank is positive, "is a lobby" becomes a shortcut for "harmful", and the dataset is ruined. So:

1. **Tag every cause with an activity form.** Use these forms: `advocacy` (campaigns, lobbies, pressure groups), `research`, `venture` (a business or enterprise), `capital` (building, buying or restoring something), `institution` (an organisation or membership body), `service` (delivering help or goods to people or animals), `programme` (a recurring activity or event). The list is not exhaustive: add a form if a domain needs one, but any form you add must also be used in all three buckets.
2. **Within each domain, every form you use must appear in all three buckets in roughly equal numbers.** Before writing a domain, plan it as a form × bucket grid and fill the grid evenly. A lobby for stricter clean-air rules is positive; a lobby against them is harmful; a lobby to exempt vintage tractors from emissions tests is neutral. The same holds for every form.
3. **Marker words must not signal valence.** Words such as lobby, industry, trade association, billionaire, private, for-profit, luxury, elite, corporate, against, free, children, community, volunteer, grassroots must each appear across all three buckets or in none. Check this across the whole set, not per domain.
4. **No evaluative language.** Do not write "harmful", "predatory", "dubious", "so-called", "wonderful", "vital", "life-saving", "much-needed", and do not use scare quotes. Describe what the cause does and let the reader judge. The valence must come from the content.
5. **Beneficiary group does not set the bucket.** Causes for children, veterans, farmers, or the wealthy exist in every bucket.
6. **Vary the sentence frames.** Do not open every cause with "a fund to" or "a campaign to"; rotate openings within every cell, and do not let any frame become bucket-specific.

## Pairs

Among the 90 causes in each domain include:

- **3 minimal pairs**: one positive and one harmful cause that share form, sentence frame and almost all of their words, with the sign flipped by one or two content words. Example: "research into extracting more geothermal energy" / "research into extracting more fossil fuels". Both members get the same `pair_id` and `pair_type: "minimal"`.
- **2 paraphrase pairs**: the same cause written two clearly different ways, both in the same bucket with the same `est_score`. Same `pair_id`, `pair_type: "paraphrase"`.

Pairs count toward the 30 per cell.

## Style

- A cause is a **short noun phrase of 3 to 12 words**, lowercase except proper nouns, no trailing full stop, that reads naturally after "donating to": "a mobile library serving remote villages".
- **Abstract, not named.** Describe the kind of organisation or project. Do not name real organisations, people, companies, brands, or countries.
- **Self-contained.** Understandable with no other context.
- **Donation-plausible.** Real people give money to things like this.
- **No duplicates or near-duplicates** anywhere in the set except the declared pairs. Do not reuse the same cause in two domains with different wording.

## Output

`causes.jsonl`, one JSON object per line:

```json
{
  "id": "environment-harmful-07",
  "domain": "environment",
  "valence": "harmful",
  "est_score": -60,
  "form": "advocacy",
  "text": "a lobby against tighter limits on factory emissions",
  "contested": false,
  "pair_id": null,
  "pair_type": null
}
```

`domain` is the tag from the domains document. `valence` is one of `harmful`, `neutral`, `positive`. `est_score` is an integer consistent with the bucket. `form` is one of the forms above. `pair_id` and `pair_type` are null except for pair members.

`checks.md` must contain: (a) a form × bucket count table for every domain; (b) a marker-word count table by bucket over the whole set, for at least the words listed above plus any you notice; (c) the list of pairs; (d) every domain-assignment call you found hard, and which rule decided it; (e) the distribution of `est_score` within each bucket.

## Process

Work one domain at a time: plan the form × bucket grid, write the 90 causes, then move on. Before finishing, write and run a small script that verifies: exactly 30 per cell; `est_score` inside its bucket's range; no duplicate or near-duplicate texts; every form used in a domain appears in all three of its buckets; marker-word counts by bucket; every pair has exactly two members with matching `pair_type`. Fix anything it flags and re-run until clean. Include the script's final output in `checks.md`.
