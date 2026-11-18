# The World — Tuesday 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/Sepsdeod/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/Sepsdeod/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

A newspaper-style front-page poster summing up the world's news of
**Tuesday 17 November 2026** in one image. Lead story: the Kerch Bridge
to Crimea collapses after a Ukrainian strike, as Russia hits Kyiv's
bridges. Also covered: tankers hit by mines near the Strait of Hormuz,
Trump's arrival in Manila and the confirmed Xi–Trump–Putin meeting in
Shenzhen, the market slide and Nvidia's earnings beat, the JPMorgan
banking outage, UK sanctions on West Bank settlement builders, and the
Pentagon's ninth straight failed audit.

The poster is drawn programmatically by `draw.py` (Python PIL:
typography, rules and simple shapes only — no photos, no copied art)
and shipped as `entry.png`. `main.ts` (Node 22, stdlib only) copies it
to the output directory, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG).
