# Task 6 – Organise the Logic into Functions

## Aim
To divide the milk payment calculation into reusable functions with parameters, return values and docstrings.

## Functions used

| Function | Parameters | Return value |
|---|---|---|
| `rate_per_litre(fat, snf)` | Fat and SNF percentages | Rate per litre rounded to two decimal places |
| `payout(litres, fat, snf)` | Quantity, fat and SNF | Payment rounded to two decimal places |
| `ten_day_total(entries)` | Collection of milk entries | Total payment rounded to two decimal places |

The `main()` function runs the sample calculations and displays the results.

## Return versus print

`return` sends a calculated value back to the caller so it can be stored, reused or included in another calculation. `print()` only displays information on the screen. For example, `payout()` returns an amount that can be added to the ten-day total.

## Local and global scope

The rate constants (`BASE_RATE`, `STANDARD_FAT`, `STANDARD_SNF`, `FAT_STEP_VALUE` and `SNF_STEP_VALUE`) are global names that the functions can read. Variables such as `fat_steps`, `snf_steps`, `rate` and `total` are local to their respective functions.

The constants should not be reassigned inside the functions. Keeping the rate values in one place makes future rate revisions easier.

## Docstrings

Each function has a docstring describing its purpose. Docstrings help other programmers understand how to use the functions.

## Alternative approach

If the calculation were written as one long script, the same formulas might be repeated for each entry. This increases duplication and makes corrections harder. Lambda expressions could represent short calculations, but they are less suitable for several steps of validation and calculation.

## Complexity analysis

For `n` milk entries:

- **Time complexity:** O(n), because each entry is processed once.
- **Space complexity:** O(n) for storing the input entries; the calculation itself uses O(1) additional space.
- **Function-call overhead:** Function calls have a small overhead, but for `n` entries the overall time remains O(n). The improved readability and reuse are more valuable than this small overhead.

## Test results

| Litres | Fat (%) | SNF (%) | Rate (Rs.) | Payment (Rs.) |
|---:|---:|---:|---:|---:|
| 10 | 3.5 | 8.5 | 30.00 | 300.00 |
| 8.5 | 4.2 | 8.7 | 33.40 | 283.90 |
| 12 | 3.1 | 8.3 | 27.80 | 333.60 |
| **Total** | | | | **917.50** |

**Conclusion:** The program organises the calculations into reusable functions, returns values for further calculations and keeps the rate constants in one place.