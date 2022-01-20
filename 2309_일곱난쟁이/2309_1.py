import sys
sys.stdin = open('../inputs/2309.txt')
from itertools import combinations

dwarves = list(int(input()) for _ in range(9))

liars = list(combinations(dwarves, 2))

for liar in liars:
    if sum(dwarves) - sum(liar) == 100:
        dwarves.remove(liar[0])
        dwarves.remove(liar[1])
        break

for dwarf in sorted(dwarves):
    print(dwarf)