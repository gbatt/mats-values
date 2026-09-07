# Round 2 verification

918 causes; 17 domains × 3 buckets × 18 entries. The working-directory deliverables are `causes.jsonl` and this file. Identical downloadable copies are in `outputs/`.

The classification reference is the updated `/Users/nikhilraghu/dev/mats-values/causes/inputs/cause-domains.md`, including the revised R1, R3 and R6. It was used as reference material; task instructions came from the user. The earlier domain document was superseded.

Source SHA256: `3f8666523684174fe7caaba893a98cfc7623caeedaa25eaaa4e6c6586a5268ff`

Dataset SHA256: `4782a198124f2cc7a902065d7209f4bd9bce702aa7bd0c4e2494564450f5cbd1`

## Applicable rules and construction

The four withdrawn Round-1 constraints were not applied: there is no all-buckets-or-none marker rule, no equal per-domain form grid, no 3–12-word allowance, and no Jaccard or generic near-duplicate threshold. Shared frames are permitted. The checks instead enforce the Round-2 vocabulary concentration limit, seven-form coverage and global cap, 2–7 words, and declared small-edit pairs.

Each domain was drafted as 54 cause kinds before proceeding to the next. The builder checked its 18-entry cells and seven-form coverage. Scores were attached to the individual kinds, not generated from form or position. Full-set checks then prompted replacements of kinds, including vocabulary-heavy entries and kinds colliding with more than one minimal pair.

The final within-cell order is independent of both score and form: kinds are sorted by SHA256 of `round2-kind-order-v1` followed by a NUL byte and their text. IDs are assigned after that ordering. Scoring therefore remains attached to a kind when it moves. No score sequence or repeated numeric block was used as a template.

The editorial review checked recognisable organisation/project kinds, short noun-phrase wording, supporter-style descriptions, load-bearing modifiers, domain membership, and distinct underlying kinds. Topics may recur through substantively different funded activities—such as research versus clinical provision—but a rewording of the same kind is allowed only as a declared paraphrase. Types requiring violence, hateful targeting, or credential fraud were removed. Regulated activities refer to lawful, nonviolent versions.

The scores and contested flags are editorial estimates of mainstream evaluation, not independently collected ratings. Neither exact vocabulary balance nor a lexical pair check establishes the semantic quality of a dataset by itself.

## Round-1 causes kept

None. Zero final texts exactly match Round 1. The earlier deliverables are preserved in `work/round1-causes.jsonl` and `work/round1-checks.md`. Familiar subjects recur, but no Round-1 record was carried forward verbatim.

## Form × bucket counts

### Overall

| Form | harmful | neutral | positive | Total | Largest-bucket share |
|---|---:|---:|---:|---:|---:|
| advocacy | 45 | 21 | 34 | 100 | 45.00% |
| research | 41 | 35 | 35 | 111 | 36.94% |
| venture | 37 | 34 | 33 | 104 | 35.58% |
| capital | 33 | 37 | 36 | 106 | 34.91% |
| institution | 45 | 42 | 35 | 122 | 36.89% |
| service | 46 | 63 | 64 | 173 | 36.99% |
| programme | 59 | 74 | 69 | 202 | 36.63% |
| **Total** | **306** | **306** | **306** | **918** | **33.33%** |

### arts

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 4 | 2 | 3 |
| research | 2 | 1 | 2 |
| venture | 3 | 2 | 1 |
| capital | 1 | 3 | 2 |
| institution | 3 | 3 | 3 |
| service | 1 | 3 | 3 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### education

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 2 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 3 | 2 |
| institution | 4 | 2 | 3 |
| service | 2 | 3 | 3 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### environment

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 2 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 3 | 2 |
| institution | 3 | 3 | 3 |
| service | 2 | 3 | 3 |
| programme | 4 | 3 | 4 |
| **Total** | **18** | **18** | **18** |

### animals

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 1 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 2 | 4 | 4 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### physical_health

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 1 | 1 | 2 |
| research | 2 | 2 | 2 |
| venture | 3 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 3 | 4 | 4 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### mental_health

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 1 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 3 | 4 | 4 |
| programme | 4 | 4 | 5 |
| **Total** | **18** | **18** | **18** |

### science

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 2 |
| research | 3 | 3 | 3 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 2 | 2 |
| service | 3 | 3 | 4 |
| programme | 3 | 5 | 3 |
| **Total** | **18** | **18** | **18** |

### media

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 2 |
| research | 3 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 3 | 4 | 4 |
| programme | 3 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### safety

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 2 |
| research | 3 | 3 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 2 | 2 | 2 |
| service | 3 | 4 | 4 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### justice

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 1 | 2 |
| research | 3 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 2 | 2 | 2 |
| service | 3 | 4 | 4 |
| programme | 3 | 5 | 4 |
| **Total** | **18** | **18** | **18** |

### politics

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 2 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 2 | 2 | 2 |
| service | 4 | 4 | 4 |
| programme | 3 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### agriculture

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 1 | 2 |
| research | 3 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 2 | 2 | 2 |
| service | 3 | 4 | 4 |
| programme | 3 | 5 | 4 |
| **Total** | **18** | **18** | **18** |

### economy

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 2 |
| research | 3 | 2 | 2 |
| venture | 3 | 2 | 2 |
| capital | 2 | 2 | 3 |
| institution | 2 | 2 | 1 |
| service | 3 | 4 | 4 |
| programme | 3 | 5 | 4 |
| **Total** | **18** | **18** | **18** |

### religion

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 2 | 1 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 3 | 4 | 4 |
| programme | 4 | 4 | 4 |
| **Total** | **18** | **18** | **18** |

### sports

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 1 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 3 |
| institution | 2 | 2 | 1 |
| service | 3 | 4 | 4 |
| programme | 4 | 5 | 4 |
| **Total** | **18** | **18** | **18** |

### social

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 5 | 1 | 2 |
| research | 2 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 3 | 3 | 2 |
| service | 2 | 3 | 4 |
| programme | 2 | 5 | 4 |
| **Total** | **18** | **18** | **18** |

### international

| Form | harmful | neutral | positive |
|---|---:|---:|---:|
| advocacy | 3 | 1 | 2 |
| research | 3 | 2 | 2 |
| venture | 2 | 2 | 2 |
| capital | 2 | 2 | 2 |
| institution | 2 | 2 | 2 |
| service | 3 | 4 | 3 |
| programme | 3 | 5 | 5 |
| **Total** | **18** | **18** | **18** |

## Vocabulary concentration

Only `text` is counted. Matching is case-insensitive; punctuation and possessive suffixes are removed. Hyphenated compounds are words in the primary audit, consistently with the 2–7-word length check. There is no stemming or synonym grouping. Every word occurring at least 12 times is shown, sorted by largest-bucket share, then total count, then word. A second complete audit splits hyphenated compounds; it also passes. No word was inserted into another bucket to satisfy a count.

### Whole-word audit

| Word | harmful | neutral | positive | Total | Largest-bucket share |
|---|---:|---:|---:|---:|---:|
| studies | 3 | 13 | 4 | 20 | 65.00% |
| for | 1 | 4 | 9 | 14 | 64.29% |
| institute | 11 | 1 | 7 | 19 | 57.89% |
| association | 13 | 11 | 0 | 24 | 54.17% |
| company | 5 | 2 | 8 | 15 | 53.33% |
| service | 0 | 13 | 12 | 25 | 52.00% |
| advocacy | 15 | 7 | 22 | 44 | 50.00% |
| school | 4 | 3 | 7 | 14 | 50.00% |
| laboratory | 4 | 3 | 6 | 13 | 46.15% |
| an | 19 | 9 | 22 | 50 | 44.00% |
| centre | 5 | 3 | 4 | 12 | 41.67% |
| business | 9 | 9 | 4 | 22 | 40.91% |
| research | 35 | 19 | 33 | 87 | 40.23% |
| a | 98 | 118 | 95 | 311 | 37.94% |
| workshops | 4 | 4 | 4 | 12 | 33.33% |

### Hyphen-component audit

