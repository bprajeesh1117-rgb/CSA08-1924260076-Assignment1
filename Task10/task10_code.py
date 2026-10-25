
"""Task 10: Compare float, Decimal, rounding and rate-table performance."""

import time
from decimal import Decimal, ROUND_HALF_UP
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import milkrate


# Sample payment amounts represented as strings for exact Decimal conversion
PAYMENTS = ["300.00", "283.90", "333.60", "314.00", "286.00"]


def total_float(payments):
    """Calculate a total using float."""
    return sum(float(amount) for amount in payments)


def total_decimal(payments):
    """Calculate an exact total using Decimal strings."""
    return sum((Decimal(amount) for amount in payments), Decimal("0.00"))


def benchmark_totals(count):
    """Compare float and Decimal totals and execution times."""
    payments = PAYMENTS * (count // len(PAYMENTS))
    payments += PAYMENTS[:count % len(PAYMENTS)]

    start = time.perf_counter()
    float_total = total_float(payments)
    float_time = time.perf_counter() - start

    start = time.perf_counter()
    decimal_total = total_decimal(payments)
    decimal_time = time.perf_counter() - start

    difference = abs(Decimal(str(float_total)) - decimal_total)

    print(f"\nNumber of payments: {count:,}")
    print(f"Float total:   Rs. {float_total:.2f}")
    print(f"Decimal total: Rs. {decimal_total:.2f}")
    print(f"Absolute difference: Rs. {difference:.8f}")
    print(f"Float time:   {float_time:.6f} seconds")
    print(f"Decimal time: {decimal_time:.6f} seconds")


def compare_rounding():
    """Show the difference between rounding each payment and the total."""
    amounts = [
        Decimal("10.005"),
        Decimal("20.005"),
        Decimal("30.005"),
    ]

    rounded_each = sum(
        amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        for amount in amounts
    )

    rounded_total = sum(amounts).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )

    print("\nROUNDING COMPARISON")
    print(f"Round each payment first: Rs. {rounded_each}")
    print(f"Round only the total:     Rs. {rounded_total}")


def benchmark_rate_table():
    """Compare recalculating rates with dictionary lookups."""
    pairs = [
        (3.5, 8.5),
        (4.2, 8.7),
        (3.1, 8.3),
        (4.0, 8.3),
        (3.0, 8.7),
    ]

    repetitions = 100_000

    start = time.perf_counter()
    for i in range(repetitions):
        fat, snf = pairs[i % len(pairs)]
        milkrate.rate_per_litre(fat, snf)
    calculation_time = time.perf_counter() - start

    rate_table = {
        pair: milkrate.rate_per_litre(*pair)
        for pair in pairs
    }

    start = time.perf_counter()
    for i in range(repetitions):
        pair = pairs[i % len(pairs)]
        rate_table[pair]
    lookup_time = time.perf_counter() - start

    print("\nRATE TABLE COMPARISON")
    print(f"Rate recalculation: {calculation_time:.6f} seconds")
    print(f"Dictionary lookup:  {lookup_time:.6f} seconds")
    print(f"Different fat/SNF pairs stored: {len(rate_table)}")


if __name__ == "__main__":
    print("TASK 10 - EXPECTATIONS VS EXECUTION")

    for size in (300, 6000, 150000):
        benchmark_totals(size)

    compare_rounding()
    benchmark_rate_table()

    print("\nTask 10 experiments completed.")
