
# Task 3 – Choose Variables and Name the Constants

## 1. Naming Rules and Conventions

Python variable names can contain letters, digits and underscores, but cannot start with a digit. Names are case-sensitive, and Python keywords cannot be used as variable names.

Variables use lowercase snake_case, such as `farmer_id` and `fat_steps`. Constants use UPPER_CASE, such as `BASE_RATE` and `FAT_STEP_VALUE`.

## 2. Named Constants

The program defines the base rate, standard fat and SNF percentages, step values and fat limits as named constants.

Python does not enforce constants. Uppercase names are a programming convention indicating that these values should not be reassigned. Keeping rates in one place makes rate revisions easier and reduces mistakes.

## 3. Dynamic Typing

Python is dynamically typed. A variable can refer to values of different types during execution.

Example:

    value = 100
    value = "100"

Initially, `value` refers to an integer (`int`). After reassignment, it refers to a string (`str`). The string must be converted before being used in numerical calculations.

## 4. Multiple Assignment and Swapping

Multiple assignment assigns values to multiple variables:

    a, b = 10, 20

Swapping can be performed using:

    a, b = b, a

After swapping, `a` is 20 and `b` is 10. No temporary variable is required.

## 5. Alternative Concept: Magic Numbers

Magic numbers are values written directly inside expressions rather than stored in named constants.

If a rate appears in k different locations, a rate revision may require changing k locations. Missing one location can produce inconsistent calculations. With named constants, the rate is defined once and can normally be revised in one place.

## 6. Alternative Concept: RATE_CARD Dictionary

The rate values can instead be stored in a dictionary:

    RATE_CARD = {
        "base": 30.00,
        "fat": 0.40,
        "snf": 0.30
    }

The program accesses the values using their keys. This groups related rates together and can be useful when the rate card contains many settings.

## 7. Time and Space Complexity

For a fixed number of rate values, accessing named constants or dictionary entries takes O(1) time. The rate calculation also takes O(1) time and O(1) additional space.

For n farmer entries, processing all entries takes O(n) time.

A dictionary uses more memory than separate numeric constants because it stores keys and dictionary structure. Both approaches use O(1) space for a fixed-size rate card.

## Conclusion

Named constants improve readability and make rate revisions easier to maintain. Dynamic typing allows a variable to refer to different types, and multiple assignment makes swapping concise. A dictionary is an alternative for organising rate values.

