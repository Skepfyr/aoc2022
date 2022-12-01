import sys

packs = []
pack = []
for item in sys.stdin:
   if not item.strip():
     packs.append(pack)
     pack = []
   else:
     pack.append(int(item))
packs.append(pack)

totals = [sum(pack) for pack in packs]

print(f"Part 1: {max(totals)}")

totals.sort()

print(f"Part 2: {sum(totals[-3:])}")
