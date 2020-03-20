#! /usr/bin/env python3

import itertools
from typing import Dict, List, Optional, Tuple

SixCycle = Tuple[
    Optional[int],
    Optional[int],
    Optional[int],
    Optional[int],
    Optional[int],
    Optional[int],
]


def polygonal(sides, index) -> int:
    return {
        3: lambda n: n * (n - 1) // 2,
        4: lambda n: n ** 2,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2),
    }[sides](index)


def four_digit_polygons(sides) -> List[int]:
    return [
        poly
        for poly in itertools.takewhile(
            lambda x: x < 10000, (polygonal(sides, x) for x in itertools.count())
        )
        if poly > 1000
    ]


def fill_in_slot(
    slot: int, story_so_far: SixCycle, unused_polys: Dict[int, List[int]]
) -> Optional[SixCycle]:
    prev_suffix = str(story_so_far[slot - 1])[2:]

    if slot == 6:  # all filled in
        if str(story_so_far[-1])[2:] == str(story_so_far[0])[:2]:
            return story_so_far
        else:  # isn't fully cyclical
            return None

    for chosen_sides, polys in unused_polys.items():
        for poly in polys:
            if not str(poly).startswith(prev_suffix):
                continue
            if maybe_done := fill_in_slot(
                slot + 1,
                story_so_far[:slot] + (poly,) + story_so_far[slot + 1 :],
                {s: p for s, p in unused_polys.items() if s != chosen_sides},
            ):
                return maybe_done
    return None


if __name__ == "__main__":
    story_so_far: SixCycle = (None,) * 6
    polygons = {sides: four_digit_polygons(sides) for sides in range(3, 8)}
    for seed_octagons in four_digit_polygons(8):
        story_so_far = (seed_octagons,) + story_so_far[1:]
        solution = fill_in_slot(1, story_so_far, polygons)
        if solution:
            print(f"{solution}, sum={sum(solution)}")
