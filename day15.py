import re
import sys
from typing import Optional, Tuple


class Sensor:
    def __init__(self, location, beacon) -> None:
        self.location = location
        self.beacon = beacon
        self.radius = abs(location[0] - beacon[0]) + abs(location[1] - beacon[1])

    def __contains__(self, point) -> bool:
        dist = abs(self.location[0] - point[0]) + abs(self.location[1] - point[1])
        return dist <= self.radius


sensors: list[Sensor] = []
regex = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)
for line in sys.stdin:
    match = re.search(regex, line)
    sensors.append(
        Sensor(
            (int(match.group(1)), int(match.group(2))),
            (int(match.group(3)), int(match.group(4))),
        )
    )

part1_row = 2000000
empty_positions = set()
for sensor in sensors:
    radius_at_y = sensor.radius - abs(sensor.location[1] - part1_row)
    if radius_at_y <= 0:
        continue
    for x in range(
        sensor.location[0] - radius_at_y, sensor.location[0] + radius_at_y + 1
    ):
        if not (x == sensor.beacon[0] and part1_row == sensor.beacon[1]):
            empty_positions.add(x)

print(f"Part 1: {len(empty_positions)}")


def find_free_square(
    min: Tuple[int, int], max: Tuple[int, int]
) -> Optional[Tuple[int, int]]:
    if min[0] > max[0] or min[1] > max[1]:
        return None
    for sensor in sensors:
        if (
            min in sensor
            and max in sensor
            and (min[0], max[1]) in sensor
            and (max[0], min[1]) in sensor
        ):
            return None
    if min == max:
        return min
    midpoint_x = (max[0] - min[0]) // 2 + min[0]
    midpoint_y = (max[1] - min[1]) // 2 + min[1]
    return (
        find_free_square(min, (midpoint_x, midpoint_y))
        or find_free_square((midpoint_x + 1, min[1]), (max[0], midpoint_y))
        or find_free_square((min[0], midpoint_y + 1), (midpoint_x, max[1]))
        or find_free_square((midpoint_x + 1, midpoint_y + 1), max)
    )


max = 4000000
(x, y) = find_free_square((0, 0), (max, max))
print(f"Part 2: {x * 4000000 + y}")
