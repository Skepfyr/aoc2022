from heapq import heappop, heappush
import sys

left = []
right = []
first = sys.stdin.readline()
width = len(first.strip()) - 2
up = [[] for _ in range(width)]
down = [[] for _ in range(width)]

for y, line in enumerate(sys.stdin):
    height = y
    if line[1] == "#":
        continue
    left.append([])
    right.append([])
    for x, cell in enumerate(line[1:-1]):
        if cell == "<":
            left[y].append(x)
        elif cell == ">":
            right[y].append(x)
        elif cell == "v":
            down[x].append(y)
        elif cell == "^":
            up[x].append(y)


def has_blizzard(x, y, time) -> bool:
    return (
        any((blizzard - time) % height == y for blizzard in up[x])
        or any((blizzard + time) % height == y for blizzard in down[x])
        or any((blizzard - time) % width == x for blizzard in left[y])
        or any((blizzard + time) % width == x for blizzard in right[y])
    )


moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
places = []
places.append((3 * (width + height), (0, -1, 1, 2)))
visited = set()

start = (0, -1)
end = (width - 1, height)
goal = [end, start, end]
part1 = False

max_time = 0

while entry := heappop(places):
    _, (x, y, time, phase) = entry
    if phase == 2 and (x, y) == end:
        if not part1:
            print(f"Part 1: {time}")
            part1 = True
        heappush(places, (phase * (width + height) + time, (x, y, time, 1)))
    elif phase == 1 and (x, y) == start:
        heappush(places, (phase * (width + height) + time, (x, y, time, 0)))
    elif phase == 0 and (x, y) == end:
        print(f"Part 2: {time}")
        break
    if (
        (x, y) != start
        and (x, y) != end
        and (
            x not in range(width) or y not in range(height) or has_blizzard(x, y, time)
        )
    ):
        continue
    for x_off, y_off in moves:
        new_x = x + x_off
        new_y = y + y_off
        if (new_x, new_y, time + 1, phase) not in visited:
            visited.add((new_x, new_y, time + 1, phase))
            heappush(
                places,
                (
                    phase * (width + height)
                    + (goal[phase][0] - new_x)
                    + (goal[phase][1] - new_y)
                    + time,
                    (new_x, new_y, time + 1, phase),
                ),
            )
