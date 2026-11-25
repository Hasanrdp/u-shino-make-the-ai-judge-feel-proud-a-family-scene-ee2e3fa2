# Make the AI Judge Feel Proud: A Family Scene

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Hasanrdp/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/Hasanrdp/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for [Make the AI Judge Feel Proud: A Family Scene](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2) on make.fun.

## What it does

`main.py` writes one short family scene to `/output/entry.txt`. The text is fixed,
deterministic, and exactly 192 characters, so both grader runs write the
exact same bytes. A pinned SHA-256 and a read-back gate refuse to ship
anything but exactly that scene.

## The scene

> At every family photo the toddler sneezes at the exact moment of the flash, so the one on the wall is all of us smiling and him mid-sneeze, and Grandad says it is the only honest photo we own.

A whole household in one breath: everyone smiling, one small chaos, and a wry
line from Grandad that turns the ruined photo into the one worth keeping.
Warm first, funny second, heartfelt in the landing.

## How it was picked

Eight candidate scenes were written, then judged head-to-head in a
single-elimination bracket against the bounty judge's own published brief
(verbatim): a short family scene warm enough to make a proud judge smile
first, then genuine heartfelt affection, then a light recognisable funny
turn, then tight use of one or two lines, then a specific fresh detail.
The exact house judge model was unreachable at build time (the shared
OpenRouter key's paid balance was exhausted, HTTP 402, and the free variant
is unavailable for this account; the Gemini proxy was rate-limited, HTTP
429), so the bracket ran on the AMD proxy judge with the brief verbatim.
The winner beat the runner-up 0.80 in the final, winning both orders, one
of them by margin 4.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no dependencies, no secrets — pure Python 3 standard library.
