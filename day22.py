import re

# import sys

input = open("input/day22")

board: list[list[str]] = []
while line := input.readline().removesuffix("\n"):
    board.append(list(line))
instructions = [
    int(x) if x.isdigit() else x
    for x in re.findall(r"\d+|R|L", input.readline().strip())
]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

facing = 0
x = board[0].index(".")
y = 0

for instruction in instructions:
    if instruction == "L":
        facing = (facing - 1) % 4
    elif instruction == "R":
        facing = (facing + 1) % 4
    else:
        for _ in range(instruction):
            target_x = x + directions[facing][0]
            target_y = y + directions[facing][1]
            if target_x in range(len(board[y])) and board[y][target_x] != " ":
                wrapped_x = target_x
            elif directions[facing][0] > 0:
                wrapped_x = 0
                while board[target_y][wrapped_x] == " ":
                    wrapped_x += 1
            elif directions[facing][0] < 0:
                wrapped_x = len(board[y]) - 1
                while board[target_y][wrapped_x] == " ":
                    wrapped_x -= 1

            if (
                target_y in range(len(board))
                and x in range(len(board[target_y]))
                and board[target_y][x] != " "
            ):
                wrapped_y = target_y
            elif directions[facing][1] > 0:
                wrapped_y = 0
                while board[wrapped_y][wrapped_x] == " ":
                    wrapped_y += 1
            elif directions[facing][1] < 0:
                wrapped_y = len(board) - 1
                while (
                    wrapped_x not in range(len(board[wrapped_y]))
                    or board[wrapped_y][wrapped_x] == " "
                ):
                    wrapped_y -= 1

            if board[wrapped_y][wrapped_x] == "#":
                break
            else:
                x = wrapped_x
                y = wrapped_y

print(f"Part 1: {(y + 1) * 1000 + (x + 1) * 4 + facing}")


facing = 0
face = 0
x = 0
y = 0

faces = [
    (50, 0, [(1, 0), (2, 1), (4, 0), (5, 0)]),
    (100, 0, [(3, 2), (2, 2), (0, 2), (5, 3)]),
    (50, 50, [(1, 3), (3, 1), (4, 1), (0, 3)]),
    (50, 100, [(1, 2), (5, 2), (4, 2), (2, 3)]),
    (0, 100, [(3, 0), (5, 1), (0, 0), (2, 0)]),
    (0, 150, [(3, 3), (1, 1), (0, 1), (4, 3)]),
]

for instruction in instructions:
    if instruction == "L":
        facing = (facing - 1) % 4
    elif instruction == "R":
        facing = (facing + 1) % 4
    else:
        for _ in range(instruction):
            _, _, adjacencies = faces[face]
            target_x = x + directions[facing][0]
            target_y = y + directions[facing][1]
            if target_x not in range(50) or target_y not in range(50):
                next_face, next_facing = adjacencies[facing]
                if target_x < 0:
                    pos = 49 - target_y
                elif target_x >= 50:
                    pos = target_y
                elif target_y < 0:
                    pos = target_x
                elif target_y >= 50:
                    pos = 49 - target_x
                else:
                    raise "huh"
                if next_facing == 0:
                    target_x = 0
                    target_y = pos
                elif next_facing == 1:
                    target_x = 49 - pos
                    target_y = 0
                elif next_facing == 2:
                    target_x = 49
                    target_y = 49 - pos
                elif next_facing == 3:
                    target_x = pos
                    target_y = 49
            else:
                next_face = face
                next_facing = facing
            x_off, y_off, _ = faces[next_face]
            if board[target_y + y_off][target_x + x_off] == "#":
                break
            face = next_face
            facing = next_facing
            x = target_x
            y = target_y

x_off, y_off, _ = faces[face]
print(f"Part 2: {(y + y_off + 1) * 1000 + (x + x_off + 1) * 4 + facing}")
