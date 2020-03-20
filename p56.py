#!/usr/bin/env python3
from functools import reduce

pairs = [(a, b) for a in range(100) for b in range(100)]
pairs = sorted(pairs, key=lambda xy: xy[0] + xy[1], reverse=True)

best_digital_sum = 0

for a, b in pairs:
    reduced = int(reduce(lambda d1, d2: str(int(d1) + int(d2)), str(a ** b)))
    if reduced > best_digital_sum:
        best_digital_sum = reduced
        print(f"{a=}, {b=}, {best_digital_sum=}")
