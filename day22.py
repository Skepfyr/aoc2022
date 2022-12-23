import re
import sys

board: list[list[str]] = []
while line := sys.stdin.readline().removesuffix("\n"):
    board.append(list(line))
instructions = [
    int(x) if x.isdigit() else x
    for x in re.findall(r"\d+|R|L", sys.stdin.readline().strip())
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
x = board[0].index(".")
y = 0
