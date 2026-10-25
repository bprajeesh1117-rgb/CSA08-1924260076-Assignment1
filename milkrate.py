from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")

def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    rate = BASE_RATE + (Decimal(str(fat_steps)) * FAT_STEP_VALUE) + (Decimal(str(snf_steps)) * SNF_STEP_VALUE)
    return rate.quantize(Decimal("0.01"))

def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    amount = Decimal(str(litres)) * rate
    return amount.quantize(Decimal("0.01"))

if __name__ == "__main__":
    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:
        rate, pay = rate_per_litre(fat, snf), payout(litres, fat, snf)
        print(f"{litres:5} L  fat {fat}  snf {snf}  rate {rate:6.2f}  pay {pay:8.2f}")