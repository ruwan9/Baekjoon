import sys
sys.stdin = open('./input.txt')


def flip(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if arrA[i][j] == '1':
                arrA[i][j] = '0'
            else:
                arrA[i][j] = '1'

N, M = map(int, input().split())
arrA = [list(input()) for _ in range(N)]
arrB = [list(input()) for _ in range(N)]
cnt = 0

for i in range(N-2):
    for j in range(M-2):
        if arrA[i][j] != arrB[i][j]:
            flip(i, j)
            cnt += 1

res = 0
if arrA != arrB:
    res = 1

if res == 1:
    print(-1)
else:
    print(cnt)