import sys

part1_total = 0
part2_total = 0
for line in sys.stdin:
    [opponent, me] = line.split(" ")
    opponent = ord(opponent.strip()) - ord("A")
    me = ord(me.strip()) - ord("X")
    outcome = (me - opponent) % 3
    score = me + 1 + [3, 6, 0][outcome]
    part1_total += score

    desired_outcome = me - 1
    best_play = (desired_outcome + opponent) % 3
    score = best_play + 1 + [3, 6, 0][desired_outcome]
    part2_total += score

print(f"Part 1: {part1_total}")
print(f"Part 2: {part2_total}")