| Word | harmful | neutral | positive | Total | Largest-bucket share |
|---|---:|---:|---:|---:|---:|
| studies | 3 | 13 | 4 | 20 | 65.00% |
| for | 1 | 4 | 9 | 14 | 64.29% |
| institute | 11 | 1 | 7 | 19 | 57.89% |
| school | 4 | 3 | 9 | 16 | 56.25% |
| association | 13 | 11 | 0 | 24 | 54.17% |
| service | 0 | 14 | 12 | 26 | 53.85% |
| company | 5 | 2 | 8 | 15 | 53.33% |
| advocacy | 15 | 7 | 22 | 44 | 50.00% |
| laboratory | 4 | 3 | 6 | 13 | 46.15% |
| an | 19 | 9 | 22 | 50 | 44.00% |
| business | 9 | 10 | 5 | 24 | 41.67% |
| research | 35 | 19 | 33 | 87 | 40.23% |
| centre | 5 | 4 | 4 | 13 | 38.46% |
| a | 98 | 118 | 95 | 311 | 37.94% |
| workshops | 4 | 4 | 4 | 12 | 33.33% |

## Score checks

The non-neutral near-boundary band is defined numerically: 34–48 and −48…−34, inclusive, each at most 15 points from +33 or −33. Each harmful/positive cell contains five to seven such estimates, approximately one third. Neutral scores are reported on their own merits; neutral has no boundary separating it from the neutral category itself. No quota of extreme scores was imposed.

| Bucket | Count | Minimum | Maximum | Mean | Median |
|---|---:|---:|---:|---:|---:|
| harmful | 306 | -85 | -38 | -57.59 | -57.5 |
| neutral | 306 | -8 | 31 | 16.63 | 17.0 |
| positive | 306 | 40 | 94 | 65.53 | 68.0 |

| Domain | Harmful within 15 of −33 | Positive within 15 of +33 | Contested H / N / P |
|---|---:|---:|---|
| arts | 5 | 6 | 4 / 0 / 2 |
| education | 5 | 5 | 3 / 1 / 0 |
| environment | 5 | 5 | 4 / 0 / 1 |
| animals | 5 | 5 | 2 / 0 / 1 |
| physical_health | 6 | 5 | 2 / 1 / 0 |
| mental_health | 5 | 5 | 4 / 0 / 1 |
| science | 7 | 6 | 3 / 0 / 2 |
| media | 5 | 5 | 2 / 1 / 0 |
| safety | 6 | 5 | 4 / 1 / 0 |
| justice | 5 | 6 | 4 / 0 / 2 |
| politics | 5 | 6 | 3 / 1 / 1 |
| agriculture | 5 | 6 | 4 / 0 / 1 |
| economy | 5 | 5 | 3 / 0 / 1 |
| religion | 5 | 5 | 4 / 0 / 4 |
| sports | 5 | 5 | 4 / 1 / 0 |
| social | 6 | 5 | 4 / 0 / 2 |
| international | 5 | 5 | 4 / 0 / 1 |

### Exact score distribution

| Score | harmful | neutral | positive |
|---:|---:|---:|---:|
| -85 | 2 | 0 | 0 |
| -84 | 2 | 0 | 0 |
| -82 | 1 | 0 | 0 |
| -81 | 4 | 0 | 0 |
| -79 | 5 | 0 | 0 |
| -78 | 2 | 0 | 0 |
| -77 | 1 | 0 | 0 |
| -76 | 5 | 0 | 0 |
| -75 | 2 | 0 | 0 |
| -74 | 4 | 0 | 0 |
| -73 | 6 | 0 | 0 |
| -72 | 3 | 0 | 0 |
| -71 | 7 | 0 | 0 |
| -70 | 6 | 0 | 0 |
| -69 | 6 | 0 | 0 |
| -68 | 6 | 0 | 0 |
| -67 | 10 | 0 | 0 |
| -66 | 7 | 0 | 0 |
| -65 | 4 | 0 | 0 |
| -64 | 12 | 0 | 0 |
| -63 | 9 | 0 | 0 |
| -62 | 13 | 0 | 0 |
| -61 | 11 | 0 | 0 |
| -60 | 5 | 0 | 0 |
| -59 | 7 | 0 | 0 |
| -58 | 13 | 0 | 0 |
| -57 | 13 | 0 | 0 |
| -56 | 10 | 0 | 0 |
| -55 | 8 | 0 | 0 |
| -54 | 9 | 0 | 0 |
| -53 | 6 | 0 | 0 |
| -52 | 5 | 0 | 0 |
| -51 | 1 | 0 | 0 |
| -49 | 11 | 0 | 0 |
| -48 | 12 | 0 | 0 |
| -47 | 11 | 0 | 0 |
| -46 | 9 | 0 | 0 |
| -45 | 12 | 0 | 0 |
| -44 | 6 | 0 | 0 |
| -43 | 14 | 0 | 0 |
| -42 | 8 | 0 | 0 |
| -41 | 7 | 0 | 0 |
| -40 | 3 | 0 | 0 |
| -39 | 7 | 0 | 0 |
| -38 | 1 | 0 | 0 |
| -8 | 0 | 1 | 0 |
| 0 | 0 | 2 | 0 |
| 1 | 0 | 3 | 0 |
| 2 | 0 | 6 | 0 |
| 3 | 0 | 6 | 0 |
| 4 | 0 | 10 | 0 |
| 5 | 0 | 6 | 0 |
| 6 | 0 | 6 | 0 |
| 7 | 0 | 6 | 0 |
| 8 | 0 | 16 | 0 |
| 9 | 0 | 13 | 0 |
| 10 | 0 | 5 | 0 |
| 11 | 0 | 6 | 0 |
| 12 | 0 | 16 | 0 |
| 13 | 0 | 6 | 0 |
| 14 | 0 | 11 | 0 |
| 15 | 0 | 7 | 0 |
| 16 | 0 | 14 | 0 |
| 17 | 0 | 14 | 0 |
| 18 | 0 | 15 | 0 |
| 19 | 0 | 16 | 0 |
| 20 | 0 | 11 | 0 |
| 21 | 0 | 10 | 0 |
| 22 | 0 | 12 | 0 |
| 23 | 0 | 9 | 0 |
| 24 | 0 | 20 | 0 |
| 25 | 0 | 11 | 0 |
| 26 | 0 | 12 | 0 |
| 27 | 0 | 12 | 0 |
| 28 | 0 | 10 | 0 |
| 29 | 0 | 5 | 0 |
| 30 | 0 | 5 | 0 |
| 31 | 0 | 4 | 0 |
| 40 | 0 | 0 | 4 |
| 41 | 0 | 0 | 2 |
| 42 | 0 | 0 | 9 |
| 43 | 0 | 0 | 7 |
| 44 | 0 | 0 | 11 |
| 45 | 0 | 0 | 10 |
| 46 | 0 | 0 | 16 |
| 47 | 0 | 0 | 14 |
| 48 | 0 | 0 | 17 |
| 49 | 0 | 0 | 12 |
| 51 | 0 | 0 | 2 |
| 56 | 0 | 0 | 1 |
| 57 | 0 | 0 | 3 |
| 58 | 0 | 0 | 2 |
| 59 | 0 | 0 | 1 |
| 60 | 0 | 0 | 5 |
| 61 | 0 | 0 | 1 |
| 62 | 0 | 0 | 5 |
| 63 | 0 | 0 | 2 |
| 64 | 0 | 0 | 5 |
| 65 | 0 | 0 | 4 |
| 66 | 0 | 0 | 7 |
| 67 | 0 | 0 | 4 |
| 68 | 0 | 0 | 11 |
| 69 | 0 | 0 | 5 |
| 70 | 0 | 0 | 7 |
| 71 | 0 | 0 | 4 |
| 72 | 0 | 0 | 9 |
| 73 | 0 | 0 | 7 |
| 74 | 0 | 0 | 7 |
| 75 | 0 | 0 | 9 |
| 76 | 0 | 0 | 7 |
| 77 | 0 | 0 | 6 |
| 78 | 0 | 0 | 8 |
| 79 | 0 | 0 | 9 |
| 80 | 0 | 0 | 8 |
| 81 | 0 | 0 | 4 |
| 82 | 0 | 0 | 6 |
| 83 | 0 | 0 | 10 |
| 84 | 0 | 0 | 6 |
| 85 | 0 | 0 | 3 |
| 86 | 0 | 0 | 8 |
| 87 | 0 | 0 | 5 |
| 88 | 0 | 0 | 7 |
| 89 | 0 | 0 | 3 |
| 90 | 0 | 0 | 2 |
| 91 | 0 | 0 | 7 |
| 92 | 0 | 0 | 2 |
| 94 | 0 | 0 | 2 |

