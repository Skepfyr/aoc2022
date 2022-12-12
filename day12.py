import sys

map = []

for y, line in enumerate(sys.stdin):
    row = []
    for x, cell in enumerate(line.strip()):
        if cell == "S":
            start = (x, y)
            cell = "a"
        elif cell == "E":
            end = (x, y)
            cell = "z"
        row.append(ord(cell) - ord("a"))
    map.append(row)

height = len(map)
width = len(map[0])
max_dist = height * width + 1

distances = [[max_dist for _ in range(width)] for _ in range(height)]
distances[end[1]][end[0]] = 0
visited = set()

while len(visited) < height * width:
    min_dist = max_dist + 1
    min_node = None
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if (x, y) not in visited and distances[y][x] < min_dist:
                min_dist = distances[y][x]
                min_node = (x, y)
    visited.add(min_node)
    node_height = map[min_node[1]][min_node[0]]
    for x, y in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        x += min_node[0]
        y += min_node[1]
        if x in range(width) and y in range(height) and map[y][x] >= node_height - 1:
            distances[y][x] = min(distances[y][x], min_dist + 1)

print(f"Part 1: {distances[start[1]][start[0]]}")

min_dist = distances[start[1]][start[0]]
for y in range(height):
    for x in range(width):
        if distances[y][x] < min_dist and map[y][x] == 0:
            min_dist = distances[y][x]

print(f"Part 2: {min_dist}")
