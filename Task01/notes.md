# Task 1 – Understand the Problem and Identify the Data

## 1. Inputs and Outputs

### Inputs
- **Farmer ID:** Identifies each farmer and is stored as a string (`str`).
- **Milk quantity:** The quantity of milk supplied in litres, stored as a floating-point value (`float`) in the introductory program.
- **Fat percentage:** The fat content of the milk, stored as a `float`.
- **SNF percentage:** The solids-not-fat content of the milk, stored as a `float`.
- **Shift:** Represents the morning or evening collection and is stored as a string (`str`).

### Outputs
- **Rate per litre:** The price calculated using the fat and SNF percentages.
- **Payment amount:** The amount payable for the milk supplied.
- **Ten-day total:** The sum of a farmer's payments over ten days.

## 2. Named Constants

The following constants are used in the program:

| Constant | Value | Purpose |
|---|---:|---|
| `BASE_RATE` | Rs. 30.00 | Standard price per litre |
| `STANDARD_FAT` | 3.5% | Reference fat percentage |
| `STANDARD_SNF` | 8.5% | Reference SNF percentage |
| `FAT_STEP_VALUE` | Rs. 0.40 | Rate adjustment per 0.1% fat change |
| `SNF_STEP_VALUE` | Rs. 0.30 | Rate adjustment per 0.1% SNF change |
| `FAT_STEP_PERCENT` | 0.1% | Fat adjustment interval |
| `SNF_STEP_PERCENT` | 0.1% | SNF adjustment interval |

Named constants avoid repeating rate values throughout the program. If the co-operative changes its rates, the relevant constants can be updated in one place.

## 3. Data Types

- **Integer (`int`):** Used for whole-number values, such as the number of farmers.
- **Float (`float`):** Used for fractional milk quantities and percentage readings in this introductory implementation.
- **String (`str`):** Used for farmer IDs and shift names.
- **Boolean (`bool`):** Used for validation results, such as whether a quantity is positive.
- **List (`list`):** Stores multiple farmer records.
- **Tuple (`tuple`):** Stores the details of one farmer as a grouped record.

These data types are selected according to the nature of each value.

## 4. Validation Rules

1. Milk quantity must be greater than zero.
2. Fat percentage must be between 2.0% and 7.0%, inclusive.
3. Farmer ID must not be empty.
4. Shift must identify a valid collection shift.
5. Rate adjustments must follow the specified 0.1 percentage-point intervals.

The assignment does not specify an allowed SNF range, so an additional SNF limit should be confirmed before it is enforced.

## 5. Assumptions

- The standard rate is Rs. 30.00 per litre at 3.5% fat and 8.5% SNF.
- Every 0.1% change in fat adjusts the rate by Rs. 0.40 per litre.
- Every 0.1% change in SNF adjusts the rate by Rs. 0.30 per litre.
- The introductory program uses `float` and displays payments to two decimal places.
- More accurate financial calculations will be considered in later tasks.

## 6. Alternative Concept and Complexity Analysis

If separate variables such as `litres1`, `fat1`, and `snf1` were created for every farmer, the program would become difficult to maintain as the number of farmers increased to 300, 6,000, or 150,000.

Using a list of tuples allows the program to process every farmer using the same loop.

For `n` farmer records:

- **Time complexity:** O(n), because each record is processed once.
- **Space complexity:** O(n), because all records are stored in a list.

Therefore, the list-based approach is easier to extend, process, validate, and maintain than using separate variables for every farmer.