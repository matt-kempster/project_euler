#!/usr/bin/env python3

# 112700000 after a minute
import cProfile
import itertools
import math
from typing import Optional, Tuple


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def is_semiprime(n) -> Optional[Tuple[int, int]]:
    for factor1 in range(2, int(math.sqrt(n)) + 1):
        if n % factor1 == 0:
            if is_prime(factor1) and is_prime(n / factor1):
                return (factor1, int(n / factor1))
    return None


# x^2 - D y^2 = 1
# x^2 - 1 = D y^2
# (x + 1)(x - 1) = ...
# for prime D:
# step 2i:
#   x + 1 = D * i
#   x = D * i - 1
# step 2i+1:
#   x - 1 = D * i
#   x = D * i + 1
#
# so, try {D-1, D+1, 2D-1, 2D+1, 3D-1, 3D+1...}


def gen_for_prime(D: int):
    x1 = D - 1
    y_squared1 = ((x1 ** 2) - 1) / D
    x2 = D + 1
    y_squared2 = ((x2 ** 2) - 1) / D
    while True:
        yield x1, y_squared1
        yield x2, y_squared2
        y_squared1 += D + 2 * x1
        x1 += D
        y_squared2 += D + 2 * x2
        x2 += D


def gen_for_semiprime(D: int, factor1: int, factor2: int):
    # note factor1 < factor2
    # 4 cases total each
    for i in itertools.count(1):
        for value in sorted(
            [(i * factor1 + 1), (i * factor2 + 1), i * D - 1, i * D + 1]
        ):
            yield value


def is_square(x: int) -> bool:
    return math.sqrt(x).is_integer()
    # return int(math.sqrt(x)) ** 2 == x


def largest_min_x(D: int) -> int:
    if not is_prime(D):
        print("temporarily broken")
        return 0

    counter = itertools.count(2)
    if is_prime(D):
        counter = gen_for_prime(D)
    else:
        factors = is_semiprime(D)
        if factors:
            counter = gen_for_semiprime(D, factors[0], factors[1])

    for i, (x, y_squared) in enumerate(counter):
        if i % 1000000 == 0:
            print(f"tried {x}")
        if is_square(y_squared):
            return x


if _name_ == "_main_":
    cProfile.run("largest_min_x(61)")
    # for D in range(1000):
    #     if is_square(D):
    #         continue

    #     x = largest_min_x(D)
    #     print(f"D={D}, x={x}")
