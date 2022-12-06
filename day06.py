import sys


def start_of_n(input: str, n: int) -> int:
    prev_chars = []
    for i, char in enumerate(input, start=1):
        prev_chars.append(char)
        if len(prev_chars) == n:
            if len(set(prev_chars)) == n:
                return i
            prev_chars.pop(0)


input = sys.stdin.readline()
print(f"Part 1: {start_of_n(input, 4)}")
print(f"Part 1: {start_of_n(input, 14)}")
