import sys
from typing import Optional


class Directory:
    parent: Optional["Directory"]
    directories: dict[str, "Directory"]
    files: dict[str, int]

    def __init__(self, parent: Optional["Directory"]) -> None:
        self.parent = parent
        self.directories = dict()
        self.files = dict()

    def for_each(self, acc, f):
        acc = f(acc, self)
        for dir in self.directories.values():
            acc = dir.for_each(acc, f)
        return acc

    def size(self) -> int:
        return sum(self.files.values())

    def total_size(self) -> int:
        return self.for_each(0, lambda acc, dir: acc + dir.size())


root = Directory(None)

current = root
for line in sys.stdin:
    line = line.strip()
    if line == "$ cd /":
        current = root
    elif line == "$ cd ..":
        current = current.parent
    elif line.startswith("$ cd "):
        next = line.removeprefix("$ cd ")
        current = current.directories[next]
    elif line == "$ ls":
        pass
    elif line.startswith("dir "):
        name = line.removeprefix("dir ")
        current.directories[name] = Directory(current)
    else:
        [size, name] = line.split(" ")
        current.files[name] = int(size)

part1 = root.for_each(
    0,
    lambda acc, dir: (acc + (dir.total_size() if dir.total_size() <= 100000 else 0)),
)
print(f"Part 1: {part1}")


required_size = 30000000 - (70000000 - root.total_size())
part2 = root.for_each(
    70000000,
    lambda acc, dir: min(acc, dir.total_size())
    if dir.total_size() >= required_size
    else acc,
)
print(f"Part 2: {part2}")
