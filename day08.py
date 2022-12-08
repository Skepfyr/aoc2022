import sys

map = [list(map(int, line.strip())) for line in sys.stdin]
size = len(map)
visible = [[False] * size for _ in range(size)]

for row in range(size):
    height = -1
    for col in range(size):
        if map[row][col] > height:
            height = map[row][col]
            visible[row][col] = True
    height = -1
    for col in reversed(range(size)):
        if map[row][col] > height:
            height = map[row][col]
            visible[row][col] = True

for col in range(size):
    height = -1
    for row in range(size):
        if map[row][col] > height:
            height = map[row][col]
            visible[row][col] = True
    height = -1
    for row in reversed(range(size)):
        if map[row][col] > height:
            height = map[row][col]
            visible[row][col] = True

print(f"Part 1: {sum(sum(row) for row in visible)}")

max_score = 0
for row in range(size):
    for col in range(size):
        height = map[row][col]
        left = 0
        for x in reversed(range(col)):
            left += 1
            if map[row][x] >= height:
                break
        right = 0
        for x in range(col + 1, size):
            right += 1
            if map[row][x] >= height:
                break
        up = 0
        for x in reversed(range(row)):
            up += 1
            if map[x][col] >= height:
                break
        down = 0
        for x in range(row + 1, size):
            down += 1
            if map[x][col] >= height:
                break

        score = left * right * up * down
        max_score = max(score, max_score)

print(f"Part 2: {max_score}")