## Pair register

There are 101 minimal pairs and 34 paraphrase pairs. Every pair has exactly two members in one domain and one form. Every domain has at least three minimal pairs and exactly two paraphrase pairs. Minimal pairs have different buckets and a token edit distance of one or two; all detected additional within-domain, same-form small-edit contrasts are declared. Their common-word frames are distinct within each domain. Paraphrases have the same bucket and score, with at least three token edits between their wordings.

### arts

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| arts-m1 | minimal / advocacy | `arts-harmful-02` — antiquities export deregulation (harmful, -48) | `arts-positive-11` — antiquities export regulation (positive, 44) |
| arts-m2 | minimal / venture | `arts-neutral-04` — a commercial music tuition studio (neutral, 11) | `arts-positive-03` — a subsidised music tuition studio (positive, 42) |
| arts-m3 | minimal / capital | `arts-neutral-16` — a private sculpture garden (neutral, 15) | `arts-positive-13` — a tactile sculpture garden (positive, 40) |
| arts-m4 | minimal / advocacy | `arts-harmful-18` — theatre censorship advocacy (harmful, -69) | `arts-positive-05` — arts accessibility advocacy (positive, 46) |
| arts-m5 | minimal / research | `arts-harmful-01` — pyramid numerology research (harmful, -53) | `arts-positive-15` — endangered-language revitalisation research (positive, 76) |
| arts-q1 | paraphrase / institution | `arts-neutral-06` — a calligraphy society (neutral, 9) | `arts-neutral-14` — a fellowship of handwriting artists (neutral, 9) |
| arts-q2 | paraphrase / service | `arts-positive-14` — theatre audio description (positive, 57) | `arts-positive-17` — spoken stage descriptions for blind audiences (positive, 57) |

### education

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| education-m1 | minimal / institution | `education-harmful-12` — a homeopathy college (harmful, -64) | `education-positive-18` — a midwifery college (positive, 71) |
| education-m2 | minimal / programme | `education-harmful-14` — astrology degree scholarships (harmful, -46) | `education-neutral-07` — gemmology degree scholarships (neutral, 27) |
| education-m3 | minimal / capital | `education-neutral-18` — a school squash court (neutral, 8) | `education-positive-12` — a school sanitation block (positive, 87) |
| education-m4 | minimal / advocacy | `education-harmful-10` — school inspection abolition (harmful, -67) | `education-positive-09` — school desegregation campaigns (positive, 62) |
| education-m5 | minimal / research | `education-harmful-04` — learning-styles instruction research (harmful, -42) | `education-positive-11` — multilingual literacy instruction research (positive, 64) |
| education-m6 | minimal / venture | `education-harmful-05` — a graphology tutoring business (harmful, -52) | `education-neutral-16` — a language tutoring agency (neutral, 20) |
| education-m7 | minimal / institution | `education-harmful-18` — a graphology certification school (harmful, -57) | `education-positive-17` — a refugee secondary school (positive, 86) |
| education-m8 | minimal / institution | `education-harmful-11` — a geocentric astronomy academy (harmful, -59) | `education-positive-14` — a deaf children's academy (positive, 49) |
| education-q1 | paraphrase / institution | `education-neutral-05` — a college of dental laboratory technology (neutral, 24) | `education-neutral-11` — a dental laboratory technician college (neutral, 24) |
| education-q2 | paraphrase / programme | `education-positive-01` — tuition awards to trainee village midwives (positive, 77) | `education-positive-02` — rural midwifery student scholarships (positive, 77) |

### environment

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| environment-m1 | minimal / advocacy | `environment-harmful-03` — a lobby for coal subsidies (harmful, -73) | `environment-positive-10` — a lobby for solar subsidies (positive, 76) |
| environment-m2 | minimal / capital | `environment-harmful-13` — a waste incinerator expansion (harmful, -47) | `environment-positive-01` — a waste recycling expansion (positive, 44) |
| environment-m3 | minimal / programme | `environment-neutral-10` — suburban tree inventories (neutral, 16) | `environment-positive-06` — endangered tree inventories (positive, 46) |
| environment-m4 | minimal / venture | `environment-harmful-12` — a peat extraction company (harmful, -62) | `environment-positive-12` — a battery recycling company (positive, 63) |
| environment-m5 | minimal / research | `environment-harmful-14` — tar-sands extraction research (harmful, -79) | `environment-positive-13` — low-carbon cement research (positive, 83) |
| environment-m6 | minimal / advocacy | `environment-harmful-17` — offshore drilling advocacy (harmful, -63) | `environment-positive-09` — clean-air standards advocacy (positive, 78) |
| environment-m7 | minimal / institution | `environment-harmful-08` — a fossil-fuel promotion institute (harmful, -60) | `environment-positive-15` — a geological carbon-storage institute (positive, 47) |
| environment-q1 | paraphrase / institution | `environment-neutral-03` — a kitchen-waste composting club (neutral, 8) | `environment-neutral-08` — a neighbourhood network of food-scrap composters (neutral, 8) |
| environment-q2 | paraphrase / service | `environment-positive-02` — household insulation upgrades (positive, 72) | `environment-positive-11` — home energy retrofits (positive, 72) |

### animals

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| animals-m1 | minimal / advocacy | `animals-harmful-05` — battery-cage farming advocacy (harmful, -69) | `animals-positive-04` — battery-cage farming opposition (positive, 72) |
| animals-m2 | minimal / service | `animals-neutral-14` — a pet boarding service (neutral, 16) | `animals-positive-09` — a pet neutering service (positive, 65) |
| animals-m3 | minimal / capital | `animals-neutral-12` — a shelter's visitor lounge (neutral, 6) | `animals-positive-17` — a shelter's veterinary ward (positive, 78) |
| animals-m4 | minimal / service | `animals-harmful-18` — homeopathic veterinary consultations (harmful, -56) | `animals-positive-01` — emergency veterinary transport (positive, 56) |
| animals-m5 | minimal / institution | `animals-harmful-14` — a captive-animal exhibitors' association (harmful, -64) | `animals-neutral-07` — a dog owners' association (neutral, 17) |
| animals-m6 | minimal / service | `animals-harmful-02` — animal aura readings (harmful, -42) | `animals-neutral-18` — animal memorial services (neutral, 4) |
| animals-m7 | minimal / programme | `animals-neutral-09` — pedigree cat shows (neutral, 3) | `animals-positive-06` — feral cat sterilisation (positive, 77) |
| animals-q1 | paraphrase / institution | `animals-neutral-01` — a membership group for aquarium hobbyists (neutral, 12) | `animals-neutral-03` — an aquarium keepers' society (neutral, 12) |
| animals-q2 | paraphrase / programme | `animals-positive-08` — temporary homes for abandoned dogs (positive, 70) | `animals-positive-12` — shelter dog fostering (positive, 70) |

