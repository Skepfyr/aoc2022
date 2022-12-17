import itertools
import re
import sys


class Valve:
    rate: int
    dests: dict[str, int]

    def __init__(self, rate, dests) -> None:
        self.rate = rate
        self.dests = dests

    def __repr__(self) -> str:
        return f"Valve{{rate: {self.rate}, dests: {self.dests}}}"


regex = re.compile(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)")
valves: dict[str, Valve] = dict()
for line in sys.stdin:
    m = re.match(regex, line.strip())
    name = m.group(1)
    rate = int(m.group(2))
    dests = m.group(3).split(", ")
    valves[name] = Valve(rate, dict((dest, 1) for dest in dests))


def closure(location: str, weight: int, dests: dict[str, int]):
    if location in dests and dests[location] <= weight:
        return
    dests[location] = weight
    for dest, additional in valves[location].dests.items():
        closure(dest, weight + additional, dests)


simplified_valves: dict[str, Valve] = dict()
for location, valve in valves.items():
    if location == "AA" or valve.rate > 0:
        dests = dict()
        visited = set()
        closure(location, 0, dests)
        simplified_dests = dict()
        for dest, weight in dests.items():
            if weight in range(1, 30) and valves[dest].rate > 0:
                simplified_dests[dest] = weight
        simplified_valves[location] = Valve(valve.rate, simplified_dests)


valves = simplified_valves


def search(location, minutes_remaining, relieved_pressure, visited: set[str]):
    if location in visited or minutes_remaining <= 0:
        return relieved_pressure
    visited.add(location)

    valve = valves[location]
    max_relieved_pressure = relieved_pressure

    if valve.rate > 0:
        # Open this valve
        minutes_remaining -= 1
        relieved_pressure += valve.rate * minutes_remaining

    for dest, weight in valve.dests.items():
        result = search(
            dest, minutes_remaining - weight, relieved_pressure, visited.copy()
        )
        max_relieved_pressure = max(max_relieved_pressure, result)
    return max_relieved_pressure


max_relieved_pressure = search("AA", 30, 0, set())
print(f"Part 1: {max_relieved_pressure}")

max_total_relieved_pressure = 0
nodes = set(simplified_valves.keys())
nodes.remove("AA")
for size in range((len(nodes) + 1) // 2):
    print(f"{size} of {(len(nodes) + 1) // 2}")
    for elephant_nodes in itertools.combinations(nodes, size):
        elephant_nodes = set(elephant_nodes)
        you_nodes = nodes.difference(elephant_nodes)
        max_you_relieved_pressure = search("AA", 26, 0, elephant_nodes)
        max_elephant_relieved_pressure = search("AA", 26, 0, you_nodes)
        max_total_relieved_pressure = max(
            max_total_relieved_pressure,
            max_you_relieved_pressure + max_elephant_relieved_pressure,
        )
print(f"Part 2: {max_total_relieved_pressure}")
