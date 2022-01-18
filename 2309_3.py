import sys
sys.stdin = open('inputs/2309.txt')

heights = sorted(list(int(input()) for _ in range(9)))
tot = sum(heights)


def check():
    for i in range(9):
        for j in range(i+1, 9):
            if tot - heights[i] - heights[j] == 100:
                for k in range(9):
                    if i != k and j != k:
                        print(heights[k])

                return


check()