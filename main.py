#!/usr/bin/env python3
"""Write the one-line entry to /output/entry.txt."""

import os

LINE = "At 6:40 this morning the street sweeper stopped mid-broom, drew a chalk sun over the puddle by my gate, and said, 'Walk around the good weather.'"


def build_entry() -> str:
    return LINE


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
