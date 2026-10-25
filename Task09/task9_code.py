
"""Task 9: Implement and test the milk payment calculator."""

import sys
from pathlib import Path

# Import milkrate.py from the project root
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import milkrate


def validate_entry(litres, fat, snf):
    """Validate quantity, fat and SNF values."""

    if not all(isinstance(v, (int, float)) for v in (litres, fat, snf)):
        raise ValueError("Quantity, fat and SNF must be numeric.")

    if not all(
        v == v and abs(v) != float("inf")
        for v in (litres, fat, snf)
    ):
        raise ValueError("Values must be finite numbers.")

    if litres <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if not 2.0 <= fat <= 7.0:
        raise ValueError("Fat must be between 2.0% and 7.0%.")


def calculate_payment(litres, fat, snf):
    """Validate an entry and calculate its payment."""
    validate_entry(litres, fat, snf)
    return milkrate.payout(litres, fat, snf)


def run_tests():
    """Test normal, boundary and invalid entries."""

    valid_tests = [
        ("Standard values", 10, 3.5, 8.5, 300.00),
        ("Fat and SNF above standard", 8.5, 4.2, 8.7, 283.90),
        ("Fat and SNF below standard", 12, 3.1, 8.3, 333.60),
        ("Fat above, SNF below", 10, 4.0, 8.3, 314.00),
        ("Fat below, SNF above", 10, 3.0, 8.7, 286.00),
        ("Minimum fat", 10, 2.0, 8.5, 240.00),
        ("Maximum fat", 10, 7.0, 8.5, 440.00),
    ]

    print("TASK 9 - VALID TESTS")
    print("-" * 75)

    for name, litres, fat, snf, expected in valid_tests:
        actual = calculate_payment(litres, fat, snf)

        assert abs(actual - expected) < 0.001, (
            f"{name}: expected {expected:.2f}, got {actual:.2f}"
        )

        print(
            f"{name:<32} Expected: {expected:8.2f} "
            f"Actual: {actual:8.2f} PASS"
        )

    invalid_tests = [
        ("Negative quantity", -1, 3.5, 8.5),
        ("Fat below minimum", 10, 1.9, 8.5),
        ("Fat above maximum", 10, 7.1, 8.5),
        ("Text quantity", "eight", 3.5, 8.5),
    ]

    print("\nTASK 9 - INVALID TESTS")
    print("-" * 75)

    for name, litres, fat, snf in invalid_tests:
        try:
            calculate_payment(litres, fat, snf)
        except (ValueError, TypeError):
            print(f"{name:<32} Rejected PASS")
        else:
            raise AssertionError(f"{name} should have been rejected.")

    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3),
        (10, 4.0, 8.3),
        (10, 3.0, 8.7),
    ]

    expected_total = 1517.50
    actual_total = round(
        sum(calculate_payment(*entry) for entry in entries), 2
    )

    assert abs(actual_total - expected_total) < 0.001, (
        f"Expected total {expected_total:.2f}, got {actual_total:.2f}"
    )

    print("\nTASK 9 - FIVE-ENTRY TOTAL")
    print(f"Expected: Rs. {expected_total:.2f}")
    print(f"Actual:   Rs. {actual_total:.2f}")
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()


