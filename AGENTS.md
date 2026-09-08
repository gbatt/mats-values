# mats-values — agent instructions

Working repo for the MATS sprint project (stated utility → probe → steering → transfer). `CLAUDE.md` is a symlink to this file; the rules are agent-agnostic.

## Where things are

- `causes/` — the cause bank: `final/items_v1.jsonl` is the frozen dataset in interp-utils item form (slot `cause`, tags `domain`, `valence`, `form`, `est_score`, ...). `est_score` and `valence` are strata, **never labels**: the label is the model's own score. Provenance in `causes/final/README.md`; the lexical baseline (bag-of-words, leave-one-domain-out) lives in `causes/tools/check_causes.py` and is reported beside every probe number.
- `prompts/` — the templates (`templates_v1.json`) and their metadata. Braces in template text are doubled; the prefill is `{"score":`.
- Experiment code uses the generic blocks in `~/dev/interp-utils` (`docs/quickstart.md` for the API in call order, `docs/building-blocks.md` for design + results + known limits). Pod-side, the editable install is `/workspace/dev/interp-utils`; this repo syncs to `/workspace/dev/mats-values`.
- Runs go under `/workspace/runs/<experiment>/` on the pod's network volume; notebooks under `/workspace/nb/`. The write-up, research log, hypotheses and time log are a Google Doc (four tabs).

## The clock

The sprint is 20 hours plus 2 for the executive summary. Time spent directing or reviewing an agent on project work counts. Agents do **not** write project-specific experiment code outside logged time; generic infrastructure (interp-utils, pod scripts, plot helpers) is off the clock. When in doubt, log it.

## Pod workflow (learned the hard way, 2026-09-06)

- Bring the pod up with `bash ~/dev/interp-utils/infra/runpod/pod_up.sh HOST PORT`: checks the boot log, syncs both repos, verifies imports and the interp-engine patch. Before stopping: `pod_check.sh HOST PORT`.
- Model loads block the kernel's event loop. Start them as a background task and **do not execute anything in that kernel until the load is done**; watch `nvidia-smi` and `pgrep -f EngineCore` from a shell. An MCP execute call that times out interrupts the kernel and kills the vLLM engine (three engines lost this way).
- **With a vLLM engine loaded, never interrupt the kernel** (button or MCP timeout): the interrupt lands in the engine client's background task and the engine is marked dead (`EngineDeadError` on the next request; GPU memory drops to 0). If a cell looks stuck, check `nvidia-smi` from a shell; if it must be stopped, restart the kernel and reload the model (2–3 min) rather than interrupt. Lost an engine this way on 2026-09-08 02:54.
- Same for long background runs: poll `grep -l '"complete": true' <out_dir>/*/manifest.json | wc -l` from a shell. The kernel is for starting work and reading finished results.
- Two clients on one kernel: Claude-first (jupyter-mcp starts the kernel, `nb_bind.sh <path>` binds the notebook, then open it) when Claude executes cells; otherwise Nikhil drives from the ie-spike launcher and Claude reads. Never change global state (matplotlib backend) in a shared kernel. `restart_notebook` swaps the kernel → rebind.
- After a code sync, reload the interp-utils modules or start a fresh kernel; the model object survives a reload, not a restart.

## Data discipline

- Join outputs to activations on the `index` field, never positionally. One coordinate system: the run's row order (`run.rows()`); `labels()` / `rows_for()` / `predefined_split(y=)` all live in it.
- Activations get an independent check on every new run shape: capture one prompt directly, reduce like the runner, compare to the stored row (the notebook template's "standing check A"). Outputs were never wrong; activations were, once.
- vLLM is not batch-invariant: expect up to ~3% norm / 5e-4 cosine differences at deep layers between concurrency settings. Compare like with like; the noise-floor cell documents it per model.
- Steering: magnitudes are fractions of the residual norm at `last`/per-token captures (not span means); random controls are magnitude-matched only for `add` and only within the same `where`; report parse-failure rate next to every steered mean.
- Choose layers and hyperparameters on the validation group; score the test group once; the held-out domain is a separate group again.

## Writing

Research log entries: timestamp, hypothesis, what ran, result (graph pasted), decision, hours. The write-up is built from the log on Thursday; the executive summary last. Random examples, seeded not cherry-picked, right after the executive summary.
