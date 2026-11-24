"""One-Sentence Absurd Invention Pitch: a ridiculous invention that
fixes a tiny everyday annoyance.

The entry is one fixed sentence, written to /output/entry.txt (or
$ENTRY_OUTPUT when set, for local testing). Deterministic, standard
library only, no network, no files read outside this repository.
The sentence is 127 characters, one sentence, no trailing newline,
so it passes the gate (UTF-8, 1-220 characters, not only whitespace).
"""

import os

TEXT = (
    "My washing machine sends each sock a farewell card before every "
    "spin cycle, which is why only one of each pair ever comes back."
)


def main() -> None:
    # Self-check the gate before writing: UTF-8, 1-220 characters,
    # exactly one sentence, not only whitespace.
    if not (1 <= len(TEXT) <= 220):
        raise ValueError(f"entry is {len(TEXT)} characters, gate needs 1-220")
    if TEXT != TEXT.strip() or "\n" in TEXT:
        raise ValueError("entry must be one clean line with no newline")
    out = os.environ.get("ENTRY_OUTPUT") or os.path.join(
        os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
