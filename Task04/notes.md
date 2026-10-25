
# Task 4 – Write Correct Expressions

## 1. Expressions for the Milk Payment

The number of fat steps is:

    fat_steps = round((fat - 3.5) / 0.1)

The number of SNF steps is:

    snf_steps = round((snf - 8.5) / 0.1)

The rate per litre is:

    rate = 30.00 + fat_steps * 0.40 + snf_steps * 0.30

The payment is:

    amount = round(litres * rate, 2)

The parentheses calculate the difference from the standard percentage before division. The `round()` function converts the calculated step count to the nearest integer.

## 2. Operator Precedence and Associativity

Python evaluates parentheses before multiplication and division, and multiplication before addition and subtraction.

For example:

    -2 ** 2

returns `-4` because exponentiation is evaluated before unary minus.

However:

    (-2) ** 2

returns `4` because the parentheses make the negative number the base.

Operators at the same precedence level are generally evaluated according to their associativity rules.

## 3. Floating-Point Precision

The expression:

    (4.2 - 3.5) / 0.1

may produce `7.000000000000001` instead of exactly `7.0`. This happens because binary floating-point cannot represent many decimal fractions exactly.

Using `round()` gives the intended step count of 7.

Another example is:

    0.1 + 0.2 == 0.3

which returns `False` because the computed floating-point sum is not exactly equal to the stored representation of `0.3`.

## 4. Difference Between round(), int() and math.floor()

- `round(x)` returns the nearest integer, using ties-to-even for exact halfway cases.
- `int(x)` removes the fractional part by truncating toward zero.
- `math.floor(x)` returns the greatest integer less than or equal to the value.

For the fat step calculation with fat = 4.2%, the calculated value is approximately 7.000000000000001. All three methods produce 7.

For fat = 3.1%, the calculated value is approximately -3.9999999999999996:

- `round()` gives -4.
- `int()` gives -3.
- `math.floor()` gives -4.

With SNF fixed at 8.5%, the resulting rates are:

| Fat | Method | Fat steps | Rate per litre |
|---|---|---:|---:|
| 4.2% | round() | 7 | Rs. 32.80 |
| 4.2% | int() | 7 | Rs. 32.80 |
| 4.2% | math.floor() | 7 | Rs. 32.80 |
| 3.1% | round() | -4 | Rs. 28.40 |
| 3.1% | int() | -3 | Rs. 28.80 |
| 3.1% | math.floor() | -4 | Rs. 28.40 |

Thus, `int()` can produce an incorrect step count for negative differences because it truncates toward zero.

## 5. Comparison Chaining and Boolean Operators

Python allows chained comparisons:

    2.0 <= fat <= 7.0

This checks that fat is at least 2.0% and at most 7.0%.

Boolean operators combine conditions:

- `and` is true only when both conditions are true.
- `or` is true when at least one condition is true.
- `not` reverses a Boolean result.

For example:

    2.0 <= fat <= 7.0 and snf == 8.5

checks both conditions together.

## 6. Alternative Concept and Complexity Analysis

An alternative is to use `int()` or `math.floor()` instead of `round()` to calculate the steps.

Using `int()` truncates negative values toward zero and can produce the wrong rate, as shown for fat = 3.1%. Using `math.floor()` produces -4 for that example, but its behaviour differs from `round()` for other fractional values. The assignment's specified approach is to round the number of steps to the nearest whole step.

Each method performs a fixed number of arithmetic operations, so its time complexity is O(1). Each uses a fixed number of variables, so its additional space complexity is O(1).

## Conclusion

Correct parentheses, step rounding and operator precedence are important for accurate milk payments. The tested examples show why `round()` is preferable to `int()` for the assignment's step calculation.