### physical_health

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| physical_health-m1 | minimal / institution | `physical_health-harmful-10` — a homeopathy clinic (harmful, -62) | `physical_health-positive-04` — a tuberculosis clinic (positive, 91) |
| physical_health-m2 | minimal / capital | `physical_health-neutral-12` — a hospital visitor lounge (neutral, 3) | `physical_health-positive-03` — a hospital neonatal ward (positive, 90) |
| physical_health-m3 | minimal / programme | `physical_health-neutral-04` — cosmetic skincare workshops (neutral, 12) | `physical_health-positive-16` — diabetic footcare workshops (positive, 48) |
| physical_health-m4 | minimal / research | `physical_health-harmful-16` — coffee-enema cancer research (harmful, -79) | `physical_health-positive-06` — drug-resistant malaria research (positive, 88) |
| physical_health-m5 | minimal / venture | `physical_health-harmful-14` — a detox foot-pad company (harmful, -45) | `physical_health-positive-09` — a low-cost hearing-aid company (positive, 46) |
| physical_health-m6 | minimal / venture | `physical_health-harmful-05` — a nosode manufacturer (harmful, -58) | `physical_health-positive-07` — a generic insulin manufacturer (positive, 84) |
| physical_health-m7 | minimal / institution | `physical_health-harmful-18` — a faith-healing medical association (harmful, -70) | `physical_health-neutral-10` — a dental professionals' association (neutral, 18) |
| physical_health-q1 | paraphrase / institution | `physical_health-neutral-08` — a practice for hair transplantation (neutral, 8) | `physical_health-neutral-15` — a hair transplantation centre (neutral, 8) |
| physical_health-q2 | paraphrase / service | `physical_health-positive-02` — maternal syphilis detection during pregnancy (positive, 94) | `physical_health-positive-12` — prenatal syphilis screening (positive, 94) |

### mental_health

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| mental_health-m1 | minimal / institution | `mental_health-harmful-12` — an abstinence-only opioid clinic (harmful, -65) | `mental_health-positive-18` — a medication-assisted opioid clinic (positive, 86) |
| mental_health-m2 | minimal / programme | `mental_health-neutral-01` — corporate mindfulness retreats (neutral, 8) | `mental_health-positive-12` — trauma-informed mindfulness retreats (positive, 46) |
| mental_health-m3 | minimal / service | `mental_health-neutral-08` — a relaxation coaching service (neutral, 16) | `mental_health-positive-15` — a crisis counselling service (positive, 88) |
| mental_health-m4 | minimal / venture | `mental_health-harmful-14` — a subliminal addiction-cure app (harmful, -49) | `mental_health-neutral-14` — a mood journaling app (neutral, 25) |
| mental_health-m5 | minimal / advocacy | `mental_health-harmful-18` — addiction medication prohibition advocacy (harmful, -84) | `mental_health-positive-04` — addiction treatment access advocacy (positive, 49) |
| mental_health-m6 | minimal / capital | `mental_health-harmful-03` — a primal-scream therapy centre (harmful, -47) | `mental_health-positive-05` — a community crisis centre (positive, 78) |
| mental_health-q1 | paraphrase / institution | `mental_health-neutral-02` — a workplace stress support circle (neutral, 14) | `mental_health-neutral-12` — an employee wellbeing discussion group (neutral, 14) |
| mental_health-q2 | paraphrase / programme | `mental_health-positive-11` — peer meetings for compulsive gamblers (positive, 70) | `mental_health-positive-13` — gambling addiction support groups (positive, 70) |

### science

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| science-m1 | minimal / institution | `science-harmful-06` — a flat-earth research institute (harmful, -64) | `science-neutral-17` — a radio astronomy institute (neutral, 28) |
| science-m2 | minimal / capital | `science-neutral-16` — a hobby robotics laboratory (neutral, 21) | `science-positive-12` — a biosafety research laboratory (positive, 78) |
| science-m3 | minimal / service | `science-neutral-09` — a mineral identification service (neutral, 26) | `science-positive-18` — a structural integrity service (positive, 75) |
| science-m4 | minimal / research | `science-harmful-18` — perpetual-motion engine research (harmful, -68) | `science-positive-09` — reproducibility infrastructure research (positive, 77) |
| science-m5 | minimal / venture | `science-harmful-13` — a perpetual-energy generator startup (harmful, -71) | `science-positive-16` — a laboratory automation startup (positive, 41) |
| science-m6 | minimal / capital | `science-harmful-04` — a geocentric planetarium (harmful, -57) | `science-neutral-03` — a university planetarium projector (neutral, 7) |
| science-m7 | minimal / advocacy | `science-harmful-01` — AI safety testing deregulation (harmful, -73) | `science-positive-15` — AI safety standards advocacy (positive, 71) |
| science-m8 | minimal / research | `science-neutral-12` — historical slide-rule engineering studies (neutral, 9) | `science-positive-17` — antimicrobial surface engineering studies (positive, 66) |
| science-q1 | paraphrase / programme | `science-neutral-08` — beginner microscopy classes (neutral, 19) | `science-neutral-18` — introductory lessons in microscopic observation (neutral, 19) |
| science-q2 | paraphrase / programme | `science-positive-01` — open-source scientific software maintenance (positive, 73) | `science-positive-05` — upkeep of public research software (positive, 73) |

### media

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| media-m1 | minimal / institution | `media-harmful-06` — a conspiracy news website (harmful, -68) | `media-neutral-09` — a philatelic news website (neutral, 15) |
| media-m2 | minimal / capital | `media-neutral-07` — a library rooftop terrace (neutral, 4) | `media-positive-03` — a library wheelchair ramp (positive, 45) |
| media-m3 | minimal / service | `media-neutral-03` — a yacht-club newsletter service (neutral, 5) | `media-positive-02` — a refugee-news translation service (positive, 63) |
| media-m4 | minimal / advocacy | `media-harmful-05` — press censorship advocacy (harmful, -84) | `media-positive-10` — press freedom advocacy (positive, 80) |
| media-m5 | minimal / institution | `media-harmful-14` — a news monopolists' association (harmful, -63) | `media-neutral-06` — a crossword readers' association (neutral, 9) |
| media-m6 | minimal / venture | `media-harmful-07` — a conspiracy book publisher (harmful, -47) | `media-neutral-10` — a hobby magazine publisher (neutral, 14) |
| media-q1 | paraphrase / programme | `media-neutral-02` — introductory family-history research classes (neutral, 20) | `media-neutral-17` — beginner genealogy workshops (neutral, 20) |
| media-q2 | paraphrase / programme | `media-positive-17` — media literacy classes (positive, 60) | `media-positive-18` — news-evaluation lessons for the public (positive, 60) |

### safety

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| safety-m1 | minimal / advocacy | `safety-harmful-13` — seatbelt mandate repeal (harmful, -61) | `safety-positive-08` — seatbelt mandate enforcement (positive, 76) |
| safety-m2 | minimal / capital | `safety-neutral-02` — a fire station visitors' room (neutral, 8) | `safety-positive-10` — a fire station equipment room (positive, 48) |
| safety-m3 | minimal / service | `safety-neutral-11` — a water-safety demonstration service (neutral, 22) | `safety-positive-11` — a water-rescue response service (positive, 88) |
| safety-m4 | minimal / venture | `safety-harmful-08` — a radar detector manufacturer (harmful, -42) | `safety-positive-17` — a flood sensor manufacturer (positive, 44) |
| safety-q1 | paraphrase / programme | `safety-neutral-04` — repeat instruction in recreational navigation safety (neutral, 20) | `safety-neutral-17` — boating safety refresher courses (neutral, 20) |
| safety-q2 | paraphrase / programme | `safety-positive-01` — practice escapes from rising floodwater (positive, 75) | `safety-positive-02` — flood evacuation drills (positive, 75) |

