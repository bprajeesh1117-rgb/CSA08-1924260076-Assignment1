
"""Task 2: Explore Python values, types, and money calculations."""

from decimal import Decimal

# 1,000 payments of Rs. 33.40 and three small adjustments of Rs. 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    """Calculate the total using floating-point arithmetic."""
    total = 0.0

    for amount in items:
        total += float(amount)

    return total


def total_decimal(items):
    """Calculate the exact decimal total from strings."""
    total = Decimal("0.00")

    for amount in items:
        total += Decimal(amount)

    return total


if __name__ == "__main__":
    # Explore Python data types
    for value in (10, 10.0, "10", True, [10, 8.5]):
        print(repr(value), "->", type(value).__name__)

    # Explore division operators
    print("7 / 2 =", 7 / 2)
    print("7 // 2 =", 7 // 2)
    print("7 % 2 =", 7 % 2)
    print("-7 // 2 =", -7 // 2)

    # Demonstrate floating-point precision
    print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

    # Compare float and Decimal totals
    print("float  :", total_float(payments))
    print("Decimal:", total_decimal(payments))

    # Compare two ways of creating Decimal values
    print("Decimal from string:", Decimal("0.1"))
    print("Decimal from float :", Decimal(float("0.1")))

    print(
        "Decimal addition:",
        Decimal("0.1") + Decimal("0.2")
        == Decimal("0.3")
    )
