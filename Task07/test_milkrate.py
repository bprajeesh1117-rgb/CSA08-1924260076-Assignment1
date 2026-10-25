
"""Test importing and using the milkrate module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import milkrate

print("Testing imported module")
print("Rate per litre:", f"Rs. {milkrate.rate_per_litre(4.2, 8.7):.2f}")
print("Farmer payout:", f"Rs. {milkrate.payout(8.5, 4.2, 8.7):.2f}")
