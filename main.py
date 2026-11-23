#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry (slot 1).

Writes exactly one warm line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
The line is a single sentence, well under the 200-character gate.

The line won an 8-candidate self-judge tournament (Hermes/nemotron as
judge, the competition's published judge brief verbatim, every match
judged in both orders): a street sweeper chalking a sun over a puddle —
on-subject, warm, surprising, concrete (6:40, chalk sun, puddle),
fresh wording, outside the field's saturated clusters (krupuk, bus
driver, cat-on-lap, mango-on-doorstep).
"""

import os

LINE = "At 6:40 this morning the street sweeper stopped mid-broom, drew a chalk sun over the puddle by my gate, and said, 'Walk around the good weather.'"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
