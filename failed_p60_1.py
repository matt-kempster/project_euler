import functools
import itertools
from dataclasses import dataclass
from itertools import chain, zip_longest
from random import randint
from typing import FrozenSet, Set, Tuple

from pyprimes import isprime, nth_prime

FiveTuple = Tuple[int, int, int, int, int]


@dataclass(frozen=True)
class EnumeratedPrime:
    index: int
    prime: int

    def __repr__(self):
        return f"P<{self.prime}>"


FivePrimes = Tuple[
    EnumeratedPrime, EnumeratedPrime, EnumeratedPrime, EnumeratedPrime, EnumeratedPrime
]


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


def dtldarek(fiver: FiveTuple) -> int:
    strings = list(map(reversed, map(str, fiver)))
    return int(
        ("".join(list(chain.from_iterable(zip_longest(*strings, fillvalue="0")))))[::-1]
    )


def dtldarek_inverse(num: int) -> FiveTuple:
    groups = [int(str(num)[-i::-5][::-1] or "0") for i in range(1, 6)]
    return groups


def convert_to_primes(group: FiveTuple) -> FivePrimes:
    return tuple(EnumeratedPrime(index, nth_prime(index)) for index in group)


BADPAIRS: Set[FrozenSet[int]] = set()


@memoize
def prime_group_good(prime_set: FrozenSet[EnumeratedPrime]) -> bool:
    global BADPAIRS
    ret = True
    for prime1, prime2 in itertools.combinations(prime_set, 2):
        if not (
            isprime(int(str(prime1.prime) + str(prime2.prime)))
            and isprime(int(str(prime2.prime) + str(prime1.prime)))
        ):
            BADPAIRS.add(frozenset((prime1.index, prime2.index)))
            ret = False
    print(BADPAIRS)
    return ret


def has_bad_pair(groups: FiveTuple) -> bool:
    global BADPAIRS
    for index1, index2 in itertools.combinations(groups, 2):
        if frozenset((index1, index2)) in BADPAIRS:
            return True
    return False

if __name__ == "__main__":
    for num in itertools.count():
        groups: FiveTuple = dtldarek_inverse(num)
        if (
            len(set(groups)) != 5
            or 0 in groups
            or 1 in groups
            or 3 in groups
            or has_bad_pair(groups)
        ):
            continue

        prime_group: FivePrimes = convert_to_primes(groups)
        print(prime_group)
        if prime_group_good(frozenset(prime_group)):
            print(prime_group, sum(prime_group))
