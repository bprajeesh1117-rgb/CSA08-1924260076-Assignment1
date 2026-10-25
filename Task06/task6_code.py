from decimal import Decimal

def calculate_payout(litres, fat, snf):
    base_rate = Decimal("30.00")
    rate = base_rate + ((fat - Decimal("3.5")) / Decimal("0.1") * Decimal("0.40")) + \
           ((snf - Decimal("8.5")) / Decimal("0.1") * Decimal("0.30"))
    return rate, rate * litres

if __name__ == "__main__":
    print("--- 10-Day Collection Summary Loop ---")
    
    # Sample 3-day data entries (Litres, Fat, SNF)
    collections = [
        (Decimal("10.5"), Decimal("3.8"), Decimal("8.6")),
        (Decimal("12.0"), Decimal("4.0"), Decimal("8.8")),
        (Decimal("9.5"), Decimal("3.5"), Decimal("8.5"))
    ]
    
    total_litres = Decimal("0.0")
    total_payout = Decimal("0.0")
    
    for i, data in enumerate(collections, start=1):
        litres, fat, snf = data
        rate, amount = calculate_payout(litres, fat, snf)
        total_litres += litres
        total_payout += amount
        print(f"Day {i}: {litres}L | Rate: Rs.{rate:.2f} | Amount: Rs.{amount:.2f}")
        
    print("-" * 40)
    print(f"Total Litres Delivered : {total_litres}L")
    print(f"Total Cumulative Payout: Rs. {total_payout:.2f}")
    