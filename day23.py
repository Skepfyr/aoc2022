from collections import defaultdict
from dataclasses import dataclass
from itertools import count
import sys


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)


elves = set()
for y, row in enumerate(sys.stdin):
    for x, cell in enumerate(row.strip()):
        if cell == "#":
            elves.add(Pos(x, y))

dirs = [
    (Pos(0, -1), [Pos(-1, -1), Pos(0, -1), Pos(1, -1)]),
    (Pos(0, 1), [Pos(-1, 1), Pos(0, 1), Pos(1, 1)]),
    (Pos(-1, 0), [Pos(-1, -1), Pos(-1, 0), Pos(-1, 1)]),
    (Pos(1, 0), [Pos(1, -1), Pos(1, 0), Pos(1, 1)]),
]

for round in count():
    proposals = defaultdict(list)
    for elf in elves:
        if all(
            (i, j) == (0, 0) or elf + Pos(i, j) not in elves
            for i in [-1, 0, 1]
            for j in [-1, 0, 1]
        ):
            continue

        for attempt in range(len(dirs)):
            (dir, tests) = dirs[(attempt + round) % len(dirs)]
            if not any((elf + test) in elves for test in tests):
                proposals[elf + dir].append(elf)
                break

    if len(proposals) == 0:
        print(f"Part 2: {round + 1}")
        break

    for dest, src in proposals.items():
        if len(src) == 1:
            elves.remove(src[0])
            elves.add(dest)

    if round == 9:
        minimum = None
        maximum = None
        for elf in elves:
            if minimum is None:
                minimum = elf
                maximum = elf
            else:
                minimum = Pos(min(elf.x, minimum.x), min(elf.y, minimum.y))
                maximum = Pos(max(elf.x, maximum.x), max(elf.y, maximum.y))

        height = maximum.y - minimum.y + 1
        width = maximum.x - minimum.x + 1
        print(f"Part 1: {height * width - len(elves)}")
