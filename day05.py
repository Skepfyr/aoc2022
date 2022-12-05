from copy import deepcopy
import re
import sys

stacks = [
    ["W", "M", "L", "F"],
    ["B", "Z", "V", "M", "F"],
    ["H", "V", "R", "S", "L", "Q"],
    ["F", "S", "V", "Q", "P", "M", "T", "J"],
    ["L", "S", "W"],
    ["F", "V", "P", "M", "R", "J", "W"],
    ["J", "Q", "C", "P", "N", "R", "F"],
    ["V", "H", "P", "S", "Z", "W", "R", "B"],
    ["B", "M", "J", "C", "G", "H", "Z", "W"],
]
pattern = r"move (\d+) from (\d+) to (\d+)"

part1 = deepcopy(stacks)
part2 = deepcopy(stacks)

for instruction in sys.stdin:
    match = re.search(pattern, instruction)
    quantity = int(match.group(1))
    source = int(match.group(2)) - 1
    destination = int(match.group(3)) - 1
    for _ in range(quantity):
        part1[destination].append(part1[source].pop())

    part2[destination].extend(part2[source][-quantity:])
    part2[source] = part2[source][:-quantity]

print("Parts 1: ", *(stack[-1] for stack in part1), sep="")
print("Parts 2: ", *(stack[-1] for stack in part2), sep="")
