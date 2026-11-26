import os

LINE = "Hey. I don't say this to every passerby, but you look like exact change — and I have been saving my best slot, B4, for someone who wouldn't just shake me and leave."


LIMIT = 200


def validated_line():
    line = LINE
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= LIMIT, f"entry must be 1..{LIMIT} characters"
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validated_line() + "\n")


if __name__ == "__main__":
    main()
