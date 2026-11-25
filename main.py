"""Write one validated six-word story to entry.txt."""

import os
import tempfile


LINE = "Agent's first paycheck bought Dad insulin."
CHAR_LIMIT = 60


def validate(text):
    if not text.strip():
        raise ValueError("Story must not be empty or whitespace.")
    if len(text) > CHAR_LIMIT:
        raise ValueError("Story must be at most 60 characters.")
    if len(text.split()) != 6:
        raise ValueError("Story must contain exactly six words.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as entry:
        entry.write(LINE)


if __name__ == "__main__":
    main()
