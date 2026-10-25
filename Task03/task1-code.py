
"""Task 3: Choose Variables and Name the Constants."""

# Named constants: define rate values and limits in one place.
BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
FAT_STEP_PERCENT = 0.1
SNF_STEP_PERCENT = 0.1
MIN_FAT = 2.0
MAX_FAT = 7.0

print("TASK 3 - VARIABLES AND CONSTANTS")
print("-" * 40)

print("Base rate       :", BASE_RATE)
print("Standard fat    :", STANDARD_FAT)
print("Standard SNF    :", STANDARD_SNF)
print("Fat step value  :", FAT_STEP_VALUE)
print("SNF step value  :", SNF_STEP_VALUE)
print("Fat limits      :", MIN_FAT, "to", MAX_FAT)

# Example calculation using named constants.
fat = 4.2
snf = 8.7

fat_steps = round((fat - STANDARD_FAT) / FAT_STEP_PERCENT)
snf_steps = round((snf - STANDARD_SNF) / SNF_STEP_PERCENT)

rate = (
    BASE_RATE
    + fat_steps * FAT_STEP_VALUE
    + snf_steps * SNF_STEP_VALUE
)

print("\nRate using named constants:", f"Rs. {rate:.2f}")

# Dynamic typing: a variable can refer to different types.
value = 100
print("\nBefore reassignment:", value, type(value).__name__)

value = "100"
print("After reassignment :", value, type(value).__name__)

# Multiple assignment and swapping.
a, b = 10, 20
print("\nBefore swapping: a =", a, "b =", b)

a, b = b, a
print("After swapping : a =", a, "b =", b)

# Alternative 1: magic numbers typed directly in the expression.
magic_rate = 30.00 + 7 * 0.40 + 2 * 0.30
print("\nRate using magic numbers:", f"Rs. {magic_rate:.2f}")

# Alternative 2: rate values stored in a dictionary.
RATE_CARD = {
    "base": 30.00,
    "fat": 0.40,
    "snf": 0.30
}

dictionary_rate = (
    RATE_CARD["base"]
    + fat_steps * RATE_CARD["fat"]
    + snf_steps * RATE_CARD["snf"]
)

print("Rate using RATE_CARD   :", f"Rs. {dictionary_rate:.2f}")
