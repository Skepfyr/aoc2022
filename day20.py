import sys

input = [(i, int(line.strip())) for i, line in enumerate(sys.stdin)]


def mix(key: int, items: list[(int, int)]):
    for elem in input:
        index = items.index(elem)
        elem = items.pop(index)
        items.insert((index + elem[1] * key - 1) % len(items) + 1, elem)


def answer(key: int, items: list[(int, int)]) -> int:
    zero_pos = [item for _, item in items].index(0)
    _, x = items[(zero_pos + 1000) % len(items)]
    _, y = items[(zero_pos + 2000) % len(items)]
    _, z = items[(zero_pos + 3000) % len(items)]
    return (x + y + z) * key


part1 = input.copy()
mix(1, part1)
print(f"Part 1: {answer(1, part1)}")

part2 = input.copy()
for _ in range(10):
    mix(811589153, part2)
print(f"Part 2: {answer(811589153, part2)}")
