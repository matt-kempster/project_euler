#!/usr/bin/env python3

from itertools import product, zip_longest
from pathlib import Path
from string import ascii_lowercase
from typing import List, Optional, Tuple

full_text: str = Path("./assets/p059_cipher.txt").read_text()
full_bytes: List[str] = list(map(int, full_text.split(",")))


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def decrypt(encoded: List[int], key: Tuple[int, int, int]) -> Optional[int]:
    message: List[int] = []
    for group in chunks(encoded, 3):
        message.extend([group[i] ^ key[i] for i in range(3)])
    final_message_str: str = "".join(map(chr, message))
    if " the " in final_message_str:
        print(final_message_str)
        return sum(message)
    else:
        return None


for potential_key in product(ascii_lowercase, repeat=3):
    if total := decrypt(full_bytes, tuple(ord(potential_key[i]) for i in range(3))):
        print(f"{potential_key=} has {total=}")
