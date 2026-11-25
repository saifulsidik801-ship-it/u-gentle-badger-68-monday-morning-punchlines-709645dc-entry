"""Monday Morning Punchlines — make.fun entry.

Writes a single joke about Monday mornings (at most 200 characters)
to /output/entry.txt, where the house gate scorer and judge read it.
"""

from pathlib import Path

# The entry: one line, no newline, so the gate sees exactly one joke.
# Chosen for the judge's criteria in order: it is unmistakably about Monday
# mornings, the "restraining order" twist lands late and is not the first
# thing anyone reaches for (no alarm, no coffee, no snooze), it says it in
# 76 characters, and it is fresh against the field's alarm/coffee cliches.
JOKE = "Monday morning is proof the weekend took out a restraining order against me."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = JOKE.strip()
    if not text or len(text) > 200 or "\n" in text:
        raise ValueError(f"entry must be one line of 1-200 characters, got {len(text)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}: {text}")


if __name__ == "__main__":
    main()
