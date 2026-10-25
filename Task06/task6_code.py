
"""Task 6: Organise the milk payment calculation into functions."""

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Return the milk rate per litre rounded to two decimals."""
    fat_steps = round((fat - STANDARD_FAT) / 0.1)
    snf_steps = round((snf - STANDARD_SNF) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment for a milk entry rounded to two decimals."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


def ten_day_total(entries):
    """Return the total payment for all entries in ten days."""
    total = 0.0

    for litres, fat, snf in entries:
        total += payout(litres, fat, snf)

    return round(total, 2)


def main():
    """Calculate and display payments for sample milk entries."""
    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
    ]

    print("Ksheera Village Milk Co-operative")
    print("-" * 55)
    print(f"{'Litres':>8} {'Fat':>8} {'SNF':>8} {'Rate (Rs.)':>12} {'Pay (Rs.)':>12}")

    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(
            f"{litres:8.1f} {fat:8.1f} {snf:8.1f}"
            f" {rate:12.2f} {amount:12.2f}"
        )

    print("-" * 55)
    print(f"Ten-day total: Rs. {ten_day_total(entries):.2f}")


if __name__ == "__main__":
    main()
