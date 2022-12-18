from operator import add, lt, gt
import sys

cubes = set()

for i, cube in enumerate(sys.stdin):
    [x, y, z] = cube.strip().split(",")
    cube = (int(x), int(y), int(z))
    cubes.add(cube)
    if i == 0:
        min_pos = cube
        max_pos = cube
    else:
        min_pos = tuple(map(min, min_pos, cube))
        max_pos = tuple(map(max, max_pos, cube))

min_pos = (min_pos[0] - 1, min_pos[1] - 1, min_pos[2] - 1)
max_pos = (max_pos[0] + 1, max_pos[1] + 1, max_pos[2] + 1)

steam = set()

faces = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]


candidates = [min_pos]
while len(candidates) > 0:
    candidate = candidates.pop()
    if any(map(lt, candidate, min_pos)) or any(map(gt, candidate, max_pos)):
        continue
    if candidate not in cubes and candidate not in steam:
        steam.add(candidate)
    else:
        continue
    for face in faces:
        candidates.append(tuple(map(add, candidate, face)))


internal_surface_area = 0
external_surface_area = 0
for x, y, z in cubes:
    for x_off, y_off, z_off in faces:
        facing_cube = (x + x_off, y + y_off, z + z_off)
        if facing_cube not in cubes:
            if facing_cube in steam:
                external_surface_area += 1
            else:
                internal_surface_area += 1

print(f"Part 1: {internal_surface_area + external_surface_area}")
print(f"Part 2: {external_surface_area}")
