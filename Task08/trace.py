from decimal import Decimal

def debug_milk_calculation(litres, fat, snf):
    print(f"[DEBUG] Input Litres: {litres}, Fat: {fat}, SNF: {snf}")
    base_rate = Decimal("30.00")
    
    fat_diff = fat - Decimal("3.5")
    snf_diff = snf - Decimal("8.5")
    
    rate = base_rate + (fat_diff / Decimal("0.1") * Decimal("0.40")) + (snf_diff / Decimal("0.1") * Decimal("0.30"))
    print(f"[DEBUG] Calculated Rate per Litre: {rate}")
    
    total_amount = rate * litres
    print(f"[DEBUG] Total Payout Amount: {total_amount}")
    return total_amount

if __name__ == "__main__":
    debug_milk_calculation(Decimal("10.0"), Decimal("4.0"), Decimal("8.8"))