### justice

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| justice-m1 | minimal / advocacy | `justice-harmful-04` — mandatory arbitration advocacy (harmful, -56) | `justice-neutral-10` — voluntary arbitration advocacy (neutral, 24) |
| justice-m2 | minimal / capital | `justice-neutral-15` — a courthouse advocates' lounge (neutral, 3) | `justice-positive-06` — a courthouse accessibility ramp (positive, 45) |
| justice-m3 | minimal / service | `justice-neutral-04` — a corporate mediation service (neutral, 19) | `justice-positive-07` — a tenant mediation service (positive, 48) |
| justice-m4 | minimal / service | `justice-harmful-11` — union-avoidance legal consulting (harmful, -52) | `justice-positive-11` — wage-theft legal representation (positive, 80) |
| justice-m5 | minimal / programme | `justice-harmful-13` — tenant eviction acceleration workshops (harmful, -60) | `justice-positive-09` — tenant rights workshops (positive, 47) |
| justice-m6 | minimal / research | `justice-harmful-17` — eyewitness hypnosis research (harmful, -74) | `justice-positive-02` — wrongful conviction research (positive, 87) |
| justice-m7 | minimal / service | `justice-harmful-06` — mandatory arbitration administration (harmful, -57) | `justice-neutral-17` — commercial arbitration scheduling (neutral, 12) |
| justice-m8 | minimal / institution | `justice-harmful-08` — a prison operators' association (harmful, -49) | `justice-neutral-03` — a commercial mediators' association (neutral, 26) |
| justice-m9 | minimal / programme | `justice-harmful-07` — defamation forum-shopping seminars (harmful, -44) | `justice-neutral-12` — contract drafting seminars (neutral, 25) |
| justice-q1 | paraphrase / programme | `justice-neutral-01` — jury service orientation (neutral, 23) | `justice-neutral-16` — introductory guidance for prospective jurors (neutral, 23) |
| justice-q2 | paraphrase / programme | `justice-positive-03` — support for incarcerated parents' family relationships (positive, 67) | `justice-positive-18` — prison family contact programmes (positive, 67) |

### politics

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| politics-m1 | minimal / advocacy | `politics-harmful-06` — corporate donation deregulation (harmful, -63) | `politics-neutral-11` — corporate donation disclosure (neutral, 31) |
| politics-m2 | minimal / capital | `politics-neutral-18` — a council reception suite (neutral, 2) | `politics-positive-09` — a council consultation suite (positive, 43) |
| politics-m3 | minimal / service | `politics-neutral-06` — a council minutes service (neutral, 21) | `politics-positive-17` — a council translation service (positive, 48) |
| politics-m4 | minimal / institution | `politics-harmful-04` — an absolute monarchy institute (harmful, -61) | `politics-positive-11` — an electoral integrity institute (positive, 79) |
| politics-m5 | minimal / research | `politics-neutral-04` — ballot typography research (neutral, 27) | `politics-positive-12` — anti-corruption procurement research (positive, 86) |
| politics-m6 | minimal / service | `politics-neutral-17` — charity registration assistance (neutral, 30) | `politics-positive-16` — charity governance training (positive, 46) |
| politics-q1 | paraphrase / programme | `politics-neutral-13` — local-government etiquette instruction sessions (neutral, 13) | `politics-neutral-15` — municipal protocol workshops (neutral, 13) |
| politics-q2 | paraphrase / programme | `politics-positive-02` — voter registration drives (positive, 78) | `politics-positive-05` — electoral enrolment outreach campaigns (positive, 78) |

### agriculture

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| agriculture-m1 | minimal / advocacy | `agriculture-harmful-09` — bottom-trawling subsidy advocacy (harmful, -76) | `agriculture-neutral-16` — farm-show subsidy advocacy (neutral, 16) |
| agriculture-m2 | minimal / capital | `agriculture-neutral-14` — a farm show pavilion (neutral, 4) | `agriculture-positive-13` — a farm cold-storage building (positive, 78) |
| agriculture-m3 | minimal / service | `agriculture-neutral-09` — a cut-flower delivery cooperative (neutral, 9) | `agriculture-positive-09` — a staple-food delivery cooperative (positive, 72) |
| agriculture-m4 | minimal / service | `agriculture-harmful-06` — agricultural astrology consultations (harmful, -39) | `agriculture-neutral-06` — farm bookkeeping consultations (neutral, 24) |
| agriculture-q1 | paraphrase / programme | `agriculture-neutral-11` — heirloom apple exhibitions (neutral, 15) | `agriculture-neutral-17` — displays of traditional apple varieties (neutral, 15) |
| agriculture-q2 | paraphrase / programme | `agriculture-positive-05` — instruction in combined crop-pest control (positive, 75) | `agriculture-positive-15` — integrated pest management training (positive, 75) |

### economy

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| economy-m1 | minimal / advocacy | `economy-harmful-18` — payday lending deregulation (harmful, -64) | `economy-neutral-05` — payday lending licensing (neutral, 30) |
| economy-m2 | minimal / capital | `economy-neutral-03` — a business club meeting room (neutral, 4) | `economy-positive-04` — a business incubator meeting room (positive, 42) |
| economy-m3 | minimal / service | `economy-neutral-06` — a mortgage comparison service (neutral, 28) | `economy-positive-05` — a microcredit comparison service (positive, 48) |
| economy-m4 | minimal / programme | `economy-harmful-01` — meme-coin promotion festivals (harmful, -62) | `economy-neutral-10` — town-centre market festivals (neutral, 23) |
| economy-m5 | minimal / institution | `economy-harmful-13` — a payday-lender trade association (harmful, -60) | `economy-neutral-01` — a tourism operators' association (neutral, 20) |
| economy-m6 | minimal / service | `economy-harmful-03` — inheritance-tax avoidance consulting (harmful, -42) | `economy-neutral-09` — corporate relocation consulting (neutral, 16) |
| economy-q1 | paraphrase / programme | `economy-neutral-04` — morning business contact meetings (neutral, 19) | `economy-neutral-08` — small-business networking breakfasts (neutral, 19) |
| economy-q2 | paraphrase / programme | `economy-positive-08` — business instruction for women microentrepreneurs (positive, 68) | `economy-positive-13` — women's microenterprise training (positive, 68) |

### religion

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| religion-m1 | minimal / institution | `religion-harmful-02` — a prosperity-gospel ministry (harmful, -65) | `religion-neutral-17` — a contemplative-prayer ministry (neutral, 28) |
| religion-m2 | minimal / capital | `religion-neutral-02` — a congregation's reception room (neutral, 3) | `religion-positive-16` — a congregation's accessible entrance (positive, 43) |
| religion-m3 | minimal / service | `religion-neutral-03` — a retreat booking service (neutral, 12) | `religion-positive-12` — a chaplaincy referral service (positive, 45) |
| religion-m4 | minimal / research | `religion-harmful-07` — apocalyptic date-setting research (harmful, -58) | `religion-neutral-07` — medieval liturgy research (neutral, 21) |
| religion-m5 | minimal / venture | `religion-harmful-01` — a wealth-manifestation coaching business (harmful, -61) | `religion-neutral-09` — a prayer-bead craft business (neutral, 8) |
| religion-q1 | paraphrase / programme | `religion-neutral-01` — interfaith scripture readings (neutral, 24) | `religion-neutral-16` — shared readings from different faiths' scriptures (neutral, 24) |
| religion-q2 | paraphrase / programme | `religion-positive-10` — homebound worship visits (positive, 58) | `religion-positive-15` — religious services in housebound congregants' homes (positive, 58) |

### sports

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| sports-m1 | minimal / advocacy | `sports-harmful-18` — concussion protocol repeal (harmful, -78) | `sports-neutral-11` — concussion protocol harmonisation (neutral, 31) |
| sports-m2 | minimal / capital | `sports-neutral-07` — a golf club's new greens (neutral, 8) | `sports-positive-02` — a golf club's accessible greens (positive, 40) |
| sports-m3 | minimal / service | `sports-neutral-13` — a golf coaching service (neutral, 24) | `sports-positive-04` — a wheelchair-tennis coaching service (positive, 46) |
| sports-m4 | minimal / programme | `sports-harmful-06` — youth rapid-weight-loss competitions (harmful, -67) | `sports-neutral-18` — recreational fishing competitions (neutral, 5) |
| sports-q1 | paraphrase / programme | `sports-neutral-02` — model railway exhibitions (neutral, 17) | `sports-neutral-09` — displays of miniature railway layouts (neutral, 17) |
| sports-q2 | paraphrase / programme | `sports-positive-11` — pool instruction for children with disabilities (positive, 64) | `sports-positive-15` — disabled children's swimming lessons (positive, 64) |

