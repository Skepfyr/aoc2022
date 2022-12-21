from copy import copy
import operator
import sys

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.floordiv,
}

monkeys = dict()
for line in sys.stdin:
    [name, operation] = line.split(":")
    try:
        monkeys[name] = int(operation.strip())
    except ValueError:
        [a, op, b] = operation.strip().split(" ")
        monkeys[name] = (op, a, b)
backup = copy(monkeys)


def solve(name) -> int:
    if isinstance(monkeys[name], int):
        return monkeys[name]
    (op, a, b) = monkeys[name]
    value = operators[op](solve(a), solve(b))
    monkeys[name] = value
    return value


print(f"Part 1: {solve('root')}")
monkeys = backup


def contains_human(name):
    if name == "humn":
        return True
    elif isinstance(monkeys[name], int):
        return False
    else:
        (_, a, b) = monkeys[name]
        a_contains_human = contains_human(a)
        b_contains_human = contains_human(b)
        if not a_contains_human:
            solve(a)
        if not b_contains_human:
            solve(b)
        return a_contains_human or b_contains_human


(_, lhs, rhs) = monkeys["root"]
if contains_human(lhs):
    num = solve(rhs)
    expr = lhs
elif contains_human(rhs):
    num = solve(lhs)
    expr = rhs
else:
    raise "No human!?"

inverse = {
    "+": (operator.sub, operator.sub),
    "-": (lambda num, lhs: lhs - num, operator.add),
    "*": (operator.floordiv, operator.floordiv),
    "/": (lambda num, lhs: lhs // num, operator.mul),
}
while expr != "humn":
    (op, lhs, rhs) = monkeys[expr]
    if lhs != "humn" and isinstance(monkeys[lhs], int):
        num = inverse[op][0](num, monkeys[lhs])
        expr = rhs
    elif rhs != "humn" and isinstance(monkeys[rhs], int):
        num = inverse[op][1](num, monkeys[rhs])
        expr = lhs
    else:
        raise "Human on both sides!?"

print(f"Part 2: {num}")
