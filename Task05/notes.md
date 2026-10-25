
# Task 5 – Read Input and Convert Types

## 1. Reading and Converting Input

Python's `input()` function always returns a string (`str`), even if the user types a number.

For example:

    text = input("Enter litres: ")
    litres = float(text)

The `float()` function converts numeric text into a floating-point value. The `int()` function converts suitable numeric text into an integer.

## 2. Handling Invalid Input

If the clerk enters `"eight"` or `"8,5"`, `float()` raises a `ValueError` because these strings are not valid Python floating-point literals.

The program uses `try/except ValueError` to catch the error, display a helpful message and ask again. The accepted decimal format uses a dot, such as `8.5`.

The program also checks that the farmer ID is not empty, the quantity is positive, the fat percentage is between 2.0% and 7.0%, and the shift is Morning or Evening. The assignment does not specify an SNF range, so the program checks that SNF is numeric without inventing a limit.

## 3. Alternative: Checking Text Before Conversion

An alternative is to inspect the input string before conversion using string methods or a custom validation function. However, validating every possible numeric format manually is complicated, especially for decimal points, signs and whitespace.

Using `try/except ValueError` lets Python perform the conversion and reports invalid numeric text through an exception.

Both approaches take O(1) time for an ordinary input string of bounded length. For a string of length m, parsing and validation can take O(m) time. The exception approach is clearer for general numeric conversion, while simple string checks may be useful for specific input formats.

## 4. Formatted Output

F-strings format the output into readable columns. For example:

    print(f"{'Payment (Rs.)':<20}: {amount:8.2f}")

The `<20` expression left-aligns the label in a field of width 20. The `8.2f` expression displays the amount in a field of width 8 with two digits after the decimal point.

## 5. Complexity Analysis

Reading and validating a single entry takes O(1) time when input lengths are bounded, and uses O(1) additional space. If invalid entries are repeatedly entered, the total time increases with the number of attempts.

For n farmer entries, processing all entries takes O(n) time, excluding time spent waiting for user input.

## Conclusion

The program converts strings to numeric values, handles invalid entries without crashing, validates the required fields and formats payment details neatly. The `try/except ValueError` approach provides a simple and reliable way to handle incorrect numeric input.
