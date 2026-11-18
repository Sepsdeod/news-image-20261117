// news-image-20261117 entry (Node 22, standard library only).
// The entry image sits beside this file as entry.png; the program writes
// an exact copy of it to the grader's output directory. No network, no
// randomness: the same input bytes always produce the same output bytes.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });

const source = new URL("./entry.png", import.meta.url);
copyFileSync(source, join(outDir, "entry.png"));
