import sys

part1 = 0
part2 = 0
for line in sys.stdin:
    pair: list[set[int]] = []
    for range_str in line.split(","):
        [start, end] = map(int, range_str.split("-"))
        pair.append(set(range(start, end + 1)))

    if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
        part1 += 1
    if pair[0] & pair[1]:
        part2 += 1

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