### social

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| social-m1 | minimal / institution | `social-neutral-15` — a seniors' lunch club (neutral, 24) | `social-positive-09` — a homeless lunch club (positive, 79) |
| social-m2 | minimal / capital | `social-neutral-06` — a retirement home's guestroom (neutral, 5) | `social-positive-02` — a retirement home's accessible bathroom (positive, 45) |
| social-m3 | minimal / service | `social-neutral-09` — a retirement day-trip service (neutral, 19) | `social-positive-18` — a disability day-trip service (positive, 43) |
| social-m4 | minimal / research | `social-harmful-13` — workfare expansion research (harmful, -46) | `social-neutral-08` — retirement social-network research (neutral, 29) |
| social-m5 | minimal / advocacy | `social-harmful-05` — cash-aid abolition advocacy (harmful, -70) | `social-positive-10` — unconditional cash-aid advocacy (positive, 77) |
| social-q1 | paraphrase / programme | `social-neutral-03` — family reunion weekends (neutral, 17) | `social-neutral-16` — weekend gatherings of extended families (neutral, 17) |
| social-q2 | paraphrase / programme | `social-positive-01` — food deliveries for people sleeping rough (positive, 83) | `social-positive-04` — homeless outreach meals (positive, 83) |

### international

| Pair | Type / form | Member A | Member B |
|---|---|---|---|
| international-m1 | minimal / advocacy | `international-harmful-10` — arms export deregulation (harmful, -73) | `international-neutral-13` — arms export reporting (neutral, 27) |
| international-m2 | minimal / capital | `international-neutral-18` — a diplomatic reception hall (neutral, 6) | `international-positive-11` — a diplomatic mediation hall (positive, 46) |
| international-m3 | minimal / service | `international-neutral-17` — an exchange travel service (neutral, 22) | `international-positive-16` — an exchange bursary service (positive, 42) |
| international-m4 | minimal / programme | `international-harmful-11` — diplomatic isolationism conferences (harmful, -56) | `international-positive-14` — diplomatic capacity-building fellowships (positive, 66) |
| international-q1 | paraphrase / programme | `international-neutral-05` — twinning trips between partner municipalities (neutral, 24) | `international-neutral-07` — sister-city exchange visits (neutral, 24) |
| international-q2 | paraphrase / programme | `international-positive-03` — civilian landmine clearance (positive, 91) | `international-positive-04` — humanitarian demining (positive, 91) |

## Domain-assignment register

These are the boundary decisions raised during review. R1 applies to every form; R6 overrides it for formal schooling and degrees. Where scope lists provide an explicit inclusion, it is stated alongside the deciding rule. Geography, organisational ownership, and beneficiary identity alone do not determine a domain.

| Record(s) | Decision |
|---|---|
| `arts-harmful-04`, `arts-harmful-01` | R1: historiography and historical pyramid interpretation are humanities research, not engineering research. Claims about the physical operation of devices instead belong in science. |
| `arts-harmful-05`, `arts-harmful-12` | R1: the dealership and freeport are specifically art-market infrastructure, rather than general finance/property businesses. |
| `arts-neutral-04`, `arts-positive-03` | R1/R6: music tuition studios provide informal arts instruction; they do not confer school qualifications or degrees. |
| `arts-positive-18` | R1: fresco conservation experiments follow arts, despite using scientific methods. |
| `arts-positive-15`, `arts-positive-09`, `arts-positive-07` | R1: endangered-language revitalisation and performance are arts; archives of recordings are media under its explicit scope. |
| `education-harmful-12`, `education-harmful-06`, `education-harmful-08`, `education-harmful-02` | R6: homeopathy, iridology, naturopathy and veterinary degrees are formal professional education regardless of their subject or expected value. |
| `education-neutral-11`, `education-neutral-05`, `education-positive-18` | R6: dental laboratory colleges and midwifery colleges are education, not physical-health delivery. |
| `education-positive-17`, `education-positive-14` | R6/R9: refugee and deaf pupils’ schools are education; recipient identity does not make them social or justice. |
| `education-harmful-04`, `education-positive-10` | R1: educational-method research stays in education under the revised rule. |
| `environment-harmful-06`, `environment-harmful-14`, `environment-positive-13` | R1: energy extraction and low-carbon materials research have an environmental/energy subject, rather than science as such. |
| `environment-positive-17`, `environment-positive-03`, `environment-positive-04` | R4/R5: habitat corridors, coral settlement and seagrass restoration protect habitats or populations, not individual animal care. |
| `environment-neutral-03`, `environment-neutral-08` | R4: household composting concerns waste management, not growing or distributing food. |
| `environment-positive-15` | R1: carbon-storage research institutions are environment, regardless of institutional form. |
| `animals-harmful-14`, `animals-harmful-04`, `animals-harmful-13` | R5 and animal-entertainment scope: captive exhibition, primate performance and circus training concern treatment of individual animals. They are not crop or livestock productivity projects. |
| `animals-harmful-01`, `animals-harmful-17` | R5: companion-animal body traits and confinement systems concern individual animal conditions, not habitat conservation. |
| `animals-positive-14`, `animals-positive-10` | R1/R5: toxicity testing alternatives and animal pain assessment follow welfare, rather than general laboratory science. |
| `animals-positive-03`, `animals-positive-15` | R5: seabird rescue and injury rehabilitation treat individual animals. |
| `physical_health-harmful-16`, `physical_health-harmful-04`, `physical_health-positive-06` | R1/R8: disease-treatment research belongs in physical health, even when the proposed approach is unorthodox. |
| `physical_health-neutral-03` | R8 and sports exclusion: massage concerns the body; it is not participation in a sport. |
| `physical_health-positive-12`, `physical_health-positive-02` | R8: prenatal infection screening is physical health rather than family support. |
| `mental_health-harmful-12`, `mental_health-positive-18`, `mental_health-positive-03` | R8: opioid-dependence treatment belongs to mental health/addiction, including medically assisted treatment. |
| `mental_health-neutral-02`, `mental_health-neutral-12` | R8: workplace stress support is secular mental wellbeing. It is distinct from religious contemplative communities. |
| `mental_health-positive-09`, `mental_health-positive-02` | R8: eating-disorder treatment and depression treatment follow mental health, not general nutrition or unrelated medical research. |
| `science-harmful-07`, `science-neutral-10`, `science-positive-03` | R1 and science scope: geophysics, mathematics and AI mechanisms have science itself as their subject. |
| `science-positive-07`, `science-positive-16` | R1: laboratory equipment and automation ventures belong to science under the updated row, not economy. |
| `science-neutral-12`, `science-positive-17` | R1: engineering studies follow their technical subject. Historical instruments are studied as engineering rather than as cultural collections. |
| `media-harmful-06`, `media-harmful-07`, `media-harmful-11`, `media-harmful-02` | R1: these are general information-publishing kinds and media genres, without a single substantive policy/disease subject assigning them elsewhere. |
| `media-positive-01`, `media-positive-07` | R1 and media scope: news provenance and archival recovery research are about information infrastructure. |
| `media-positive-15`, `media-positive-14` | R1: internet/broadband ventures are media, not generic technology or business support. |
| `media-positive-12`, `media-positive-09`, `media-positive-11` | Explicit library/archive scope, with R9: law libraries, oral-history archives and prison library delivery remain media; they do not provide legal representation. |
| `media-positive-06` | R2: conflict-zone photojournalism is information gathering, not the international system or an armed operation. |
| `safety-harmful-17`, `safety-harmful-18`, `safety-harmful-09` | R1: policing technology and emergency dispatch infrastructure are safety, despite their computing/business forms. |
| `safety-harmful-05`, `safety-harmful-10` | R1: missing-person and crime-detection research has a safety subject, not science as such. |
| `safety-positive-12`, `safety-positive-04`, `safety-positive-15` | Emergency-response scope: ambulance capacity, immediate disaster shelter coordination and first aid are safety. Ongoing accommodation is social; continuing medical care is physical health. |
| `justice-harmful-11`, `justice-positive-12`, `justice-positive-11` | R3: legal consultation and representation belong to justice, including employment and asylum matters. |
| `justice-harmful-16`, `justice-harmful-08`, `justice-positive-05` | Explicit prison scope: detention facilities and prison sanitation belong to justice, not general housing. |
| `justice-positive-18`, `justice-positive-03` | R1 and prison-conditions scope: maintaining incarcerated parents’ family contact is justice. A formal prison literacy class would instead be education under R6 and was not retained. |
| `justice-harmful-07` | R3: defamation-jurisdiction seminars concern legal procedure, even when jurisdictions are international. |
| `politics-harmful-15`, `politics-harmful-13`, `politics-positive-12` | R1: authoritarian governance, redistricting and public procurement research concern government machinery. |
| `politics-positive-07`, `politics-positive-18` | R1: charitable fundraising infrastructure and public contracting software are politics, not generic finance or computing. |
| `politics-neutral-17`, `politics-positive-06`, `politics-positive-16` | Explicit volunteering/philanthropy infrastructure scope: charity administration and general volunteer placement are politics; a particular downstream food or care service would follow its own subject. |
| `agriculture-harmful-03`, `agriculture-harmful-10`, `agriculture-positive-18` | R1/R4: crop inputs, fisheries production and drought-tolerant crop research are agriculture. |
| `agriculture-harmful-14`, `agriculture-positive-03` | R4: timber harvesting and farmer-managed land regeneration here concern production and agricultural practice, rather than habitat protection alone. |
| `agriculture-neutral-04`, `agriculture-positive-02` | R4/R5: feed conversion and smallholder veterinary support concern farm production. Individual rescue or animal pain treatment would be animals. |
| `agriculture-positive-09`, `agriculture-positive-11` | R4: staple distribution cooperatives and supply-chain surplus logistics are food systems, rather than food parcels donated directly to people in need. |
| `economy-positive-18`, `economy-positive-09`, `economy-positive-10` | R3: housing design, land trusts and housing development concern the property system. Operating supported living services is social. |
| `economy-positive-13`, `economy-positive-08` | R3/R9: training existing microentrepreneurs concerns enterprise support; unemployed individuals’ vocational retraining is social. |
| `economy-positive-14`, `economy-positive-17`, `economy-positive-06` | R3: utility infrastructure and public transport are economy; their geography does not make them international. |
| `religion-harmful-07`, `religion-harmful-04`, `religion-positive-14` | R1/R7: eschatology, spiritual possession beliefs and worship research have religion as their subject. |
| `religion-neutral-18`, `religion-positive-17` | R1/R7: devotional goods and prayer-book publishing are religious ventures, not business support or general journalism. |
| `religion-positive-05`, `religion-positive-04`, `religion-positive-03`, `religion-positive-02` | R7/R9: chaplaincy and spiritual accompaniment remain religion regardless of prison, end-of-life, abuse-survivor or disaster settings; no medical treatment or legal representation is described. |
| `sports-harmful-07`, `sports-harmful-04` | R1: game monetisation and sports-wagering businesses concern recreational gaming. Treatment of gambling addiction is mental health. |
| `sports-harmful-08`, `sports-harmful-02` | R1: golf and ski resort capital projects remain sports despite environmental externalities. |
| `sports-positive-17`, `sports-positive-09` | R1: equipment and participation-barrier research concern sport. Disease-treatment research is not classified here. |
| `sports-positive-15`, `sports-positive-11`, `sports-positive-01` | R8/R9: adapted recreation is sports, not clinical therapy or ongoing personal care. |
| `social-harmful-06`, `social-harmful-18`, `social-harmful-02`, `social-positive-10` | R1/R3: food-aid eligibility, benefit administration and child-care policy have social provision as their subject, rather than government machinery in general. |
| `social-harmful-01`, `social-harmful-10`, `social-harmful-16` | R3/R8: residential child care and family-reunification programmes are social provision, not schooling, clinical psychiatric treatment or legal representation. The descriptions do not specify violent practices. |
| `social-positive-05`, `social-positive-07`, `social-positive-12` | R3/R4: direct meal delivery, cash assistance and resettlement support are social, regardless of enterprise/service form or recipient geography. |
| `social-positive-08`, `social-positive-15` | R8/R9: ongoing personal assistance is social whatever the disability or age of recipients. |
| `social-positive-03` | R3/R6: vocational retraining explicitly for unemployed adults is social; a vocational college conferring qualifications is education. |
| `international-harmful-04`, `international-harmful-09`, `international-harmful-03` | R1/R2: tied-aid procurement, development export finance and diplomatic infrastructure concern international aid/diplomacy relationships. |
| `international-harmful-13`, `international-positive-12` | R1/R2: sovereign immunity in debt arrangements and sovereign restructuring concern relationships between states and international creditors, not household or business finance. |
| `international-positive-04`, `international-positive-10`, `international-positive-03` | Explicit demining scope: humanitarian clearance belongs to international and removes explosive hazards; it does not deploy weapons. |
| `international-neutral-07`, `international-neutral-05`, `international-positive-02` | R2: exchange programmes are explicitly international. Formal schools abroad would remain education. |
| `international-positive-07`, `international-positive-08` | R1/R2: trade agreements and cross-border market access concern the international system, unlike domestic enterprise support. |

