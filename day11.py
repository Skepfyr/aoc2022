from copy import deepcopy
import sys
from collections import deque


class Monkey:
    items: deque[int]

    def __init__(self, items, op, test, true, false) -> None:
        self.items = items
        self.op = op
        self.divisor = test
        self.true = true
        self.false = false

    def next_item(self) -> int:
        old = self.items.popleft()  # noqa: F841
        local = {"old": old}
        exec(self.op, {}, local)  # Uses old and defines new
        return local["new"]

    def test(self, item) -> int:
        if item % self.divisor == 0:
            return self.true
        else:
            return self.false


monkeys: list[Monkey] = []
worry_modulus = 1

for line in sys.stdin:
    items = sys.stdin.readline().strip().removeprefix("Starting items: ")
    items = deque(map(int, items.split(", ")))
    operation = sys.stdin.readline().strip().removeprefix("Operation: ")
    test = int(sys.stdin.readline().strip().removeprefix("Test: divisible by "))
    true = int(sys.stdin.readline().strip().removeprefix("If true: throw to monkey "))
    false = int(sys.stdin.readline().strip().removeprefix("If false: throw to monkey "))
    sys.stdin.readline()
    monkeys.append(Monkey(items, operation, test, true, false))
    worry_modulus *= test

old_monkeys = deepcopy(monkeys)
inspections = [0] * len(monkeys)
for _round in range(20):
    for i, monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            inspections[i] += 1
            item = monkey.next_item() // 3
            monkeys[monkey.test(item)].items.append(item)

inspections.sort(reverse=True)
print(f"Part 1: {inspections[0] * inspections[1]}")

monkeys = old_monkeys
inspections = [0] * len(monkeys)
for _round in range(10000):
    for i, monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            inspections[i] += 1
            item = monkey.next_item() % worry_modulus
            monkeys[monkey.test(item)].items.append(item)

inspections.sort(reverse=True)
print(f"Part 1: {inspections[0] * inspections[1]}")
