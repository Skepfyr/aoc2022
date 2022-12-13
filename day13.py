import functools
import sys


def compare(left, right) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return left - right
    else:
        if not isinstance(left, list):
            left = [left]
        if not isinstance(right, list):
            right = [right]
        for (l, r) in zip(left, right):
            cmp = compare(l, r)
            if cmp != 0:
                return cmp
        return len(left) - len(right)


part1 = 0
packet_list = []
for idx, left in enumerate(sys.stdin, start=1):
    left = eval(left.strip())
    packet_list.append(left)
    right = eval(sys.stdin.readline().strip())
    packet_list.append(right)
    sys.stdin.readline()
    if compare(left, right) < 0:
        part1 += idx

print(f"Part 1: {part1}")

packet_list.append([[2]])
packet_list.append([[6]])

packet_list.sort(key=functools.cmp_to_key(compare))
two = packet_list.index([[2]]) + 1
six = packet_list.index([[6]]) + 1
print(f"Part 2: {two * six}")
