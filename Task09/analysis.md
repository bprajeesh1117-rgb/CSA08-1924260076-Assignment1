# Task 9 – Implementation and Test Results

## 1. Test Table (Expected vs Actual)

| Test Case Type | Input Data (Litres, Fat, SNF) | Expected Output / Behavior | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Normal (Above Standard)** | 10.0 L, 4.0% Fat, 8.8% SNF | Rate: Rs. 33.40, Pay: Rs. 334.00 | Rate: Rs. 33.40, Pay: Rs. 334.00 | Pass |
| **Normal (Below Standard)** | 12.0 L, 3.1% Fat, 8.3% SNF | Rate: Rs. 27.80, Pay: Rs. 333.60 | Rate: Rs. 27.80, Pay: Rs. 333.60 | Pass |
| **Boundary Entry** | 10.0 L, 3.5% Fat, 8.5% SNF | Rate: Rs. 30.00, Pay: Rs. 300.00 | Rate: Rs. 30.00, Pay: Rs. 300.00 | Pass |
| **Invalid Entry (Negative)** | -5.0 L, 4.0% Fat, 8.5% SNF | Error / Rejection (Negative Quantity) | Handled / Rejected | Pass |
| **Invalid Entry (Text)** | "abc" L, 4.0% Fat, 8.5% SNF | ValueError / Type Conversion Error | Caught via Input Validation | Pass |

## 2. Testing Summary
- All boundary values, normal operating points, and invalid exception entries were successfully tested.
- The use of the `decimal` module ensured zero rounding discrepancies across test cases.