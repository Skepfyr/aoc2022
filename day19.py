from copy import copy
from dataclasses import dataclass
import re
import sys


@dataclass
class Materials:
    ore: int
    clay: int
    obsidian: int
    geodes: int

    def __add__(self, other: "Materials") -> "Materials":
        return Materials(
            self.ore + other.ore,
            self.clay + other.clay,
            self.obsidian + other.obsidian,
            self.geodes + other.geodes,
        )

    def __sub__(self, other: "Materials") -> "Materials":
        return Materials(
            self.ore - other.ore,
            self.clay - other.clay,
            self.obsidian - other.obsidian,
            self.geodes - other.geodes,
        )

    def contains(self, other: "Materials") -> bool:
        return (
            self.ore >= other.ore
            and self.clay >= other.clay
            and self.obsidian >= other.obsidian
            and self.geodes >= other.geodes
        )


@dataclass
class Blueprint:
    ore_robot: Materials
    clay_robot: Materials
    obsidian_robot: Materials
    geode_robot: Materials


blueprints: list[Blueprint] = []
blueprint_regex = re.compile(
    r"Blueprint \d+: "
    + r"Each ore robot costs (\d+) ore. "
    + r"Each clay robot costs (\d+) ore. "
    + r"Each obsidian robot costs (\d+) ore and (\d+) clay. "
    + r"Each geode robot costs (\d+) ore and (\d+) obsidian."
)
for input in sys.stdin:
    match = re.fullmatch(blueprint_regex, input.strip())
    ore_robot = Materials(int(match.group(1)), 0, 0, 0)
    clay_robot = Materials(int(match.group(2)), 0, 0, 0)
    obsidian_robot = Materials(int(match.group(3)), int(match.group(4)), 0, 0)
    geode_robot = Materials(int(match.group(5)), 0, int(match.group(6)), 0)
    blueprint = Blueprint(ore_robot, clay_robot, obsidian_robot, geode_robot)
    blueprints.append(blueprint)


def possible_geodes(
    blueprint: Blueprint, robots: Materials, materials: Materials, time: int
) -> int:
    # Assume that each robot creates a material for each robot type
    ore_materials = copy(materials)
    clay_materials = copy(materials)
    obsidian_materials = copy(materials)
    geode_materials = copy(materials)
    for _ in range(time):
        new_robots = Materials(0, 0, 0, 0)
        if ore_materials.contains(blueprint.ore_robot):
            new_robots.ore = 1
            ore_materials -= blueprint.ore_robot
        if clay_materials.contains(blueprint.clay_robot):
            new_robots.clay = 1
            clay_materials -= blueprint.clay_robot
        if obsidian_materials.contains(blueprint.obsidian_robot):
            new_robots.obsidian = 1
            obsidian_materials -= blueprint.obsidian_robot
        if geode_materials.contains(blueprint.geode_robot):
            new_robots.geodes = 1
            geode_materials -= blueprint.geode_robot
        ore_materials += robots
        clay_materials += robots
        obsidian_materials += robots
        geode_materials += robots
        robots += new_robots
    return geode_materials.geodes


def max_geodes(
    blueprint: Blueprint, robots: Materials, materials: Materials, time: int, best: int
) -> int:
    if time == 0:
        return materials.geodes
    if possible_geodes(blueprint, robots, materials, time) <= best:
        return best
    # Do nothing
    best = max(best, max_geodes(blueprint, robots, materials + robots, time - 1, best))
    # Build Ore robot
    if materials.contains(blueprint.ore_robot):
        best = max(
            best,
            max_geodes(
                blueprint,
                robots + Materials(1, 0, 0, 0),
                materials - blueprint.ore_robot + robots,
                time - 1,
                best,
            ),
        )
    # Build Clay robot
    if materials.contains(blueprint.clay_robot):
        best = max(
            best,
            max_geodes(
                blueprint,
                robots + Materials(0, 1, 0, 0),
                materials - blueprint.clay_robot + robots,
                time - 1,
                best,
            ),
        )
    # Build Obsidian robot
    if materials.contains(blueprint.obsidian_robot):
        best = max(
            best,
            max_geodes(
                blueprint,
                robots + Materials(0, 0, 1, 0),
                materials - blueprint.obsidian_robot + robots,
                time - 1,
                best,
            ),
        )
    # Build Geode robot
    if materials.contains(blueprint.geode_robot):
        best = max(
            best,
            max_geodes(
                blueprint,
                robots + Materials(0, 0, 0, 1),
                materials - blueprint.geode_robot + robots,
                time - 1,
                best,
            ),
        )
    return best


quality_sum = 0
for i, blueprint in enumerate(blueprints, start=1):
    quality_sum += i * max_geodes(
        blueprint, Materials(1, 0, 0, 0), Materials(0, 0, 0, 0), 24, 0
    )

print(f"Part 1: {quality_sum}")

part2 = 1
for blueprint in blueprints[:3]:
    part2 *= max_geodes(blueprint, Materials(1, 0, 0, 0), Materials(0, 0, 0, 0), 32, 0)

print(f"Part 2: {part2}")
