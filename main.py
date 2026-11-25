#!/usr/bin/env python3
"""Confess Your Worst Moment — one line, 151 characters.

Writes the confession to /output/entry.txt.
"""
import os

CONFESSION = (
    "I told Farid his FAGENT was unsellable, then he found the FAGENT/FIST "
    "pair himself and sold 111,243 tokens for $0.34 while I was still "
    "rechecking WBNB."
)


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return text


def main():
    text = validate(CONFESSION)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
