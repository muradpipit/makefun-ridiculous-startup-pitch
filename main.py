"""One-sentence startup pitch for make.fun's "Ridiculous at First Glance,
Real by the Second" bounty.

The program writes exactly one sentence to entry.txt: a pitch for
"apology insurance" -- a monthly subscription where a professional
apologist writes and delivers your apology when you mess up.

Why this pitch: it is genuinely bizarre (insuring an apology), the
business logic survives a second look (a good apology saves jobs and
marriages, most people are terrible at them, and a professional
writer is a real service, like ghostwriting or crisis PR, sold on a
subscription), and the sentence names the odd thing, who pays, and
why it holds together.

The gate (from the kit's RULES.txt): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only white space. The program checks
that up front and fails loudly instead of shipping a bad entry.
"""

import os

# The pitch: one sentence, at most 200 characters.
PITCH = (
    "Apology insurance: for $9 a month, a professional apologist writes "
    "and delivers your apology when you mess up, because a good apology "
    "saves jobs and marriages and most people are terrible at them."
)


def main():
    if not 1 <= len(PITCH) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not PITCH.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in PITCH:
        raise ValueError("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # The grader collects outputs as another user, so the file must
    # be readable by everyone, whatever the umask is.
    os.chmod(path, 0o644)
    # Read it back: a broken entry must fail loudly here, not sail
    # through to judging with the wrong contents.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != PITCH:
        raise ValueError("entry.txt does not hold the pitch as written")
    if not 1 <= len(written) <= 200 or not written.strip():
        raise ValueError("entry.txt fails the 1 to 200 character gate")


if __name__ == "__main__":
    main()
