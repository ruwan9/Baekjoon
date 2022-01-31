import sys
sys.stdin = open('input.txt')

N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, input().split())))

for i in range(1, N):
    houses[i][0] += min(houses[i - 1][1], houses[i - 1][2])
    houses[i][1] += min(houses[i - 1][0], houses[i - 1][2])
    houses[i][2] += min(houses[i - 1][0], houses[i - 1][1])

res = min(houses[N-1])
print(res)