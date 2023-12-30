# --- Day 1: Trebuchet?! ---
## Description (Summarized) [ part a ]
- Aiding elves in fixing issue in global snow production with stars marking locations of problems
    * each puzzle has 1 star, second is unlocked after completing first
- first challenge is to correct a calibration document that has been messed up as a result of a helper who jumbled the calibration values with a mix of integers and string characters
    * on each line, the calibration value is a combo of first and last occurring digits to form single two digit number

## Problem Restated
- we want to decipher the two digit integers for each line and then return the sum of all those numbers added up

## Analysis
- Input: file, input.txt
- Output: int, total_sum
- Data Structures to use:

- Process
    * Function Goal:
        - iterate through lines -> find first and last instances of integers -> combine into two digit (first digit being first integer and vice versa) -> sum for all lines


## Description [ part b ]
- some digits are spelled out with letters, i.e one, two ... are valid digits and now i need to find real first and last digit
    * two1nine is 29
