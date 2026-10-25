# Task 12 – Re-evaluate and Adapt the Design

## A. Impact Analysis

The new requirements introduce two-decimal analyser readings, an April–June base rate of Rs. 32.00, a fat-step value of Rs. 0.45 and a bonus of Rs. 0.50 per litre when the ten-day supply exceeds 500 litres.

The rate constants and rate calculation function are affected. The ten-day total function must also calculate the total litres and apply the bonus only when the limit is exceeded.

## B. Evaluation of the Original Design

The original design remains useful because its calculation functions and modular structure can be reused. However, the original rate constants cannot represent the seasonal rates by themselves.

The revised program uses `Decimal` for decimal arithmetic and `ROUND_HALF_UP` to calculate the nearest 0.1 percentage-point step and round money to two decimal places.

For example, with seasonal rates and fat 3.56%, SNF 8.54%, and 10 litres, the fat reading rounds to one step above standard while the SNF reading rounds to zero steps. The rate is Rs. 32.45 per litre and the payment is Rs. 324.50.

## C. Adaptation

The program now has separate original and seasonal rate constants. The `seasonal` parameter selects the applicable rate card. The `calculate_ten_day_total()` function calculates the ten-day volume and applies the bonus only when total supply is greater than 500 litres.

## D. Evidence-Based Defence

The tests verify the original rate, the seasonal rate, two-decimal analyser readings, a 501-litre supply that receives the bonus, and a 500-litre supply that does not.

The revised design avoids duplicating the calculation logic. Its main limitation is that the caller must select the correct season explicitly; a production system should select the rate card using the actual payment period and should retain an auditable record of the rate card used.

## Conclusion

The original design is modified rather than completely redesigned. Its modular structure is retained, while the rate card, decimal arithmetic and ten-day bonus calculation are adapted to satisfy the new requirements.