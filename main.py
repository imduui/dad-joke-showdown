"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Deterministic, no network, no input files.
"""

import os

JOKE = (
    "My kids asked what I do for a living. I said, \"I'm a "
    "dad-abase administrator — I keep the family records, back "
    "up the memories, and I never lose my temper. I just "
    "misplace it.\""
)


def main() -> None:
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 200, f"joke is {len(joke)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
