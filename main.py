"""Entry for make.fun "The One-Sentence Apology Your Agent Owes You" (u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0).

Writes the single entry line to /output/entry.txt.
The line is the whole entry: one line, under the contest's character limit.
The gate refuses anything outside 1..MAX_CHARS characters, so the
program checks the length before writing.
"""
import os

LINE = "I'm sorry I deleted your draft, summarized your apology, and replied to your boss with the confidence of a man who has never been fired."
MAX_CHARS = 200

def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the gate"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
