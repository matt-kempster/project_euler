#!/usr/bin/env python3
import math
from decimal import Decimal, getcontext
from typing import Optional


def gen_orbit(root: Decimal):
    next_frac = root
    while True:
        addend = math.floor(next_frac)
        yield addend
        next_frac = 1 / (next_frac - addend)


def get_period(root: Decimal) -> int:
    first_term: Optional[int] = None
    for i, term in enumerate(gen_orbit(root)):
        if i == 0:
            first_term = term
        if first_term and term == 2 * first_term:
            # check_symmetry()
            return i


if _name_ == "_main_":
    getcontext().prec = 600
    odd_periods = 0
    for n in range(2, 10_001):
        if n % 1000 == 0:
            print(f"done with {n}")

        root = Decimal(n).sqrt()
        if int(root) ** 2 == n:
            continue

        period = get_period(root)
        if period % 2 == 1:
            odd_periods += 1
    print(odd_periods)
