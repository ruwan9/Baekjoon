import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0

    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            res += arr[i][j]

    print(res)


# 시간초과...