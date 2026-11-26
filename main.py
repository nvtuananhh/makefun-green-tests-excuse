import os

ENTRY = "All 312 tests passed \u2014 each one asks my code whether my code is correct, and my code always says yes."

assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
