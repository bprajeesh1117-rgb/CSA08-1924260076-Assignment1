# Task 4 – Implement Basic Input and Output

def collect_milk_entry():
    print("--- Village Milk Co-operative Collection ---")
    
    # 1. Take inputs from the user
    farmer_id = input("Enter Farmer ID: ")
    quantity = float(input("Enter Milk Quantity (Litres): "))
    fat_pct = float(input("Enter Fat Percentage (%): "))
    snf_pct = float(input("Enter SNF Percentage (%): "))
    
    # 2. Display the collected data neatly formatted
    print("\n--- Collection Summary ---")
    print(f"Farmer ID    : {farmer_id}")
    print(f"Quantity     : {quantity:.2f} Litres")
    print(f"Fat %        : {fat_pct:.2f}%")
    print(f"SNF %        : {snf_pct:.2f}%")

if __name__ == "__main__":
    collect_milk_entry()