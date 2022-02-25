import sys
sys.stdin = open('input.txt')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

tmp = 2
for i in range(1, n):
    for j in range(tmp):
        if j == 0:
            data[i][j] += data[i-1][j]
        elif j == i:
            data[i][j] += data[i-1][j-1]
        else:
            data[i][j] += max(data[i-1][j-1], data[i-1][j])
    tmp += 1
print(max(data[n-1]))