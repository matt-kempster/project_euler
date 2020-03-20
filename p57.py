#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Fraction:
    numerator: int
    denominator: int


def flip(frac: Fraction) -> Fraction:
    return Fraction(frac.denominator, frac.numerator)


def increment(frac: Fraction) -> Fraction:
    return Fraction(frac.numerator + frac.denominator, frac.denominator)


def next_expansion(prev: Fraction) -> Fraction:
    # add one, flip, add one:
    return increment(flip(increment(prev)))


def numerator_heavy(frac: Fraction):
    return len(str(frac.numerator)) > len(str(frac.denominator))


numerator_heavy_expansions = 0
expansion = Fraction(3, 2)
for idx in range(1000):
    expansion = next_expansion(expansion)
    numerator_heavy_expansions += 1 if numerator_heavy(expansion) else 0
    if idx % 5 == 0:
        print(f"{idx=}: {numerator_heavy_expansions=}")
print(f"final: {numerator_heavy_expansions}")
