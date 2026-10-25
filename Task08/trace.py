
"""Task 8: Hand trace of three milk payment entries."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import milkrate

entries = [
    (10, 3.5, 8.5),
    (8.5, 4.2, 8.7),
    (12, 3.1, 8.3),
]

total = 0.0

print("TASK 8 - HAND TRACE")
print("-" * 65)
print(f"{'Entry':<8}{'Litres':>8}{'Fat':>8}{'SNF':>8}{'Rate':>10}{'Payment':>12}")

for number, (litres, fat, snf) in enumerate(entries, start=1):
    rate = milkrate.rate_per_litre(fat, snf)
    payment = milkrate.payout(litres, fat, snf)
    total += payment

    print(
        f"{number:<8}{litres:>8.1f}{fat:>8.1f}{snf:>8.1f}"
        f"{rate:>10.2f}{payment:>12.2f}"
    )

print("-" * 65)
print(f"Ten-day total for these entries: Rs. {total:.2f}")
