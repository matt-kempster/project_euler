#!/usr/bin/env python3
# want a ** b to be b digits long
# len(str(a ** b)) == b
# left-hand side equals ceil(b * log(a, base=10))
# which means that log(a, base=10) needs to be close to 1
# which means a should be "close" to 10, i.e. within an order of magnitude
# for example 10 ** b is always (b + 1) digits long
# and it goes up from there
# so a < 10
# but then, 2 ** b
import math


def size(a, b):
    return math.ceil(b * math.log(a, 10))


if _name_ == "_main_":
    total = set()
    for a in range(1, 10):
        for b in range(1, 10_000):
            if size(a, b) == b:
                print(f"a, b = {a}, {b}")
                total.add(a ** b)
    print(f"total = {len(total)}")
