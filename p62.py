import itertools
from collections import defaultdict

from dataclasses import dataclass


@dataclass
class CubeCount:
    count: int
    smallest_cube: int


if __name__ == "__main__":
    current_digit_length = 1
    cube_digits = {}
    for num in itertools.count():
        cubed = num ** 3
        sorted_str = "".join(sorted(str(cubed)))
        if len(str(cubed)) > current_digit_length:
            current_digit_length = len(sorted_str)
            print(f"{current_digit_length=}")
            cube_digits = {sorted_str: CubeCount(1, cubed)}
        elif sorted_str in cube_digits:
            if cube_digits[sorted_str].count == 4:
                print(f"winner, probably: {cube_digits[sorted_str].smallest_cube}")
                break
            else:
                cube_digits[sorted_str].count += 1
        else:
            cube_digits[sorted_str] = CubeCount(1, cubed)
