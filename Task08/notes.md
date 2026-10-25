# Task 8 – Plan the Algorithm Before Coding

## Algorithmic Problem Solving
The four steps are:
1. Understand the problem and identify inputs and outputs.
2. Plan the solution using pseudocode and a flowchart.
3. Write the Python program.
4. Test the program using sample entries.

## Flowchart
The flowchart in `flowchart.md` validates numeric input, checks that quantity is positive and fat is between 2.0% and 7.0%, then calculates and displays the payment.

## Hand Trace
| Entry | Litres | Fat | SNF | Rate (Rs.) | Payment (Rs.) |
|---|---:|---:|---:|---:|---:|
| 1 | 10 | 3.5 | 8.5 | 30.00 | 300.00 |
| 2 | 8.5 | 4.2 | 8.7 | 33.40 | 283.90 |
| 3 | 12 | 3.1 | 8.3 | 27.80 | 333.60 |
| **Total** | | | | | **917.50** |

## Alternative Approaches
**Store all entries:** Store each entry in a list and calculate the total at the end. Time complexity is O(n), and space complexity is O(n).

**Running total:** Calculate each payment as it is entered and add it immediately to the total. Time complexity is O(n), with O(1) extra space for the running total.

Storing entries is useful when they must be reviewed, corrected or processed again.

## Conclusion
Pseudocode, a flowchart and a hand trace help plan and verify the payment algorithm before implementation.