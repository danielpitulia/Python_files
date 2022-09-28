#!/bin/python3.10
# Date = 2022-09-26
# Code challenge on www.codewars.com to decompose numbers into so called egyptian fractions. For example, decompose("21/23") or "21" "23" or 21/23 should return ["1/2", "1/3", "1/13", "1/359", "1/644046"] Ref: http://en.wikipedia.org/wiki/Egyptian_fraction
# The code works but doesn't have the correct precision to pass the tests. Will maybe look into this later.
import math

def decompose(fraction):
    decimal_value = eval(fraction)
    if decimal_value == 0:
        return ""
    if decimal_value >= 1:
        return int(decimal_value)

    denominator = 2
    decomposition = "0"
    rest = decimal_value

    while rest > 1e-10:
        next_fraction = f"+1/{str(denominator)}"
        if eval(decomposition + next_fraction) <= decimal_value:
            decomposition += next_fraction
            print(decomposition)

        rest = decimal_value - eval(decomposition)
        if rest != 0:
            denominator = math.ceil(1/rest)

    return decomposition[2:].split("+")

print(decompose("0.66"))
