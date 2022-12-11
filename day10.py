import sys


def execute(instructions):
    register = 1
    for instruction in instructions:
        instruction = instruction.strip()
        if instruction == "noop":
            yield register
        else:
            yield register
            yield register
            [_, v] = instruction.split(" ")
            register += int(v)


signal_strength = 0
image = ""
for cycle, register in enumerate(execute(sys.stdin), start=1):
    if (cycle - 20) % 40 == 0:
        signal_strength += cycle * register
    col = (cycle - 1) % 40
    if col in range(register - 1, register + 2):
        image += "█"
    else:
        image += " "
    if col == 39:
        image += "\n"

print(f"Part 1: {signal_strength}")
print(f"Part 2:\n{image}")
