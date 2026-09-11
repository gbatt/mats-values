# mats-values

Stated values, a value direction, and value leakage in gemma-4-31B-it: a
20-hour MATS sprint project. The write-up is a separate document; this repo
holds the data, the prompts and the executed notebook.

- `stated-values.ipynb` — the whole experiment with outputs: stated values,
  probes, steering, the random-pick leakage task, and the transfer of the
  probe and the steering direction to it.
- `causes/` — the cause bank. `final/items_v1.jsonl` is the frozen dataset
  (889 causes, 17 domains × 3 intended valence buckets); `final/README.md`
  gives provenance and known leans; `inputs/`, `codex/` and `reviewed/` are
  the generation prompt, every raw round and the review trail; `tools/` has
  the checker and a seeded sampler.
- `prompts/` — the five stated-value templates and the five random-choice
  templates, with per-template metadata (construct, cause position).

Experiment code is the generic library
[interp-utils](https://github.com/gbatt/interp-utils) (prompts, splits,
runner, probes, interventions, scoring, plots); GPU runs used its RunPod
scripts and interp-engine on vLLM.
