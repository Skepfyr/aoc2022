from operator import add, sub
import sys

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}


def sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1


rope = [(0, 0)] * 10

part1_visited = set()
part1_visited.add((0, 0))
part2_visited = set()
part2_visited.add((0, 0))
for line in sys.stdin:
    [dir, num] = line.strip().split(" ")
    dir = directions[dir]
    for _ in range(int(num)):
        rope[0] = tuple(map(add, rope[0], dir))
        for knot in range(1, len(rope)):
            diff = tuple(map(sub, rope[knot - 1], rope[knot]))
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                rope[knot] = tuple(map(add, rope[knot], map(sign, diff)))
        part1_visited.add(rope[1])
        part2_visited.add(rope[9])

print(f"Part 1: {len(part1_visited)}")
print(f"Part 2: {len(part2_visited)}")
