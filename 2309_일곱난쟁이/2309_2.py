import sys
sys.stdin = open('../inputs/2309.txt')
from itertools import combinations

heights = list(int(input()) for _ in range(9))
for dwarves in combinations(heights, 7):
    if sum(dwarves) == 100:
        for dwarf in sorted(dwarves):
            print(dwarf)

        break
