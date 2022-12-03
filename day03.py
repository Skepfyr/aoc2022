import functools
import operator
import sys

rucksacks = [line.strip() for line in sys.stdin]

total = 0
for rucksack in rucksacks:
    a, b = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    a_items, b_items = set(a), set(b)
    duplicate = (a_items & b_items).pop()
    priority = ord(duplicate) - (ord("A") - 26 if duplicate.isupper() else ord("a")) + 1
    total += priority

print(f"Part 1: {total}")

total = 0
for i in range(0, len(rucksacks), 3):
    group = (set(rucksack) for rucksack in rucksacks[i : i + 3])
    common_item = functools.reduce(operator.and_, group).pop()
    priority = (
        ord(common_item) - (ord("A") - 26 if common_item.isupper() else ord("a")) + 1
    )
    total += priority

print(f"Part 2: {total}")
