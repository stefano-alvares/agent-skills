# Batch file skeleton (docs/crew/<yyyy-mm-dd>-<slug>.md)

One file per batch. `ship-spec` writes the top half, `plan-forge` the bottom half. Atlas's studio
batches add the website parts from `studio-build`. Keep it current while the work runs; re-read it on
every resume.

```
# <batch title>

## His words (verbatim)
> <his message, typos included>
1. <ask 1>  2. <ask 2>  ...

## Ship spec
Mission: <who gets what value, one line>
Definition of shipped:
- <what he clicks or runs> -> <expected result>
Ask ledger:
| # | Ask | Bucket | Owner | Gate | Done-check |
Out of scope: <what and when it would be added>
Needs your call: <decision, recommendation first>

## Decided
- <date> <decision> (his words when he gave them)

## Defaults (he can override any)

## Plan  (plan-forge, mode: quick | light | standard | high-risk)
Weakest point: <the assumption that, if false, breaks the sequence>
<steps with FILES / CHANGE / PROOF / RISK, or cards by file>

## Log
- <date> <locked decision, failed approach and why, deviation and why>
```
