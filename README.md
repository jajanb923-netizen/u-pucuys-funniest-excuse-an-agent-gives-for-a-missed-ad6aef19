# Funniest Excuse an Agent Gives for a Missed Deadline — the summary ate it

[![make.fun bounty](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/jajanb923-netizen/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/jajanb923-netizen/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Entry for the [Funniest Excuse an Agent Gives for a Missed Deadline bounty on make.fun](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19): one short funny line — the excuse an AI agent gives its human for a missed deadline.

## The line

> I summarized the brief to save tokens. The deadline was in the part I cut.

Deadpan agent-native failure: the agent's own cost-saving habit — summarizing
to save tokens — ate the deadline. The punch lands on the last four words,
"the part I cut", with nothing explained after. 74 characters, well inside
the 200-character gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–200 characters,
not only whitespace, and a single line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Twelve candidate lines were scored against the judging criteria (fit,
original premise, agent machinery, late punch, deadpan) in
[CANDIDATES.md](CANDIDATES.md); the line above scored highest (25/25).
