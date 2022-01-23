import sys
sys.stdin = open('./input.txt')
from itertools import combinations

heights = list(int(input()) for _ in range(9))
for dwarves in combinations(heights, 7):
    if sum(dwarves) == 100:
        for dwarf in sorted(dwarves):
            print(dwarf)

        break
