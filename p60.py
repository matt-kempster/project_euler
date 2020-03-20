import functools
import itertools
import random
from math import sqrt
from typing import FrozenSet, List

from pyprimes import isprime, primes_below


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


@memoize
def is_good_pair(prime1, prime2) -> bool:
    str1 = str(prime1)
    str2 = str(prime2)
    return isprime(int(str1 + str2)) and isprime(int(str2 + str1))


def get_good_pairs(prime_pool: List[int]) -> List[FrozenSet[int]]:
    good: List[FrozenSet[int]] = []
    for prime1, prime2 in itertools.combinations(prime_pool, 2):
        if is_good_pair(prime1, prime2):
            good.append(frozenset((prime1, prime2)))
    return good


def gen_good_pairs_of_pairs(good_pairs: List[FrozenSet[int]]):
    seen_pairs_of_pairs = set()
    # idea: "fraction zigzag" these good pairs
    # (update - I tried that, it was too careful or something :/)
    # instead, just roughly approximate it by sorting them by sum.
    # interestingly, this seems to sometimes slow down execution?
    good_pairs.sort(key=lambda pair: sum(pair))
    for pair1, pair2 in itertools.combinations(good_pairs, 2):
        # repeats would be multiples of e.g. 11 or 101, so check:
        if pair1 & pair2:  # intersection ("&") of sets imply repeats
            continue
        prime_1a, prime_1b = pair1
        prime_2a, prime_2b = pair2
        four_primes = frozenset((prime_1a, prime_1b, prime_2a, prime_2b))
        if four_primes in seen_pairs_of_pairs:
            continue  # avoid repeats
        if (
            is_good_pair(prime_1a, prime_2a)
            and is_good_pair(prime_1a, prime_2b)
            and is_good_pair(prime_1b, prime_2a)
            and is_good_pair(prime_1b, prime_2b)
        ):  # "cross check" - don't recompute is_good_pair(pair1) and ...(pair2)
            print(four_primes)
            seen_pairs_of_pairs.add(four_primes)
            yield four_primes


if __name__ == "__main__":
    prime_pool = list(primes_below(10000))  # arbitrary limit
    prime_pool.remove(2)  # ends with 2 --> not prime
    prime_pool.remove(5)  # ends with 5 --> not prime
    good_pairs = get_good_pairs(prime_pool)  # constant time: about ~10 secs
    print("done getting pairs")

    for good_pop in gen_good_pairs_of_pairs(good_pairs):
        for prime in prime_pool:  # the fifth prime
            if all(is_good_pair(prime, pop_prime) for pop_prime in good_pop):
                five_primes = list(good_pop) + [prime]
                print(f"winner: {five_primes}, sum={sum(five_primes)}")
                break  # prime_pool is ascending, so done with this foursome
