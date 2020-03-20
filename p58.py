#!/usr/bin/env python3

# idea: count relevant primes per ring of numbers
# each corner is like, n-1 more than the previous bottom right corner
# and then each corner from there is just n more
# and the previous bottom right corner is an odd square

import itertools
from pyprimes import isprime

prime_count = 0
prime_percent = 0
for side_length in itertools.count(start=3, step=2):  # only odd
    prev_odd_square = (side_length - 2) ** 2
    corners = [prev_odd_square + (side_length - 1) * corner for corner in range(1, 4)]
    prime_count += sum(map(isprime, corners))
    prime_percent = prime_count / (2 * side_length - 1)
    print(f"{side_length=}: {prime_count=}, {prime_percent=}")
    if prime_percent < 0.1:
        break
