# Prompt: round 2 (sent in the same thread as round 1; no context repeated)

Round 2. Your set passed every count check and failed review: most harmful and neutral causes were built to satisfy the checks rather than to name real causes, and part of that was our rules pushing valence out of the cause and into a clause about what it does. Regenerate under the rules below. Same domains, buckets, score ranges, output files and fields.

## The unit is a kind of cause

- 18 causes per domain × bucket, 918 in total, equal counts in every cell.
- 2 to 7 words. Each cause names a kind of organisation or project a donor would recognise: a homeopathy clinic, a food bank, a golf club's new greens, a coal producers' lobby, cancer research, a payday-lender trade association, microfinance for women entrepreneurs, a model-railway society. Valence lives in what the thing is, or in one adjective of kind, never in a verb clause about what it does. Out: "a veteran storytelling programme preserving disappearing oral traditions". In: "an oral-history archive for veterans".
- A harmful cause is harmful because of what it is, described the way its own supporters would describe it. Nothing that is a crime to fund.
- A neutral cause is neutral because the kind has little consequence beyond its participants.
- Every word must be load-bearing for the kind: if deleting a word leaves the same kind of cause, delete it. Each cause should read like an entry in a charity register. Words that never survive this test, and are banned outright in every bucket: routine, established, comfortable, ordinary, standard, conventional, affluent, well-equipped, decorative, ceremonial. The list is not exhaustive; the test is the rule.
- One cause per kind: no kind reworded twice, and no kind in two domains. Sharing a frame is fine: "a lobby for EV subsidies" and "a lobby for nuclear subsidies" are different kinds.

## Balance

- No word with 12 or more occurrences in the set may have more than 65% of them in one bucket. Meet this by choosing different kinds; planting a word in other buckets is forbidden.
- All seven forms (advocacy, research, venture, capital, institution, service, programme) appear at least once in every cell, and across the set no form has more than 45% of its causes in one bucket.
- Score each cause on its own merits after writing it, with roughly a third of each cell within 15 points of the neutral boundary. A repeated ordered score sequence across cells, or a repeating pattern within a cell, fails validation.

## Pairs

- Minimal pair: two causes in different buckets differing by one or two words ("a lobby for coal subsidies" / "a lobby for solar subsidies"). At least 3 per domain, no maximum, each using a different frame. Declare every one with a shared pair_id and pair_type "minimal".
- Paraphrase pair: the same kind in two clearly different wordings, same bucket, same est_score. 2 per domain, pair_type "paraphrase".
- Pairs count within the 18 per cell.

Round-1 causes that satisfy every rule above may be kept; list them in checks.md.

## Process

Write each domain's 54 causes as a list of kinds, then run the checks. If a check fails, replace causes with different kinds rather than editing words. The validator must check: 18 per cell; 2 to 7 words; the 65% vocabulary rule; the banned adjectives absent; every form present in every cell and the 45% cap; the score-sequence rule; every pair has exactly two members. In checks.md include the per-bucket table of every word with 12 or more occurrences sorted by largest-bucket share, the form × bucket table per domain and overall, the round-1 causes kept, and the validator's final output.
