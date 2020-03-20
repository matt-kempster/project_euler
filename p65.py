#!/usr/bin/env python3
import itertools
import math
from fractions import Fraction
from typing import List


def get_orbit(frac: Fraction, length: int = 100) -> List[int]:
    next_frac: Fraction = frac
    orbit = []
    while len(orbit) < length:
        addend = math.floor(next_frac)
        orbit.append(addend)
        next_frac = 1 / Fraction(next_frac - addend)
    return orbit


def calculate_e() -> Fraction:
    curr_euler = Fraction(1)
    factorial = Fraction(1)
    for n in itertools.count(1):
        factorial *= n
        if factorial > Fraction(10 ** 300):
            break
        delta = Fraction(1) / factorial
        curr_euler += delta
    return curr_euler


if _name_ == "_main_":
    euler = calculate_e()
    orbit = get_orbit(euler)
    running_frac = Fraction(0)
    for term in reversed(orbit):
        running_frac = Fraction(1, term + running_frac)
    numerator = Fraction(1, running_frac).numerator
    print(sum(int(digit) for digit in str(numerator)))
