import sys

cave = set()
max_depth = 0

for path in sys.stdin:
    path = path.strip().split(" -> ")
    prev = list(map(int, path[0].split(",")))
    for step in path[1:]:
        next = list(map(int, step.split(",")))
        if prev[0] == next[0]:
            for y in range(min(prev[1], next[1]), max(prev[1], next[1]) + 1):
                cave.add((prev[0], y))
        else:
            for x in range(min(prev[0], next[0]), max(prev[0], next[0]) + 1):
                cave.add((x, prev[1]))
        max_depth = max(max_depth, next[1])
        prev = next

hit_floor = False
total_sand = 0
while (500, 0) not in cave:
    x = 500
    y = 0
    while True:
        if y <= max_depth and (x, y + 1) not in cave:
            y += 1
        elif y <= max_depth and (x - 1, y + 1) not in cave:
            x -= 1
            y += 1
        elif y <= max_depth and (x + 1, y + 1) not in cave:
            x += 1
            y += 1
        else:
            cave.add((x, y))
            total_sand += 1
            break
    if y > max_depth and not hit_floor:
        hit_floor = True
        print(f"Part 1: {total_sand - 1}")

print(f"Part 2: {total_sand}")
