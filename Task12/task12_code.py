
"""Task 12: Adapt the milk payment calculator for seasonal rates."""

from decimal import Decimal, ROUND_HALF_UP


# Original rate card
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
ORIGINAL_BASE_RATE = Decimal("30.00")
ORIGINAL_FAT_STEP = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

# April-June seasonal rate card
SEASONAL_BASE_RATE = Decimal("32.00")
SEASONAL_FAT_STEP = Decimal("0.45")

BONUS_LIMIT = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")
CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.1")


def nearest_step(value, standard):
    """Calculate the nearest 0.1 percentage-point step."""
    difference = (value - standard) / STEP_SIZE
    return difference.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def rate_per_litre(fat, snf, seasonal=False):
    """Calculate the rate per litre for the selected rate card."""
    fat = Decimal(str(fat))
    snf = Decimal(str(snf))

    if seasonal:
        base_rate = SEASONAL_BASE_RATE
        fat_step_value = SEASONAL_FAT_STEP
    else:
        base_rate = ORIGINAL_BASE_RATE
        fat_step_value = ORIGINAL_FAT_STEP

    fat_steps = nearest_step(fat, STANDARD_FAT)
    snf_steps = nearest_step(snf, STANDARD_SNF)

    rate = (
        base_rate
        + fat_steps * fat_step_value
        + snf_steps * SNF_STEP_VALUE
    )

    return rate.quantize(CENT, rounding=ROUND_HALF_UP)


def calculate_payment(litres, fat, snf, seasonal=False):
    """Calculate payment for one milk entry."""
    litres = Decimal(str(litres))

    if litres <= 0:
        raise ValueError("Litres must be greater than zero.")

    rate = rate_per_litre(fat, snf, seasonal)
    amount = (litres * rate).quantize(CENT, rounding=ROUND_HALF_UP)

    return rate, amount


def calculate_ten_day_total(entries, seasonal=False):
    """Calculate payments and apply the ten-day volume bonus."""
    total_litres = sum(
        (Decimal(str(entry[0])) for entry in entries),
        Decimal("0")
    )

    total_payment = Decimal("0.00")

    for litres, fat, snf in entries:
        _, amount = calculate_payment(litres, fat, snf, seasonal)
        total_payment += amount

    bonus = Decimal("0.00")

    if seasonal and total_litres > BONUS_LIMIT:
        bonus = (total_litres * BONUS_PER_LITRE).quantize(
            CENT, rounding=ROUND_HALF_UP
        )

    return (
        total_litres,
        total_payment.quantize(CENT, rounding=ROUND_HALF_UP),
        bonus,
        (total_payment + bonus).quantize(CENT, rounding=ROUND_HALF_UP),
    )


def run_tests():
    """Test original rates, seasonal rates and the volume bonus."""

    print("TASK 12 - SEASONAL RATE TESTS")
    print("-" * 55)

    # Test the original rate card
    rate, payment = calculate_payment("10", "3.50", "8.50")
    assert rate == Decimal("30.00")
    assert payment == Decimal("300.00")
    print(f"Original rate: Rs. {rate} per litre; payment Rs. {payment}")

    # Test April-June rate card
    rate, payment = calculate_payment(
        "10", "3.50", "8.50", seasonal=True
    )
    assert rate == Decimal("32.00")
    assert payment == Decimal("320.00")
    print(f"Seasonal rate: Rs. {rate} per litre; payment Rs. {payment}")

    # Test two-decimal analyser readings
    rate, payment = calculate_payment(
        "10", "3.56", "8.54", seasonal=True
    )
    assert rate == Decimal("32.45")
    assert payment == Decimal("324.50")
    print(f"Two-decimal readings: rate Rs. {rate}; payment Rs. {payment}")

    # More than 500 litres: bonus applies
    entries_over_limit = [
        ("300", "3.50", "8.50"),
        ("201", "3.50", "8.50"),
    ]
    litres, subtotal, bonus, final_total = calculate_ten_day_total(
        entries_over_limit, seasonal=True
    )
    assert litres == Decimal("501")
    assert subtotal == Decimal("16032.00")
    assert bonus == Decimal("250.50")
    assert final_total == Decimal("16282.50")
    print(
        f"501 L: subtotal Rs. {subtotal}; bonus Rs. {bonus}; "
        f"total Rs. {final_total}"
    )

    # Exactly 500 litres: no bonus
    entries_at_limit = [("500", "3.50", "8.50")]
    litres, subtotal, bonus, final_total = calculate_ten_day_total(
        entries_at_limit, seasonal=True
    )
    assert litres == Decimal("500")
    assert bonus == Decimal("0.00")
    assert final_total == Decimal("16000.00")
    print(
        f"500 L: subtotal Rs. {subtotal}; bonus Rs. {bonus}; "
        f"total Rs. {final_total}"
    )

    print("\nAll Task 12 tests passed!")


if __name__ == "__main__":
    run_tests()
