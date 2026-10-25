# Task 8 – Plan the Algorithm Before Coding

## 1. Algorithmic Problem-Solving Steps

1. **Understand:** Identify the inputs: milk quantity, fat percentage and SNF percentage. The outputs are rate per litre and payment.
2. **Plan:** Write pseudocode and a flowchart before implementation.
3. **Write:** Implement the planned algorithm in Python using the calculation functions.
4. **Test:** Compare expected results with actual results for normal and boundary entries.

## 2. Pseudocode for One Payment

**Algorithm: CalculatePayment**

**Input:** litres, fat, SNF

**Output:** rate per litre and payment amount

1. Set base rate = 30.00.
2. Set standard fat = 3.5 and standard SNF = 8.5.
3. Calculate fat steps = round((fat − 3.5) / 0.1).
4. Calculate SNF steps = round((SNF − 8.5) / 0.1).
5. Calculate rate = 30.00 + (fat steps × 0.40) + (SNF steps × 0.30).
6. Round rate to two decimal places.
7. Calculate payment = litres × rate.
8. Round payment to two decimal places.
9. Display rate and payment.
10. Stop.

## 3. Pseudocode for the Ten-Day Total

**Algorithm: CalculateTenDayTotal**

**Input:** A collection of n milk entries

**Output:** Total payment for the collection period

1. Set total = 0.00.
2. For each milk entry:
   - Calculate its payment using `CalculatePayment`.
   - Add the payment to total.
3. Round total to two decimal places.
4. Display total.
5. Stop.

## 4. Hand Trace of Three Entries

| Entry | Litres | Fat (%) | SNF (%) | Rate (Rs.) | Payment (Rs.) |
|---|---:|---:|---:|---:|---:|
| 1 | 10 | 3.5 | 8.5 | 30.00 | 300.00 |
| 2 | 8.5 | 4.2 | 8.7 | 33.40 | 283.90 |
| 3 | 12 | 3.1 | 8.3 | 27.80 | 333.60 |
| **Total** | | | | | **917.50** |

### Hand calculation

**Entry 1:** Both percentages match the standard values. Rate = Rs. 30.00. Payment = 10 × 30.00 = Rs. 300.00.

**Entry 2:** Fat steps = 7 and SNF steps = 2. Rate = 30.00 + (7 × 0.40) + (2 × 0.30) = Rs. 33.40. Payment = 8.5 × 33.40 = Rs. 283.90.

**Entry 3:** Fat steps = −4 and SNF steps = −2. Rate = 30.00 − (4 × 0.40) − (2 × 0.30) = Rs. 27.80. Payment = 12 × 27.80 = Rs. 333.60.

Total = 300.00 + 283.90 + 333.60 = **Rs. 917.50**.

## 5. Alternative: Store Entries or Keep a Running Total

**Approach A – Store all entries:** Save each entry in a list and calculate the total after reading all entries. Time complexity is O(n), and storage is O(n).

**Approach B – Running total:** Calculate each payment as the entry is read and immediately add it to the total. Time complexity is O(n), and extra storage for the running total is O(1), excluding the current entry.

A list is necessary when the individual entries must be reviewed, corrected, displayed or processed again. A running total is suitable when only the final total is required.