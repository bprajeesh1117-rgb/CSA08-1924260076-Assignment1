
"""Task 5: Read input and convert types."""


def read_number(prompt):
    """Read a numeric value and handle invalid input."""
    while True:
        text = input(prompt).strip()

        try:
            return float(text)
        except ValueError:
            print("Invalid number. Enter a number using a decimal point, e.g. 8.5.")


def read_milk_entry():
    """Read and validate one farmer's milk entry."""
    farmer_id = input("Enter farmer ID: ").strip()

    while not farmer_id:
        print("Farmer ID cannot be empty.")
        farmer_id = input("Enter farmer ID: ").strip()

    litres = read_number("Enter milk quantity in litres: ")
    while litres <= 0:
        print("Quantity must be greater than zero.")
        litres = read_number("Enter milk quantity in litres: ")

    fat = read_number("Enter fat percentage: ")
    while not 2.0 <= fat <= 7.0:
        print("Fat must be between 2.0% and 7.0%.")
        fat = read_number("Enter fat percentage: ")

    snf = read_number("Enter SNF percentage: ")

    shift = input("Enter shift (Morning/Evening): ").strip().title()
    while shift not in ("Morning", "Evening"):
        print("Shift must be Morning or Evening.")
        shift = input("Enter shift (Morning/Evening): ").strip().title()

    return farmer_id, litres, fat, snf, shift


def calculate_rate(fat, snf):
    """Calculate the rate per litre using the standard rate card."""
    base_rate = 30.00
    standard_fat = 3.5
    standard_snf = 8.5
    fat_step_value = 0.40
    snf_step_value = 0.30

    fat_steps = round((fat - standard_fat) / 0.1)
    snf_steps = round((snf - standard_snf) / 0.1)

    return round(
        base_rate
        + fat_steps * fat_step_value
        + snf_steps * snf_step_value,
        2
    )


def main():
    """Read an entry and display its calculated payment."""
    print("Ksheera Village Milk Co-operative")
    print("-" * 55)

    farmer_id, litres, fat, snf, shift = read_milk_entry()

    rate = calculate_rate(fat, snf)
    amount = round(litres * rate, 2)

    print("\nPAYMENT DETAILS")
    print("-" * 55)
    print(f"{'Farmer ID':<20}: {farmer_id}")
    print(f"{'Quantity (litres)':<20}: {litres:8.2f}")
    print(f"{'Fat (%)':<20}: {fat:8.2f}")
    print(f"{'SNF (%)':<20}: {snf:8.2f}")
    print(f"{'Shift':<20}: {shift}")
    print(f"{'Rate per litre (Rs.)':<20}: {rate:8.2f}")
    print(f"{'Payment (Rs.)':<20}: {amount:8.2f}")


if __name__ == "__main__":
    main()
