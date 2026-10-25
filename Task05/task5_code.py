from decimal import Decimal

# Constants for standard milk quality and pricing
STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
BASE_RATE = Decimal("30.00")
FAT_STEP = Decimal("0.40")
SNF_STEP = Decimal("0.30")

def calculate_milk_rate(fat, snf, quantity):
    # Calculate variations from standard
    fat_diff = fat - STANDARD_FAT
    snf_diff = snf - STANDARD_SNF
    
    # Rate adjustment based on steps (every 0.1% change)
    fat_steps = fat_diff / Decimal("0.1")
    snf_steps = snf_diff / Decimal("0.1")
    
    # Final rate per litre
    rate_per_litre = BASE_RATE + (fat_steps * FAT_STEP) + (snf_steps * SNF_STEP)
    
    # Ensure rate doesn't drop below a minimum threshold
    if rate_per_litre < Decimal("15.00"):
        rate_per_litre = Decimal("15.00")
        
    total_amount = rate_per_litre * quantity
    return rate_per_litre, total_amount

if __name__ == "__main__":
    print("--- Village Milk Payout Calculator ---")
    fat = Decimal("4.0")
    snf = Decimal("8.8")
    litres = Decimal("50.5")
    
    rate, amount = calculate_milk_rate(fat, snf, litres)
    print(f"Rate per Litre: Rs. {rate:.2f}")
    print(f"Total Amount  : Rs. {amount:.2f}")