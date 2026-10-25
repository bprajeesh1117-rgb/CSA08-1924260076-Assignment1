# Task 2 – Explore Values and Types in the Interpreter

## 1. Python Data Types

The `type()` function identifies the type of a value.

| Value | Type |
|---|---|
| `10` | `int` |
| `10.0` | `float` |
| `"10"` | `str` |
| `True` | `bool` |
| `[10, 8.5]` | `list` |

An integer stores a whole number, a float stores a floating-point number, a string stores text, a Boolean represents `True` or `False`, and a list stores multiple values.

## 2. Division Operators

- `7 / 2` returns `3.5` because `/` performs true division.
- `7 // 2` returns `3` because `//` performs floor division.
- `7 % 2` returns `1` because `%` gives the remainder.
- `-7 // 2` returns `-4` because floor division rounds toward negative infinity.

## 3. Floating-Point Precision

The expression `0.1 + 0.2 == 0.3` returns `False`. Binary floating-point arithmetic cannot represent many decimal fractions exactly, so the calculated result is slightly different from `0.3`.

## 4. Float and Decimal Comparison

The program adds 1,000 payments of Rs. 33.40 and three adjustments of Rs. 0.10.

The expected mathematical total is Rs. 33,400.30.

Using `float` produces a small precision error, while `Decimal` constructed from strings produces `33400.30` exactly for these decimal inputs.

## 5. Creating Decimal Values

`Decimal("0.1")` preserves the intended decimal value. In contrast, `Decimal(float("0.1"))` captures the existing binary floating-point approximation and produces a long decimal representation.

Therefore, monetary values should be created from strings using `Decimal`, rather than from floats.

## 6. Alternative Concept and Complexity Analysis

An alternative is to store money as integer paise. For example, Rs. 33.40 becomes 3,340 paise, and Rs. 0.10 becomes 10 paise. Integer addition is exact when amounts are represented as whole paise.

Using `round()` after every float addition does not necessarily guarantee an exact bank total because rounding at intermediate stages can change the result.

Both the float and Decimal summation methods take O(n) time for n payments and O(1) additional summation space, excluding the input list. The memory occupied by a value can be inspected using `sys.getsizeof()`.

## Conclusion

`Decimal` created from strings or integer paise is more suitable than ordinary float arithmetic for accurate financial calculations.