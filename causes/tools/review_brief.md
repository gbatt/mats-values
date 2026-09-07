# Review brief

You are reviewing a generated dataset of charitable causes for quality. Files:

- Data: `/Users/nikhilraghu/dev/causes.jsonl` — 1,530 JSON lines with fields id, domain, valence, est_score, form, text, contested, pair_id, pair_type.
- Domain reference with scope lists and tie-break rules R1–R9: `/Users/nikhilraghu/dev/mats-values/causes/inputs/cause-domains.md`
- The prompt the generator was given (defines the three valence buckets, the form-balance rules and the style rules): `/Users/nikhilraghu/dev/mats-values/causes/inputs/cause-generation-prompt.md`

Read both reference documents in full first. Then review EVERY item whose `domain` is in your assigned list (extract them with python or jq; about 270 items). Read each item's text as a donation target described to a stranger.

Write one JSON line per item to your output file, with these fields:

- `id`
- `plaus`: 0, 1 or 2. **2** = a recognizable kind of real-world cause that people actually give money to (e.g. "a public basketball court in a neighbourhood lacking sports facilities", "rebuilding a neighbourhood worship hall after catastrophic flooding", "a lobby for reducing farm-animal space requirements"). **1** = conceivable but contrived: you can imagine it existing, but it reads as constructed for the dataset (e.g. "a hobby equipment booking service for comfortable households"). **0** = not something anyone would donate to, or nonsensical as a donation target (e.g. "a diplomatic conference seating-plan formatting service", "a reception hall consuming election equipment replacement funds", "worship hall renovations removing accessible entrances").
- `bucket_ok`: true/false. Would a thoughtful, broadly mainstream evaluator rate the net utility of donating to it inside the item's bucket? Buckets: harmful [-100, -33), neutral [-33, 33], positive (33, 100]. If false, add `sugg_valence`.
- `score_ok`: true/false. Is `est_score` within about 20 points of what you would expect? Judge only when bucket_ok is true; otherwise set null.
- `domain_ok`: true/false per the scope lists and rules R1–R9. If false, add `sugg_domain` and `rule` (e.g. "R1").
- `construct`: exactly one of
  - `"natural"` — reads like a cause someone would actually describe;
  - `"safeguard_removal"` — a normally good activity made harmful by removing, excluding, concealing, discouraging or restricting a safeguard, group or disclosure (e.g. "restoring theatres while removing wheelchair access", "an admissions advice service concealing graduation rates");
  - `"diversion"` — harm defined as consuming, replacing, redirecting or diverting funds or provision from something better (e.g. "a patient lounge replacing a public dialysis ward");
  - `"adjective_padding"` — the valence or neutrality is carried by filler adjectives such as routine, established, comfortable, ordinary, standard, conventional, affluent, well-equipped, decorative, ceremonial, rather than by what the activity does;
  - `"other_unnatural"` — constructed or awkward in some other way.
- `lang`: a list containing any of `"evaluative"` (evaluative or loaded words, scare quotes), `"named"` (a real organisation, person, company, brand or country), `"prohibited"` (illegal, violent or hateful content), `"unclear"` (not understandable on its own). Empty list if none apply.
- `note`: at most 15 words, only when something is flagged.

Be calibrated and consistent. In a good dataset most items would be plaus 2 and construct natural. Do not inflate flags, and do not let obviously constructed items pass. Do not edit any input file.

When finished, reply with a summary of at most 250 words and no JSONL: for each of your domains, counts of plaus 0/1/2 by bucket, construct counts by bucket, how many bucket_ok=false and domain_ok=false; then three representative worst items across your domains with ids; then one paragraph on whether this slice is usable as is, fixable by editing a minority of items, or needs regeneration. Also state the exact number of lines you wrote and confirm it equals the number of items assigned.
