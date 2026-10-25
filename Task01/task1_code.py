
"""Task 1: Understand the Milk Payment Problem."""

# Named constants
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
FAT_STEP_PERCENT = 0.1
SNF_STEP_PERCENT = 0.1

# Farmer records: ID, litres, fat, SNF, shift
farmers = [
    ("F001", 10.0, 3.5, 8.5, "Morning"),
    ("F002", 8.5, 4.2, 8.7, "Evening"),
    ("F003", 12.0, 3.1, 8.3, "Morning")
]

print("KSHEERA VILLAGE MILK CO-OPERATIVE")
print("-" * 45)

for farmer_id, litres, fat, snf, shift in farmers:
    # Calculate fat and SNF steps
    fat_steps = round(
        (fat - STANDARD_FAT) / FAT_STEP_PERCENT
    )
    snf_steps = round(
        (snf - STANDARD_SNF) / SNF_STEP_PERCENT
    )

    # Calculate rate and payment
    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    amount = round(litres * rate, 2)

    # Display the results
    print(f"Farmer ID : {farmer_id}")
    print(f"Litres    : {litres:.2f}")
    print(f"Fat       : {fat:.1f}%")
    print(f"SNF       : {snf:.1f}%")
    print(f"Shift     : {shift}")
    print(f"Rate/Litre: Rs. {rate:.2f}")
    print(f"Payment   : Rs. {amount:.2f}")
    print("-" * 45)