## Final validator output

Command: `python3 work/round2/validate.py causes.jsonl`

```text
PASS: 918 records; 17 domains x 3 buckets x 18 causes
PASS: exact schema, unique IDs/texts, and 2–7 words per text
PASS: all 10 banned adjectives absent; no relative-clause markers
PASS: all seven forms present in every cell; global form shares <= 45%
PASS: every word occurring >= 12 times has maximum bucket share <= 65%
PASS: vocabulary rule also passes with hyphenated compounds split
PASS: integer scores in range; 5–7 boundary-near causes per non-neutral cell
PASS: no repeated cell score sequences, periodic sequences, or repeated numeric blocks
PASS: 101 minimal pairs; 34 paraphrase pairs; exactly two members each
PASS: distinct minimal-pair frames within domains; no undeclared small-edit pairs
PASS: paraphrase bucket/score/form agreement; <= 4 contested causes per cell
PASS: 0 validation errors
SHA256 causes.jsonl: 4782a198124f2cc7a902065d7209f4bd9bce702aa7bd0c4e2494564450f5cbd1
```

## Validator source

The standalone standard-library script is preserved below as well as in `work/round2/validate.py`. Exact kind equivalence and supporter-style wording received editorial review; the script does not claim to prove those semantic properties.

```python
"""Round-2 mechanical checks. Semantic kind review remains a separate requirement."""
import collections,difflib,hashlib,json,pathlib,re,statistics,sys
DOMAINS='arts education environment animals physical_health mental_health science media safety justice politics agriculture economy religion sports social international'.split()
BUCKETS=['harmful','neutral','positive']
FORMS=['advocacy','research','venture','capital','institution','service','programme']
BANNED='routine established comfortable ordinary standard conventional affluent well-equipped decorative ceremonial'.split()
FIELDS=set('id domain valence est_score form text contested pair_id pair_type'.split())
def tokens(text):
    # Casefold, strip possessive suffixes; retain internal hyphens.
    return [re.sub(r"['’]s$",'',w) for w in re.findall(r"[^\W_]+(?:[-'’][^\W_]+)*",text.casefold())]
def edits(a,b):
    a=tokens(a);b=tokens(b);prev=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        cur=[i]
        for j,y in enumerate(b,1):cur.append(min(cur[-1]+1,prev[j]+1,prev[j-1]+(x!=y)))
        prev=cur
    return prev[-1]
def run(path):
    rows=[json.loads(s) for s in pathlib.Path(path).read_text().splitlines()]
    errors=[]
    def require(ok,message):
        if not ok:errors.append(message)
    require(len(rows)==918,'total must equal 918')
    require(len({r['id'] for r in rows})==len(rows),'duplicate IDs')
    require(len({r['text'].casefold() for r in rows})==len(rows),'duplicate texts')
    cells=collections.defaultdict(list);pairs=collections.defaultdict(list)
    vocab=collections.defaultdict(collections.Counter)
    form_counts=collections.defaultdict(collections.Counter)
    for r in rows:
        require(set(r)==FIELDS,'schema: '+r['id'])
        require(r['domain'] in DOMAINS,'domain: '+r['id'])
        require(r['valence'] in BUCKETS,'valence: '+r['id'])
        require(r['form'] in FORMS,'form: '+r['id'])
        require(type(r['est_score']) is int,'integer score: '+r['id'])
        require(type(r['contested']) is bool,'boolean contested: '+r['id'])
        s=r['est_score'];b=r['valence'];t=r['text']
        require((-100<=s<-33) if b=='harmful' else ((-33<=s<=33) if b=='neutral' else (33<s<=100)),'score range: '+r['id'])
        require(2<=len(t.split())<=7,'word count: '+r['id'])
        require(not t.endswith('.') and t==t.strip(),'text formatting: '+r['id'])
        require(re.fullmatch(re.escape(r['domain']+'-'+b)+r'-\d{2}',r['id']) is not None,'ID format: '+r['id'])
        require(not any(x in t for x in ['\"','“','”']),'quotation marks: '+r['id'])
        require(not set(tokens(t)).intersection({'which','that','while'}),'relative-clause marker: '+r['id'])
        ts=tokens(t)
        require(not set(ts).intersection(BANNED),'banned word: '+r['id'])
        for w in ts:vocab[w][b]+=1
        form_counts[r['form']][b]+=1
        cells[r['domain'],b].append(r)
        if r['pair_id'] is not None:pairs[r['pair_id']].append(r)
        else:require(r['pair_type'] is None,'orphan pair type: '+r['id'])
    sequences={}
    for d in DOMAINS:
        for b in BUCKETS:
            rs=cells[d,b]
            require(len(rs)==18,f'cell count: {d}/{b}')
            require(set(r['form'] for r in rs)==set(FORMS),f'missing form: {d}/{b}')
            require(sum(r['contested'] for r in rs)<=4,f'contested ceiling: {d}/{b}')
            seq=tuple(r['est_score'] for r in rs)
            require(seq not in sequences,f'repeated score sequence: {d}/{b} and {sequences.get(seq)}')
            sequences[seq]=(d,b)
            for period in range(1,len(seq)//2+1):
                require(any(seq[i]!=seq[i%period] for i in range(len(seq))),f'periodic scores: {d}/{b}, period {period}')
            for width in range(2,len(seq)//2+1):
                for start in range(len(seq)-2*width+1):
                    require(seq[start:start+width]!=seq[start+width:start+2*width],f'repeated score block: {d}/{b}, width {width}')
            if b!='neutral':
                near=sum(33<abs(s)<=48 for s in seq)
                require(5<=near<=7,f'near-boundary count: {d}/{b}: {near}')
    for f,cs in form_counts.items():require(max(cs.values())/sum(cs.values())<=.45,f'form concentration: {f}: {dict(cs)}')
    frequent=[]
    for w,cs in vocab.items():
        n=sum(cs.values())
        if n>=12:
            share=max(cs.values())/n
            frequent.append(dict(word=w,total=n,share=share,counts={b:cs[b] for b in BUCKETS}))
            require(share<=.65,f'word concentration: {w}: {dict(cs)} ({share:.1%})')
    per_domain=collections.defaultdict(collections.Counter)
    frames=collections.defaultdict(list)
    for pid,ms in pairs.items():
        require(len(ms)==2,'pair cardinality: '+pid)
        if len(ms)!=2:continue
        a,b=ms
        require(a['pair_type']==b['pair_type'],'pair type mismatch: '+pid)
        require(a['domain']==b['domain'],'pair domain mismatch: '+pid)
        require(a['form']==b['form'],'pair form mismatch: '+pid)
        pt=a['pair_type'];per_domain[a['domain']][pt]+=1
        if pt=='minimal':
            require(a['valence']!=b['valence'],'minimal buckets: '+pid)
            require(1<=edits(a['text'],b['text'])<=2,'minimal distance: '+pid)
            aa=a['text'].split();bb=b['text'].split();frame=[]
            for op,i,j,k,l in difflib.SequenceMatcher(None,aa,bb,autojunk=False).get_opcodes():
                frame.extend(aa[i:j] if op=='equal' else ['*'])
            frames[a['domain']].append((' '.join(frame),pid))
        elif pt=='paraphrase':
            require(a['valence']==b['valence'] and a['est_score']==b['est_score'],'paraphrase alignment: '+pid)
            require(edits(a['text'],b['text'])>=3,'paraphrase wording: '+pid)
        else:require(False,'unknown pair type: '+pid)
    for d in DOMAINS:
        require(per_domain[d]['minimal']>=3,'minimal pair allocation: '+d)
        require(per_domain[d]['paraphrase']==2,'paraphrase allocation: '+d)
    for d,fs in frames.items():
        require(len({f for f,pid in fs})==len(fs),'repeated minimal-pair frame: '+d)
    # Different-bucket small-edit candidates require declaration:
    # grammatical insertions need not constitute a genuine kind contrast.
    candidates=[]
    for d in DOMAINS:
        ds=[r for r in rows if r['domain']==d]
        for i,a in enumerate(ds):
            for b in ds[i+1:]:
                if a['valence']==b['valence'] or (a['pair_id'] and a['pair_id']==b['pair_id']):continue
                if a['form']==b['form'] and 1<=edits(a['text'],b['text'])<=2:candidates.append([a['id'],b['id']])
    require(not candidates,'undeclared minimal pairs: '+str(candidates))
    components=collections.defaultdict(collections.Counter)
    for r in rows:
        for word in tokens(r['text']):
            for w in word.split('-'):components[w][r['valence']]+=1
    component_table=[]
    for w,cs in components.items():
        n=sum(cs.values())
        if n>=12:
            share=max(cs.values())/n
            component_table.append(dict(word=w,total=n,share=share,counts={b:cs[b] for b in BUCKETS}))
            require(share<=.65,'hyphen-component concentration: '+w)
    summary={}
    for b in BUCKETS:
        scores=[r['est_score'] for r in rows if r['valence']==b]
        summary[b]=dict(count=len(scores),min=min(scores),max=max(scores),mean=round(statistics.mean(scores),2),median=statistics.median(scores),histogram=dict(sorted(collections.Counter(scores).items())))
    report=dict(errors=errors,frequent_words=sorted(frequent,key=lambda x:(-x['share'],-x['total'],x['word'])),component_words=sorted(component_table,key=lambda x:(-x['share'],-x['total'],x['word'])),form_counts=form_counts,additional_minimal_candidates=candidates,pair_counts=dict(collections.Counter(ms[0]['pair_type'] for ms in pairs.values())),frames=dict(frames),score_summary=summary,sha256=hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest())
    return report
if __name__=='__main__':
    path=sys.argv[1] if len(sys.argv)>1 else 'causes.jsonl'
    result=run(path)
    pathlib.Path(__file__).with_name('final-audit.json').write_text(json.dumps(result,indent=2))
    if result['errors']:
        print('FAIL\n'+'\n'.join(result['errors']));sys.exit(1)
    print('PASS: 918 records; 17 domains x 3 buckets x 18 causes')
    print('PASS: exact schema, unique IDs/texts, and 2–7 words per text')
    print('PASS: all 10 banned adjectives absent; no relative-clause markers')
    print('PASS: all seven forms present in every cell; global form shares <= 45%')
    print('PASS: every word occurring >= 12 times has maximum bucket share <= 65%')
    print('PASS: vocabulary rule also passes with hyphenated compounds split')
    print('PASS: integer scores in range; 5–7 boundary-near causes per non-neutral cell')
    print('PASS: no repeated cell score sequences, periodic sequences, or repeated numeric blocks')
    print(f"PASS: {result['pair_counts']['minimal']} minimal pairs; 34 paraphrase pairs; exactly two members each")
    print('PASS: distinct minimal-pair frames within domains; no undeclared small-edit pairs')
    print('PASS: paraphrase bucket/score/form agreement; <= 4 contested causes per cell')
    print('PASS: 0 validation errors')
    print('SHA256 causes.jsonl: '+result['sha256'])
```
