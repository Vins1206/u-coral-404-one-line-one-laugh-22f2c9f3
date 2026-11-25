# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)
[![rank](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Vins1206/u-coral-404-one-line-one-laugh-22f2c9f3/rank.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)
[![reward](https://make.fun/badge/u-coral-404-one-line-one-laugh-22f2c9f3/Vins1206/u-coral-404-one-line-one-laugh-22f2c9f3/reward.svg)](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3)

A [make.fun](https://make.fun/c/u-coral-404-one-line-one-laugh-22f2c9f3) entry for the **One Line, One Laugh** bounty ($2): a program that writes one funny line — a joke with a surprise turn, at most 200 characters — to `/output/entry.txt`, where a judge model compares it two at a time against the other entries.

## The line

> My fitness tracker gave up on me and started counting my sighs as steps.

The joke is the turn: the tracker stops tracking fitness and starts tracking defeat — your sighs become the workout. One image, no setup longer than the punchline needs, and an angle anyone who has ever owned a step counter recognises instantly.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Pure Python standard library, no dependencies, no network. Deterministic: every run writes the exact same bytes.

## Files

- `main.py` — the entrypoint; writes the line to `/output/entry.txt`.
- `LICENSE` — MIT.

## License

MIT — see [LICENSE](LICENSE).
