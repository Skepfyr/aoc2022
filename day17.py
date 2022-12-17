from itertools import count
import math
import sys

rocks = [
    [
        [True, True, True, True],
    ],
    [
        [False, True, False],
        [True, True, True],
        [False, True, False],
    ],
    [
        [True, True, True],
        [False, False, True],
        [False, False, True],
    ],
    [
        [True],
        [True],
        [True],
        [True],
    ],
    [
        [True, True],
        [True, True],
    ],
]

input = sys.stdin.read().strip()
tower = []

max_required_moves = math.lcm(len(input), len(rocks))


def is_colliding(rock, x, y):
    if x < 0:
        return True
    if y < 0:
        return True
    if x + len(rock[0]) > 7:
        return True
    for y_offset, row in enumerate(rock):
        if y + y_offset >= len(tower):
            break
        for x_offset, stone in enumerate(row):
            if tower[y + y_offset][x + x_offset] and stone:
                return True
    return False


rocks_total = 1000000000000
seen = dict()
seen_repeat = False

move = 0
for rocks_current in count():
    if rocks_current == 2022:
        part1 = len(tower)
    if not seen_repeat and rocks_current % len(rocks) == 0:
        action = move % len(input)
        if (
            action in seen
            and len(seen[action]) > 1
            and len(tower) - seen[action][-1][1]
            == seen[action][-1][1] - seen[action][-2][1]
        ):
            seen_repeat = True
            rocks_initial, height_initial = seen[action][-1]
            height_at_repeat = len(tower)
            rocks_at_repeat = rocks_current
            rocks_remaining = rocks_total - rocks_initial
            repeats = rocks_remaining // (rocks_current - rocks_initial)
            rocks_remainder = rocks_remaining % (rocks_current - rocks_initial)
        else:
            if action not in seen:
                seen[action] = []
            seen[action].append((rocks_current, len(tower)))
    if seen_repeat and rocks_current == rocks_at_repeat + rocks_remainder:
        height_at_end = len(tower)
        break
    rock = rocks[rocks_current % len(rocks)]
    x = 2
    y = len(tower) + 3
    while True:
        char = input[move % len(input)]
        move += 1
        if char == "<":
            jet = -1
        else:
            jet = 1
        if not is_colliding(rock, x + jet, y):
            x += jet
        if is_colliding(rock, x, y - 1):
            break
        else:
            y -= 1
    for _ in range(y + len(rock) - len(tower)):
        tower.append([False] * 7)
    for y_offset, row in enumerate(rock):
        for x_offset, stone in enumerate(row):
            tower[y + y_offset][x + x_offset] |= stone

print(f"Part 1: {part1}")
part2 = (
    height_initial
    + repeats * (height_at_repeat - height_initial)
    + (height_at_end - height_at_repeat)
)
print(f"Part 2: {part2}")
